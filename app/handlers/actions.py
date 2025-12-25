import os
import uuid
import smtplib
from email.message import EmailMessage
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
import logging

router = APIRouter()

API_KEY = os.getenv("COHEN_ACTIONS_API_KEY", "CHANGE_ME")
TO_EMAIL = "info@cohenhouse.it"
FROM_EMAIL = os.getenv("FROM_EMAIL", TO_EMAIL)
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_TLS = os.getenv("SMTP_TLS", "1") == "1"
LOG_PATH = "./logs/inquiries.log"

class LeadRequest(BaseModel):
    name: str
    check_in: str
    check_out: str
    adults: int
    children: Optional[int] = 0
    children_ages: Optional[str] = ""
    apartment_preference: Optional[str] = ""
    arrival_time: Optional[str] = ""
    key_logistics_needs: Optional[str] = ""
    special_requests: Optional[str] = ""
    contact_email: Optional[str] = ""
    contact_whatsapp: Optional[str] = ""

def verify_api_key(x_api_key: str):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

def send_email(subject: str, body: str, reply_to: Optional[str] = None):
    if not SMTP_HOST:
        logging.warning("⚠️ SMTP not configured - email not sent")
        return
    
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content(body)
    
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as s:
            if SMTP_TLS:
                s.starttls()
            if SMTP_USER:
                s.login(SMTP_USER, SMTP_PASS)
            s.send_message(msg)
        print(f"✅ Email sent to {TO_EMAIL}")
    except Exception as e:
        print(f"❌ Email error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/lead")
async def create_lead(data: LeadRequest, x_api_key: str = Header(None, alias="X-API-Key")):
    verify_api_key(x_api_key)
    lead_id = str(uuid.uuid4())
    
    subject = f"Cohen House Inquiry – {data.check_in} to {data.check_out} – {data.name}"
    body = "\n".join([
        f"Lead ID: {lead_id}",
        f"Name: {data.name}",
        f"Dates: {data.check_in} to {data.check_out}",
        f"Guests: {data.adults} adults, {data.children} children" + (f" (ages {data.children_ages})" if data.children_ages else ""),
        f"Apartment: {data.apartment_preference}",
        f"Arrival: {data.arrival_time}",
        f"Logistics: {data.key_logistics_needs}",
        f"Requests: {data.special_requests}",
        f"Email: {data.contact_email}",
        f"WhatsApp: {data.contact_whatsapp}",
        "",
        "Sent via Cohen House Concierge"
    ])
    
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(body + "\n\n")
    
    send_email(subject, body, reply_to=data.contact_email or None)
    return {"ok": True, "lead_id": lead_id}
