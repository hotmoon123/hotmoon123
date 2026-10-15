import { Platform } from 'react-native';
import * as SecureStore from 'expo-secure-store';
import * as Crypto from 'expo-crypto';
let token:string|null=null;
const key='stitchledger.session.v2';
export const requestKey=()=>Crypto.randomUUID();
export async function restoreToken(){token=Platform.OS==='web'?sessionStorage.getItem(key):await SecureStore.getItemAsync(key);return token;}
export async function saveToken(value:string|null){token=value;if(Platform.OS==='web'){value?sessionStorage.setItem(key,value):sessionStorage.removeItem(key);}else{value?await SecureStore.setItemAsync(key,value):await SecureStore.deleteItemAsync(key);}}
export class ApiError extends Error{constructor(public status:number,msg:string){super(msg);}}
export async function api<T=any>(path:string,method='GET',body?:unknown,id?:string):Promise<T>{
 const base=(process.env.EXPO_PUBLIC_API_URL||'').replace(/\/$/,'');
 if(Platform.OS!=='web'&&!base)throw new Error('Set EXPO_PUBLIC_API_URL to your reachable HTTPS backend, then restart the mobile bundler.');
 if(Platform.OS!=='web'&&base&&!base.startsWith('https://')&&!__DEV__)throw new Error('Release builds require an HTTPS backend.');
 const controller=new AbortController();const timeout=setTimeout(()=>controller.abort(),25000);
 try{
  const response=await fetch(base+'/api'+path,{method,headers:{'Content-Type':'application/json',...(token?{Authorization:'Bearer '+token}:{}),...(id?{'Idempotency-Key':id}:{})},body:body===undefined?undefined:JSON.stringify(body),signal:controller.signal});
  if(!response.ok){let d=await response.json().catch(()=>({detail:'Unexpected server response'}));throw new ApiError(response.status,typeof d.detail==='string'?d.detail:Array.isArray(d.detail)?d.detail.map((e:any)=>`${e.loc?.slice(1).join('.')}: ${e.msg}`).join('\n'):'Request failed');}
  if(response.status===204)return undefined as T;
  if(path.endsWith('.csv'))return await response.text() as T;
  return await response.json();
 }catch(e){if(e instanceof ApiError)throw e;throw new Error('Unable to reach the server. Check your connection. If saving a payment, retry without changing the form; the same request will not be counted twice.');}finally{clearTimeout(timeout);}
}
export type User={id:string;email:string;studio:string;demo:number};
export type Order={id:string;customer:string;garment:string;due:string;total:number;paid:number;status:string;notes:string;version:number;created:string;payments?:Payment[];audit?:{action:string;detail:string;created:string}[]};
export type Payment={id:string;order_id:string;amount:number;method:string;note:string;created:string;customer?:string;garment?:string};
export const money=(n:number)=>'GH₵ '+(n/100).toLocaleString('en-GH',{minimumFractionDigits:2,maximumFractionDigits:2});
export function cents(v:string){if(!/^\d+(\.\d{1,2})?$/.test(v))throw new Error('Enter a positive amount with up to two decimal places.');const [a,b='']=v.split('.');const n=Number(a)*100+Number(b.padEnd(2,'0'));if(!Number.isSafeInteger(n)||n>100000000)throw new Error('Amount is too large.');return n;}
export const dateKey=()=>{const d=new Date();return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;};
export const closed=(o:Order)=>['Collected','Cancelled'].includes(o.status);
export const transitions:Record<string,string[]>={Booked:['Cutting','Cancelled'],Cutting:['Booked','Sewing','Cancelled'],Sewing:['Cutting','Ready','Cancelled'],Ready:['Sewing','Collected','Cancelled'],Collected:[],Cancelled:[]};
