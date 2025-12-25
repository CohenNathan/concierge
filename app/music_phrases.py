"""
Dramatic music phrases for Solomon the Bear
"""
import random

# Dramatic opening phrase before music
MUSIC_FIRE_PHRASE = "Orchestra, let turn the silence into fire. One breath, one will, no mercy - FIRE!"

# Traditional music phrases
TRADITIONAL_PHRASES = [
    "Sicilian warriors dance! Ancient rhythms awaken!",
    "Pizzica erupts! The island calls its children!",
    "Ancestral drums thunder! Sicily remembers!"
]

# Fun/Party music phrases  
FUN_PHRASES = [
    "FORWARD! Chaos is our ally! Vogliamo le bambole!",
    "Madness unleashed! Let joy explode!",
    "The party ignites! No rules, only rhythm!"
]

# Romantic music phrases
ROMANTIC_PHRASES = [
    "Hearts collide! L'impero begins!",
    "Love conquers all! Mannarino speaks!",
    "Romance blooms! Sicily's passion flows!"
]

# Political/Cultural music phrases
POLITICAL_PHRASES = [
    "Cultural thunder! Deija na Marinno rises!",
    "Voices unite! The people's anthem!",
    "History speaks! Tradition endures!"
]

def get_music_phrase(music_type: str) -> str:
    """Get dramatic phrase for music type"""
    phrases = {
        'traditional': TRADITIONAL_PHRASES,
        'fun': FUN_PHRASES,
        'romantic': ROMANTIC_PHRASES,
        'political': POLITICAL_PHRASES
    }
    
    selected = phrases.get(music_type, TRADITIONAL_PHRASES)
    return f"{MUSIC_FIRE_PHRASE} {random.choice(selected)}"
