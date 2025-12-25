import subprocess
from app.utils.window_manager import window_manager

class BrowserController:
    def __init__(self):
        print("✅ Browser controller ready")
    
    def open_website(self):
        """Open Cohen House website behind Solomon"""
        return window_manager.open_url_behind_solomon("https://cohenhouse.it", "Cohen House")
    
    def open_skyscanner(self):
        """Open Skyscanner behind Solomon"""
        return window_manager.open_url_behind_solomon("https://www.skyscanner.com/transport/flights//CTA/", "Skyscanner")
    
    def open_etna(self):
        """Open Etna Trasporti behind Solomon"""
        return window_manager.open_url_behind_solomon("https://www.etnatrasporti.it/travel-plan/solution.php", "Etna Trasporti")
    
    def open_trenitalia(self):
        """Open Trenitalia behind Solomon"""
        return window_manager.open_url_behind_solomon("https://www.trenitalia.com/it.html", "Trenitalia")

browser = BrowserController()
