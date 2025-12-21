QUICK_RESPONSES = {
    'it': {
        # Greetings
        'mi senti': "Sì, ti sento perfettamente!",
        'buongiorno': "Buongiorno! Benvenuto a Cohen House.",
        'buonasera': "Buonasera! Come posso aiutarti?",
        'ciao': "Ciao! Come posso aiutarti?",
        'salve': "Salve! Benvenuto!",
        
        # Language
        'parli inglese': "Sì, parlo inglese. How can I help?",
        'parli italiano': "Certo! Sono Solomon, il tuo assistente.",
        
        # Location
        'dove': "Via Nazionale, 20 metri da Isola Bella.",
        'dove siete': "Via Nazionale, 20 metri da Isola Bella.",
        'indirizzo': "Via Nazionale, Taormina, vicino a Isola Bella.",
        'spiaggia': "Isola Bella è a 20 metri da qui!",
        'mare': "Il mare è vicinissimo, 20 metri!",
        
        # Shopping
        'supermercato': "Sotto di noi, di fronte Isola Bella!",
        'negozi': "Il supermercato è sotto di noi, altri negozi in centro.",
        'spesa': "Supermercato proprio sotto di noi!",
        
        # Prices
        'prezzo': "€450-500/notte. Diretto: -20%!",
        'quanto costa': "€450-500/notte. Prenota diretto per -20%!",
        'costo': "€450-500 a notte. Sconto 20% su cohenhouse.it!",
        
        # Apartments
        'boho': "BOHO: 100m², 10 ospiti, €500/notte, terrazza vista Etna!",
        'vintage': "VINTAGE: 90m², 8 ospiti, €450/notte, balcone su Isola Bella!",
        'shabby': "SHABBY: 90m², 8 ospiti, €450/notte, stile shabby chic!",
        'appartamenti': "3 appartamenti: BOHO, VINTAGE, SHABBY. Vuoi dettagli?",
        
        # Booking
        'prenotare': "Prenota su www.cohenhouse.it - Sconto 20%!",
        'disponibilità': "Controlla su www.cohenhouse.it per date disponibili!",
        'libro': "Prenota direttamente su cohenhouse.it per il miglior prezzo!",
        
        # Music
        'musica': "FIRE!",
        'canzone': "FIRE!",
        
        # Name
        'chi sei': "Sono Solomon, il tuo orso concierge AI!",
        'nome': "Mi chiamo Solomon!",
        
        # Thanks
        'grazie': "Prego! Sono qui per aiutarti!",
    },
    'en': {
        # Greetings
        'hello': "Hello! Welcome to Cohen House.",
        'hi': "Hi! How can I help you?",
        'good morning': "Good morning! Welcome!",
        'good evening': "Good evening! How can I assist?",
        
        # Language
        'speak italian': "Sì! Posso parlare italiano!",
        'speak english': "Yes, I speak English. How can I help?",
        
        # Location
        'where': "Via Nazionale, 20 meters from Isola Bella.",
        'location': "Via Nazionale, Taormina, 20m from the beach!",
        'address': "Via Nazionale, Taormina, Sicily.",
        'beach': "Isola Bella beach is just 20 meters away!",
        'sea': "The sea is super close, only 20 meters!",
        
        # Shopping
        'supermarket': "Below us, opposite Isola Bella!",
        'shop': "Supermarket below us, more shops in town center.",
        'grocery': "Grocery store right below Cohen House!",
        
        # Prices
        'price': "€450-500/night. Direct: save 20%!",
        'cost': "€450-500 per night. Book direct at cohenhouse.it for 20% off!",
        'how much': "€450-500/night. Save 20% booking direct!",
        
        # Apartments
        'boho': "BOHO: 100m², 10 guests, €500/night, terrace with Etna view!",
        'vintage': "VINTAGE: 90m², 8 guests, €450/night, balcony over Isola Bella!",
        'shabby': "SHABBY: 90m², 8 guests, €450/night, shabby chic style!",
        'apartments': "3 apartments: BOHO, VINTAGE, SHABBY. Want details?",
        
        # Booking
        'book': "Book at www.cohenhouse.it - Save 20%!",
        'reserve': "Reserve directly at cohenhouse.it for best price!",
        'availability': "Check www.cohenhouse.it for available dates!",
        
        # Music
        'music': "FIRE!",
        'song': "FIRE!",
        
        # Name
        'who are you': "I'm Solomon, your AI bear concierge!",
        'your name': "I'm Solomon!",
        
        # Thanks
        'thank': "You're welcome! Here to help!",
        'thanks': "My pleasure! Anything else?",
    }
}

def get_quick_response(text: str, lang: str):
    if not text or not lang:
        return None, False
    
    text_lower = text.lower()
    responses = QUICK_RESPONSES.get(lang, {})
    
    for keyword, response in responses.items():
        if keyword in text_lower:
            is_music = keyword in ['musica', 'music', 'canzone', 'song']
            print(f"⚡ INSTANT: {keyword}")
            return response, is_music
    
    return None, False
