import {Platform} from 'react-native';
import * as Notifications from 'expo-notifications';
import {Order,closed} from './api';

const CHANNEL='stitchledger-order-reminders';
const DAILY_KIND='stitchledger.daily-workflow';
const ORDER_KIND='stitchledger.order-due';
export const DAILY_REMINDER_HOUR=8;

// Notifications are deliberately generic: a locked phone should not reveal customer names,
// garment details, balances or production notes. The authenticated app reveals those details.
if(Platform.OS!=='web'){
  Notifications.setNotificationHandler({
    handleNotification:async()=>({
      shouldShowBanner:true,
      shouldShowList:true,
      shouldPlaySound:true,
      shouldSetBadge:false,
      priority:Notifications.AndroidNotificationPriority.DEFAULT,
    }),
  });
}

export type ReminderResult={scheduled:boolean;message:string};
export type ReminderTarget={kind:'daily'|'order'|'unknown';orderId:string};

function native(){return Platform.OS!=='web';}
function dataKind(value:unknown):string{
  return value&&typeof value==='object'&&typeof (value as Record<string,unknown>).kind==='string'
    ?String((value as Record<string,unknown>).kind):'';
}
function orderId(value:unknown):string{
  return value&&typeof value==='object'&&typeof (value as Record<string,unknown>).orderId==='string'
    ?String((value as Record<string,unknown>).orderId):'';
}
function target(value:unknown):ReminderTarget{
  const kind=dataKind(value);
  if(kind===DAILY_KIND)return {kind:'daily',orderId:''};
  if(kind===ORDER_KIND)return {kind:'order',orderId:orderId(value)};
  return {kind:'unknown',orderId:''};
}

export function listenForReminderResponse(callback:(target:ReminderTarget)=>void){
  if(!native())return {remove:()=>undefined};
  return Notifications.addNotificationResponseReceivedListener(response=>callback(target(response.notification.request.content.data)));
}

export function lastReminderTarget():ReminderTarget{
  if(!native())return {kind:'unknown',orderId:''};
  return target(Notifications.getLastNotificationResponse()?.notification.request.content.data);
}

export function clearLastReminderResponse(){
  if(native())Notifications.clearLastNotificationResponse();
}

async function readyForLocalNotifications():Promise<boolean>{
  if(!native())return false;
  if(Platform.OS==='android'){
    await Notifications.setNotificationChannelAsync(CHANNEL,{
      name:'Order reminders',
      description:'Daily StitchLedger workflow and due-date reminders',
      importance:Notifications.AndroidImportance.DEFAULT,
      sound:'default',
      vibrationPattern:[0,180,120,180],
      enableVibrate:true,
      showBadge:false,
    });
  }
  let permissions=await Notifications.getPermissionsAsync();
  if(!permissions.granted)permissions=await Notifications.requestPermissionsAsync();
  return permissions.granted;
}

async function cancelWhere(predicate:(request:Notifications.NotificationRequest)=>boolean){
  if(!native())return;
  const scheduled=await Notifications.getAllScheduledNotificationsAsync();
  await Promise.all(scheduled.filter(predicate).map(item=>Notifications.cancelScheduledNotificationAsync(item.identifier)));
}

export async function dailyWorkflowReminderScheduled(){
  if(!native())return false;
  const scheduled=await Notifications.getAllScheduledNotificationsAsync();
  return scheduled.some(item=>dataKind(item.content.data)===DAILY_KIND);
}

export async function enableDailyWorkflowReminder(activeOrders:Order[]):Promise<ReminderResult>{
  if(!native())return {scheduled:false,message:'Daily device notifications are available in the Android or iPhone app, not in the browser preview.'};
  if(!activeOrders.length)return {scheduled:false,message:'Book or keep at least one active order before turning on a daily workflow reminder.'};
  if(!await readyForLocalNotifications())return {scheduled:false,message:'Notification permission was not granted. You can turn it on later in your phone settings.'};
  await cancelWhere(item=>dataKind(item.content.data)===DAILY_KIND);
  await Notifications.scheduleNotificationAsync({
    content:{
      title:'Your StitchLedger check-in',
      body:'Review booked, cutting, sewing, ready and overdue work in your order book.',
      data:{kind:DAILY_KIND,screen:'daily-check-in'},
    },
    trigger:{
      type:Notifications.SchedulableTriggerInputTypes.DAILY,
      hour:DAILY_REMINDER_HOUR,
      minute:0,
      channelId:CHANNEL,
    },
  });
  return {scheduled:true,message:'Daily workflow reminder set for 8:00 AM on this device.'};
}

export async function disableDailyWorkflowReminder(){
  await cancelWhere(item=>dataKind(item.content.data)===DAILY_KIND);
}

function reminderDate(order:Order,daysBefore:number){
  const target=new Date(`${order.due}T08:00:00`);
  target.setDate(target.getDate()-daysBefore);
  return target;
}

function tomorrowAtEight(){
  const target=new Date();
  target.setDate(target.getDate()+1);
  target.setHours(8,0,0,0);
  return target;
}

async function scheduleAt(order:Order,targetDate:Date,label:string):Promise<ReminderResult>{
  if(!native())return {scheduled:false,message:'Order reminders are available in the Android or iPhone app, not in the browser preview.'};
  if(closed(order))return {scheduled:false,message:'Closed orders do not receive reminders.'};
  if(targetDate.getTime()<=Date.now())return {scheduled:false,message:'That reminder time has passed. Update the collection date or choose a future reminder.'};
  if(!await readyForLocalNotifications())return {scheduled:false,message:'Notification permission was not granted. You can turn it on later in your phone settings.'};
  await cancelWhere(item=>dataKind(item.content.data)===ORDER_KIND&&orderId(item.content.data)===order.id);
  await Notifications.scheduleNotificationAsync({
    content:{
      title:'StitchLedger order reminder',
      body:'Open StitchLedger to review an active order.',
      data:{kind:ORDER_KIND,orderId:order.id,screen:'order'},
    },
    trigger:{type:Notifications.SchedulableTriggerInputTypes.DATE,date:targetDate,channelId:CHANNEL},
  });
  return {scheduled:true,message:`${label} at ${targetDate.toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short'})} 8:00 AM.`};
}

export async function scheduleOrderReminder(order:Order,daysBefore:number):Promise<ReminderResult>{
  return scheduleAt(order,reminderDate(order,daysBefore),'Collection reminder set for');
}

export async function scheduleTomorrowReminder(order:Order):Promise<ReminderResult>{
  return scheduleAt(order,tomorrowAtEight(),'Order reminder set for tomorrow');
}
