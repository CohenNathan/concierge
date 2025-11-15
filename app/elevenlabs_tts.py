from __future__ import annotations
import os

class ElevenLabsTTS:
    """Safe stub – if ELEVENLABS_API_KEY липсва, просто не се ползва."""
    def __init__(self) -> None:
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            print("⚠ ELEVENLABS_API_KEY is not set – ElevenLabsTTS is disabled, AzureTTS ще се използва.")
            self.enabled = False
        else:
            self.enabled = True

    async def generate(self, text: str, lang: str = "en") -> dict:
        """
        Този проект в момента използва AzureTTS. Този метод е само placeholder.
        Ако някъде бъде извикан, вдигаме ясна грешка.
        """
        raise RuntimeError("ElevenLabsTTS е изключен – използвай AzureTTS.")
