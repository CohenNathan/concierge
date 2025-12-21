from fastapi import APIRouter, HTTPException, Header
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# API key за сигурност
BOOKING_API_KEY = os.getenv("BOOKING_API_KEY", "sk_booking_secret_2025")

@router.post("/api/check-availability")
async def check_availability(
    check_in: str,
    check_out: str,
    guests: int,
    x_api_key: str = Header(None)
):
    """Check availability for booking - called by Custom GPT"""
    
    # Verify API key
    if x_api_key != BOOKING_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # TODO: Интегрирай с твоя booking manager
    # Засега връща mock data
    
    available_apartments = []
    
    if guests <= 8:
        available_apartments.append({
            "name": "Appartamento 2",
            "size": "90m²",
            "capacity": 8,
            "price_per_night": 450,
            "available": True
        })
        available_apartments.append({
            "name": "Appartamento 3", 
            "size": "90m²",
            "capacity": 8,
            "price_per_night": 450,
            "available": True
        })
    
    if guests <= 10:
        available_apartments.append({
            "name": "Appartamento 1",
            "size": "100m²", 
            "capacity": 10,
            "price_per_night": 500,
            "available": True
        })
    
    return {
        "check_in": check_in,
        "check_out": check_out,
        "guests": guests,
        "available_apartments": available_apartments,
        "total_apartments": len(available_apartments)
    }

@router.post("/api/create-reservation")
async def create_reservation(
    apartment_name: str,
    check_in: str,
    check_out: str,
    guests: int,
    guest_name: str,
    guest_email: str,
    guest_phone: str,
    x_api_key: str = Header(None)
):
    """Create reservation request - called by Custom GPT"""
    
    if x_api_key != BOOKING_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # TODO: Интегрирай с booking manager
    # Засега връща mock confirmation
    
    reservation_id = f"RES-{hash(guest_email) % 100000}"
    
    return {
        "success": True,
        "reservation_id": reservation_id,
        "status": "pending_confirmation",
        "message": "Reservation request received. Cohen House will contact you within 2 hours.",
        "apartment": apartment_name,
        "check_in": check_in,
        "check_out": check_out,
        "guests": guests,
        "contact_email": "info@cohenhouse.com",
        "contact_whatsapp": "+39 347 887 9992"
    }
