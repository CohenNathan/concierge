QUICK_RESPONSES = {
    'it': {
        'mi senti': "Sì, ti sento perfettamente!",
        'buongiorno': "Buongiorno! Benvenuto a Cohen House.",
        'ciao': "Ciao! Come posso aiutarti?",
        'parli inglese': "Sì, parlo inglese. How can I help?",
        'dove': "Via Nazionale, 20 metri da Isola Bella.",
        'supermercato': "Sotto di noi, di fronte Isola Bella!",
        'prezzo': "€450-500/notte. Diretto: -20%!",
        'musica': "FIRE!",
    },
    'en': {
        'hello': "Hello! Welcome to Cohen House.",
        'where': "Via Nazionale, 20 meters from Isola Bella.",
        'supermarket': "Below us, opposite Isola Bella!",
        'price': "€450-500/night. Direct: save 20%!",
        'music': "FIRE!",
    }
}

def get_quick_response(text: str, lang: str):
    if not text or not lang:
        return None, False
    
    text_lower = text.lower()
    responses = QUICK_RESPONSES.get(lang, {})
    
    for keyword, response in responses.items():
        if keyword in text_lower:
            is_music = keyword in ['musica', 'music']
            print(f"⚡ INSTANT: {keyword}")
            return response, is_music
    
    return None, False
