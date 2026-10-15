"""Optional, opt-in drafting adapter. No tools, no money mutations, no names sent."""
import os,httpx
from fastapi import HTTPException

def available():return bool(os.getenv('OPENAI_API_KEY') and os.getenv('AI_MODEL'))
def draft(status,due):
 if not available():raise HTTPException(503,'AI is not configured. The free message template still works.')
 try:
  r=httpx.post('https://api.openai.com/v1/responses',headers={'Authorization':'Bearer '+os.environ['OPENAI_API_KEY']},json={'model':os.environ['AI_MODEL'],'store':False,'max_output_tokens':180,'instructions':'Write one brief, polite tailoring studio customer update. Use only the provided status and scheduled date. Do not claim a garment is ready unless status is Ready. Do not invent guarantees, names, prices, discounts or payment details. No markdown. This is a draft a human must review.','input':f'Status: {status}. Scheduled collection date: {due}.'},timeout=20)
  r.raise_for_status();d=r.json();text=' '.join(x['text'] for o in d.get('output',[]) for x in o.get('content',[]) if x.get('type')=='output_text')
  if not text.strip():raise ValueError()
  return text[:1500]
 except (httpx.HTTPError,ValueError,KeyError):raise HTTPException(502,'AI provider unavailable. Use the template instead.')
