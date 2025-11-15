import os
import time
from ring_doorbell import Auth, Ring
from dotenv import load_dotenv

load_dotenv()

REFRESH_TOKEN = os.environ.get("RING_REFRESH_TOKEN")
if not REFRESH_TOKEN:
    print("Грешка: Липсва RING_REFRESH_TOKEN в .env")
    exit(1)

def token_updater(token: str) -> None:
    token_file = os.path.expanduser("~/.ring_token.json")
    with open(token_file, "w") as f:
        f.write(token)

print("Стартирам Ring listener (sync режим)...")

auth = Auth("Concierge/1.0", None, token_updater)

try:
    auth.load_token_from_refresh(REFRESH_TOKEN)
    print("Автентикация с refresh token – УСПЕХ")
except Exception as e:
    print("Грешка при автентикация:", e)
    exit(1)

ring = Ring(auth)
print("ring.authenticated =", ring.authenticated)

try:
    ring.update_devices()
    print("Устройствата са обновени")
except Exception as e:
    print("Грешка при update_devices():", e)
    exit(1)

devices = ring.devices()
if not isinstance(devices, dict):
    print("ГРЕШКА: ring.devices() връща:", devices)
    exit(1)

doorbells = devices.get("doorbots", [])
if not doorbells:
    print("Няма намерени звънци.")
    exit(0)

print(f"Намерени: {[d.name for d in doorbells]}")
print("Слушам за звънене...")

last_ding_id = None
while True:
    for doorbell in doorbells:
        try:
            history = doorbell.history(limit=1, kind="ding")
            if history:
                ding = history[0]
                ding_id = ding.get("id")
                if ding_id and ding_id != last_ding_id and ding.get("state") == "ringing":
                    last_ding_id = ding_id
                    print(f"ЗВЪНЕЦ! {doorbell.name}")
        except:
            pass
    time.sleep(2)
