# Configuration constants for Cohen House Concierge
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
BOOKING_API_KEY = os.getenv("BOOKING_API_KEY", "sk_booking_secret_2025")
COHEN_ACTIONS_API_KEY = os.getenv("COHEN_ACTIONS_API_KEY", "CHANGE_ME")

# Email Configuration
TO_EMAIL = "info@cohenhouse.it"
FROM_EMAIL = os.getenv("FROM_EMAIL", TO_EMAIL)
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
SMTP_TLS = os.getenv("SMTP_TLS", "1") == "1"

# Paths
LOG_PATH = "./logs/inquiries.log"

# Application Settings
DEFAULT_LANGUAGE = "it"
