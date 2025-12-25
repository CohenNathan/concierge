import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

async def search_flights(origin:  str, destination: str, date: str = None) -> str:
    """Search for flights using SerpApi Google Flights"""
    if not SERPAPI_KEY: 
        return "⚠️ SerpApi key not configured"
    
    try:
        params = {
            "engine": "google_flights",
            "departure_id": origin,
            "arrival_id":  destination,
            "outbound_date": date or "2025-07-01",
            "currency": "EUR",
            "hl": "it",
            "api_key": SERPAPI_KEY
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if "best_flights" in results and results["best_flights"]:
            flights = results["best_flights"][: 3]
            response = "✈️ Voli trovati:\n\n"
            for i, flight in enumerate(flights, 1):
                price = flight.get("price", "N/A")
                airline = flight["flights"][0]. get("airline", "N/A")
                duration = flight. get("total_duration", "N/A")
                response += f"{i}. {airline} - €{price} ({duration} min)\n"
            return response
        else:
            return "Nessun volo trovato.  Prova su Skyscanner:  https://www.skyscanner.it"
            
    except Exception as e:
        print(f"❌ Flight search error: {e}")
        return f"Cerca voli su Skyscanner: https://www.skyscanner.it/transport/flights/{origin}/{destination}"

async def search_web(query: str, lang: str = "it") -> str:
    """General web search using SerpApi"""
    if not SERPAPI_KEY:
        return "⚠️ SerpApi key not configured"
    
    try:
        params = {
            "engine": "google",
            "q": query,
            "hl": lang,
            "gl": lang,
            "api_key":  SERPAPI_KEY
        }
        
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if "organic_results" in results: 
            top_results = results["organic_results"][:3]
            response = "🔍 Ho trovato:\n\n"
            for i, result in enumerate(top_results, 1):
                title = result.get("title", "N/A")
                link = result.get("link", "N/A")
                snippet = result.get("snippet", "")[: 100]
                response += f"{i}. {title}\n{snippet}...\n{link}\n\n"
            return response
        else:
            return "Nessun risultato trovato."
            
    except Exception as e:
        print(f"❌ Web search error: {e}")
        return "Errore nella ricerca.  Riprova."

def open_spotify(query: str = "italian music") -> str:
    """Generate Spotify link"""
    encoded_query = query.replace(" ", "%20")
    return f"🎵 Apri Spotify: https://open.spotify.com/search/{encoded_query}"
