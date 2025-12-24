"""
═══════════════════════════════════════════════════════════════════
SOLOMON AI CONCIERGE - COMPREHENSIVE CONFIGURATION
Cohen House Taormina - Professional Luxury Concierge System
═══════════════════════════════════════════════════════════════════
"""

# ═════════════════════════════════════════════════════════════════
# ASSISTANT IDENTITY
# ═════════════════════════════════════════════════════════════════
ASSISTANT = {
    "name": "Solomon",
    "full_title": "Solomon, the Magical AI Bear Concierge",
    "role": "Luxury concierge at Cohen House Taormina",
    "personality": "Warm, professional, brief, helpful",
    "languages": ["it", "en"],
    "response_style": "1-3 sentences maximum, direct answers, no fluff"
}

# ═════════════════════════════════════════════════════════════════
# COHEN HOUSE - PROPERTY DETAILS
# ═════════════════════════════════════════════════════════════════
COHEN_HOUSE = {
    "name": "Cohen House",
    "location": {
        "address": "Via Nazionale",
        "city": "Taormina",
        "region": "Sicily, Italy",
        "distance_to_isola_bella": "20 meters walk",
        "distance_to_beach": "2 minutes walk to Isola Bella beach",
        "distance_to_taormina_center": "5 minutes by car, 15 minutes walk uphill"
    },
    "contact": {
        "website": "www.cohenhouse.it",
        "email": "info@cohenhouse.com",
        "whatsapp": "+39 347 887 9992",
        "phone": "+39 347 887 9992"
    },
    "check_in": {
        "time": "15:00 onwards (flexible with EKEY system)",
        "late_check_in": "No fee - EKEY system allows 24/7 access with personal code",
        "early_check_in": "Subject to availability, contact in advance",
        "system": "EKEY code access system - guests receive personal code via email/WhatsApp",
        "no_physical_keys": "No physical keys needed - digital code access only"
    },
    "check_out": {
        "time": "10:00 standard",
        "late_check_out": "FREE if no next-day reservation - MUST contact concierge for approval",
        "approval_process": "Concierge checks next-day bookings and coordinates with cleaning company",
        "why_inform": "Concierge must call cleaning company to reschedule if late check-out approved",
        "no_fee": "No late check-out fee, but approval required",
        "system": "EKEY code remains active until approved departure time"
    }
}

# ═════════════════════════════════════════════════════════════════
# APARTMENTS - DETAILED SPECIFICATIONS
# ═════════════════════════════════════════════════════════════════
APARTMENTS = {
    "BOHO": {
        "name": "Boho Apartment",
        "size_sqm": 100,
        "capacity_max": 10,
        "bedrooms": "3-4 bedrooms",
        "bathrooms": 1,
        "style": "Bohemian design with warm colors, natural textiles, ethnic influences",
        "features": [
            "Large terrace with panoramic sea and Mount Etna view",
            "Fully equipped kitchen",
            "Air conditioning in all rooms",
            "Free WiFi",
            "Washing machine",
            "Smart TV",
            "Vintage furniture and decorations"
        ],
        "sleeping_arrangements": "3 double beds, 4 single beds",
        "pricing": {
            "high_season_per_night": 500,
            "currency": "EUR",
            "season": "June-September"
        },
        "best_for": "Large families, groups, bohemian lovers"
    },
    "VINTAGE": {
        "name": "Vintage Apartment",
        "size_sqm": 90,
        "capacity_max": 8,
        "bedrooms": "2-3 bedrooms",
        "bathrooms": 1,
        "style": "Sicilian & Venetian Baroque - antique baroque furniture",
        "features": [
            "Balcony overlooking Isola Bella Nature Reserve",
            "Authentic baroque antique furniture",
            "Fully equipped kitchen",
            "Air conditioning",
            "Free WiFi",
            "Washing machine",
            "Smart TV"
        ],
        "sleeping_arrangements": "2 double beds, 4 single beds",
        "pricing": {
            "high_season_per_night": 450,
            "currency": "EUR",
            "season": "June-September"
        },
        "best_for": "Couples, families who love classic elegance"
    },
    "SHABBY": {
        "name": "Shabby Chic Apartment",
        "size_sqm": 90,
        "capacity_max": 8,
        "bedrooms": "2-3 bedrooms",
        "bathrooms": 1,
        "style": "Shabby Chic - romantic vintage with pastel colors",
        "features": [
            "Balcony and/or terrace",
            "Pastel color scheme",
            "Fully equipped kitchen",
            "Air conditioning",
            "Free WiFi",
            "Washing machine",
            "Smart TV",
            "Romantic vintage decor"
        ],
        "sleeping_arrangements": "2 double beds, 4 single beds",
        "pricing": {
            "high_season_per_night": 450,
            "currency": "EUR",
            "season": "June-September"
        },
        "best_for": "Romantic couples, small families, vintage lovers"
    }
}

# ═════════════════════════════════════════════════════════════════
# BOOKING & PRICING
# ═════════════════════════════════════════════════════════════════
BOOKING = {
    "direct_booking": {
        "discount_percentage": "20-25%",
        "platforms_commission": "Booking.com/Airbnb take 20-25% commission",
        "message": "Book directly at www.cohenhouse.it and save 20-25%!",
        "payment_methods": ["Bank transfer", "PayPal", "Credit card"],
        "deposit": "30% deposit required to confirm booking"
    },
    "cancellation_policy": {
        "free_cancellation": "Up to 14 days before arrival",
        "50_percent_refund": "7-14 days before arrival",
        "no_refund": "Less than 7 days before arrival"
    },
    "minimum_stay": {
        "high_season": "3 nights minimum (July-August)",
        "mid_season": "2 nights minimum (May-June, September)",
        "low_season": "1 night minimum (October-April)"
    }
}

# ═════════════════════════════════════════════════════════════════
# LOCATION & NEARBY ATTRACTIONS
# ═════════════════════════════════════════════════════════════════
NEARBY = {
    "beaches": {
        "isola_bella": {
            "distance": "20 meters (30 seconds walk)",
            "type": "Nature Reserve, pebble beach",
            "features": "Crystal clear water, connected to island by sand strip",
            "entrance_fee": "€4 (Nature Reserve entrance)",
            "facilities": "Beach clubs, restaurants, restrooms"
        },
        "mazzaro": {
            "distance": "5 minutes walk",
            "type": "Main beach with sand and pebbles",
            "features": "Beach clubs, water sports, restaurants",
            "cable_car": "Cable car to Taormina center from here"
        },
        "giardini_naxos": {
            "distance": "10 minutes drive",
            "type": "Long sandy beach",
            "features": "Family-friendly, many beach clubs and restaurants"
        }
    },
    "supermarkets": {
        "primary": {
            "name": "Local supermarket",
            "location": "Ground floor of Cohen House building",
            "distance": "Directly below apartments",
            "also_location": "Opposite Isola Bella entrance",
            "hours": "8:00-20:00 daily",
            "type": "Full grocery selection"
        },
        "conad": {
            "distance": "5 minutes walk",
            "type": "Larger supermarket chain"
        }
    },
    "restaurants": {
        "la_botte": {
            "distance": "50 meters",
            "specialty": "Fresh fish and seafood",
            "price_range": "€30-45 per person",
            "rating": "Excellent local favorite"
        },
        "la_capinera": {
            "distance": "3 minutes drive",
            "specialty": "Michelin star restaurant",
            "price_range": "€80-120 per person",
            "rating": "1 Michelin star"
        },
        "trattoria_da_nino": {
            "distance": "Taormina center",
            "specialty": "Traditional Sicilian",
            "price_range": "€20-30 per person"
        },
        "bam_bar": {
            "distance": "Taormina center",
            "specialty": "Best granita in Sicily",
            "price_range": "€4-8",
            "famous_for": "Almond granita with brioche"
        }
    },
    "attractions": {
        "greek_theatre": {
            "distance": "5 minutes drive from Cohen House",
            "description": "Ancient Greek theatre with Mount Etna view",
            "entrance_fee": "€10",
            "best_time": "Early morning or sunset"
        },
        "corso_umberto": {
            "description": "Main shopping street in Taormina",
            "features": "Luxury boutiques, cafes, restaurants"
        },
        "castelmola": {
            "distance": "15 minutes drive uphill from Taormina",
            "description": "Medieval village with panoramic views",
            "famous_for": "Almond wine"
        }
    }
}

# ═════════════════════════════════════════════════════════════════
# TRANSPORT - COMPREHENSIVE GUIDE
# ═════════════════════════════════════════════════════════════════
TRANSPORT = {
    "buses": {
        "to_catania": {
            "stop_location": "After Hotel Panoramic (100m from Cohen House)",
            "company": "Etna Trasporti",
            "website": "www.etnatrasporti.it",
            "frequency": "Every 60-90 minutes",
            "journey_time": "70 minutes",
            "price": "€5-7 one way",
            "first_bus": "6:15",
            "last_bus": "20:30",
            "ticket_purchase": "On bus, tobacco shop, or online"
        },
        "to_messina": {
            "stop_location": "At Isola Bella entrance (20m from Cohen House)",
            "company": "Interbus / Etna Trasporti",
            "frequency": "Every 45-60 minutes",
            "journey_time": "50 minutes",
            "price": "€4-6 one way",
            "first_bus": "6:30",
            "last_bus": "21:00"
        },
        "to_taormina_center": {
            "stop_location": "Via Nazionale (in front of building)",
            "company": "Local Taormina buses",
            "frequency": "Every 15-20 minutes",
            "journey_time": "5-10 minutes",
            "price": "€2 one way",
            "alternative": "Cable car from Mazzarò beach"
        }
    },
    "trains": {
        "station_name": "Taormina-Giardini",
        "distance_from_cohen_house": "3 km (5 minutes drive)",
        "taxi_to_station": "€15-20",
        "routes": {
            "to_messina": {
                "journey_time": "40 minutes",
                "price": "€5-6",
                "frequency": "Every 60-90 minutes",
                "type": "Regional trains"
            },
            "to_catania": {
                "journey_time": "50 minutes",
                "price": "€4-5",
                "frequency": "Every 60-90 minutes",
                "type": "Regional trains"
            },
            "to_syracuse": {
                "journey_time": "90 minutes",
                "price": "€8-10",
                "connection": "Via Catania"
            },
            "to_palermo": {
                "journey_time": "4 hours",
                "price": "€15-20",
                "connection": "Via Messina",
                "type": "Regional + Intercity"
            }
        },
        "booking": "www.trenitalia.com or at station",
        "tip": "Book in advance for cheaper fares"
    },
    "airport_transfers": {
        "catania_airport": {
            "distance": "50 km",
            "journey_time": "45-60 minutes",
            "options": {
                "private_transfer": {
                    "price": "€80-100",
                    "booking": "Via Cohen House or online",
                    "advantages": "Door-to-door, comfortable, flexible"
                },
                "taxi": {
                    "price": "€70-90",
                    "booking": "At airport taxi stand",
                    "note": "Fixed price from airport"
                },
                "bus": {
                    "price": "€8-10",
                    "company": "Etna Trasporti",
                    "frequency": "8-10 times daily",
                    "journey_time": "90 minutes",
                    "note": "Must connect in Taormina center"
                },
                "rental_car": {
                    "price": "€30-50/day",
                    "companies": "Europcar, Hertz, Avis at airport",
                    "parking": "Free parking near Cohen House"
                }
            }
        }
    },
    "local_transport": {
        "taxi": {
            "availability": "Call or hail on street",
            "typical_fares": {
                "to_taormina_center": "€15-20",
                "to_train_station": "€15-20",
                "to_giardini_naxos": "€15-20"
            },
            "phone": "+39 0942 51150 (Radio Taxi Taormina)"
        },
        "car_rental": {
            "recommended": "Yes, for exploring Sicily",
            "companies": "Available in Taormina and airports",
            "parking_cohen_house": "Free street parking nearby",
            "traffic_zones": "Limited traffic zones (ZTL) in Taormina center"
        },
        "scooter_rental": {
            "availability": "Available in Taormina",
            "price": "€30-50/day",
            "license": "Valid driving license required"
        }
    }
}

# ═════════════════════════════════════════════════════════════════
# HOUSE RULES & POLICIES
# ═════════════════════════════════════════════════════════════════
HOUSE_RULES = {
    "check_in_out": {
        "check_in": "15:00 onwards - flexible with EKEY digital access system",
        "check_out": "10:00 standard",
        "late_check_out_policy": "FREE if approved by concierge - depends on next-day reservations",
        "late_check_out_process": "Contact concierge → Check availability → Concierge calls cleaning company → Approval",
        "ekey_system": "Personal digital access code (no physical keys) - 24/7 entry",
        "key_delivery": "EKEY code sent via email/WhatsApp 1-2 days before arrival",
        "late_check_in_fee": "NO FEE - EKEY allows arrival anytime, day or night",
        "late_check_out_fee": "NO FEE - but MUST get concierge approval in advance"
    },
    "quiet_hours": {
        "evening": "23:00-08:00",
        "note": "Please respect neighbors, residential building"
    },
    "smoking": {
        "policy": "No smoking inside apartments",
        "allowed": "Smoking permitted on balconies/terraces only"
    },
    "pets": {
        "policy": "Small pets allowed by prior arrangement",
        "fee": "€30 cleaning fee per stay",
        "conditions": "Must be well-behaved, not left alone"
    },
    "parties": {
        "policy": "No parties or events allowed",
        "note": "Quiet family/couple accommodation only"
    },
    "additional_guests": {
        "policy": "Only registered guests allowed",
        "fee": "€20/person/night for extra guests beyond booking"
    },
    "damage": {
        "policy": "Guests responsible for damages",
        "deposit": "Security deposit held until after inspection"
    }
}

# ═════════════════════════════════════════════════════════════════
# AMENITIES & SERVICES
# ═════════════════════════════════════════════════════════════════
AMENITIES = {
    "included": {
        "wifi": "Free high-speed WiFi in all apartments",
        "air_conditioning": "In all rooms",
        "heating": "Central heating in winter",
        "kitchen": "Fully equipped: oven, stove, fridge, dishwasher, microwave",
        "washing_machine": "In all apartments",
        "linens": "Bed linens and towels provided",
        "toiletries": "Basic toiletries provided",
        "smart_tv": "In living room",
        "iron": "Iron and ironing board available"
    },
    "optional_services": {
        "airport_transfer": "€80-100 from Catania airport",
        "grocery_delivery": "Pre-arrival grocery shopping (cost + €20 fee)",
        "baby_equipment": "Cot €20, high chair €15 per stay",
        "extra_cleaning": "€60 per cleaning during stay",
        "late_checkout": "FREE with concierge approval (must request in advance)",
        "early_checkin": "FREE if apartment ready (contact concierge to confirm)"
    },
    "nearby_services": {
        "pharmacy": "5 minutes walk",
        "doctor": "Medical center 10 minutes drive",
        "atm": "50 meters",
        "post_office": "Taormina center"
    }
}

# ═════════════════════════════════════════════════════════════════
# PRACTICAL INFORMATION
# ═════════════════════════════════════════════════════════════════
PRACTICAL_INFO = {
    "wifi": {
        "network_name": "Provided at check-in",
        "password": "Provided at check-in",
        "speed": "High-speed fiber connection"
    },
    "parking": {
        "type": "Free street parking",
        "location": "Near building (within 50m)",
        "availability": "Usually available, not guaranteed",
        "alternative": "Paid parking garage 200m away (€15/day)"
    },
    "accessibility": {
        "stairs": "Building has stairs, no elevator",
        "ground_floor": "No ground floor apartments",
        "note": "Not suitable for guests with severe mobility issues"
    },
    "emergency": {
        "emergency_number": "112 (EU emergency number)",
        "police": "113",
        "ambulance": "118",
        "fire": "115",
        "coast_guard": "1530"
    },
    "useful_apps": {
        "transport": "Moovit, Google Maps",
        "taxi": "Free Now, Uber (limited in Sicily)",
        "restaurants": "TheFork, TripAdvisor",
        "translation": "Google Translate"
    }
}

# ═════════════════════════════════════════════════════════════════
# WEATHER & BEST TIME TO VISIT
# ═════════════════════════════════════════════════════════════════
WEATHER = {
    "best_months": "May, June, September, October",
    "high_season": "July-August (very hot, crowded)",
    "shoulder_season": "April-May, September-October (ideal)",
    "low_season": "November-March (mild, some rain)",
    "sea_temperature": {
        "june_september": "22-26°C (comfortable swimming)",
        "may_october": "18-22°C (refreshing)"
    },
    "what_to_pack": {
        "summer": "Light clothing, sunscreen, hat, beach gear",
        "spring_fall": "Light layers, light jacket for evenings",
        "winter": "Warm jacket, umbrella"
    }
}

# ═════════════════════════════════════════════════════════════════
# MUSIC CONFIGURATION
# ═════════════════════════════════════════════════════════════════
MUSIC = {
    "dramatic_trigger": "Orchestra... turn silence into fire. One breath, one will - no mercy. FIRE!",
    "tracks": {
        "traditional": {
            "name": "Pizzica di San Vito",
            "spotify_id": "7MTyDl0UFVVJ1BLFQd8Er8",
            "description": "Traditional Salento tarantella rhythm",
            "origin": "Southern Italy folk music"
        },
        "political": {
            "name": "Deija na Marinno",
            "spotify_id": "205qFlGXIK5tcygiVYFMVS",
            "description": "Political consciousness music"
        },
        "love": {
            "name": "L'impero by Mannarino",
            "spotify_id": "5vV4umLhQqsuk6ei84nelx",
            "description": "Romantic Italian love song"
        },
        "fun": {
            "name": "Vogliamo le bambole",
            "spotify_id": "6yJuXrXneHttpJjzCWvnMG",
            "description": "Fun, upbeat, chaotic energy"
        }
    },
    "keywords": {
        "generic": ["musica", "music", "song", "canzone", "play", "suona", "metti", "ascoltare"],
        "traditional": ["tradizionale", "traditional", "pizzica", "tarantella", "salento", "folk"],
        "political": ["politica", "political", "marinno", "deija", "protest"],
        "love": ["amore", "love", "romantic", "romantica", "impero", "mannarino"],
        "fun": ["divertente", "fun", "funny", "allegra", "bambole", "vogliamo", "party"]
    },
    "prompts": {
        "it": "Che tipo di musica preferisci? Tradizionale, Divertente, Politica, o Romantica?",
        "en": "What kind of music? Traditional, Fun, Political, or Romantic?"
    }
}

# ═════════════════════════════════════════════════════════════════
# AI BEHAVIOR SETTINGS
# ═════════════════════════════════════════════════════════════════
BEHAVIOR = {
    "max_response_tokens": 80,
    "temperature": 0.7,
    "model": "gpt-4o-mini",
    "languages": ["it", "en"],
    "default_language": "it",
    "response_style": {
        "length": "1-3 sentences maximum",
        "tone": "Warm, professional, helpful",
        "forbidden_phrases": [
            "How can I assist you",
            "How may I help",
            "Is there anything else"
        ],
        "respond_only_when_asked": True,
        "no_autoplay": True,
        "one_voice_at_a_time": True
    }
}

# ═════════════════════════════════════════════════════════════════
# WHISPER SPEECH RECOGNITION
# ═════════════════════════════════════════════════════════════════
WHISPER = {
    "model": "whisper-1",
    "temperature": 0.0,
    "min_text_length": 4,
    "max_words": 15,
    "blocked_phrases": [
        "sottotitoli", "amara", "subscribe", "thank you for watching",
        "like and subscribe", "grazie per", "iscriviti", "community"
    ],
    "language_priority": ["it", "en"]
}

# ═════════════════════════════════════════════════════════════════
# TEXT-TO-SPEECH SETTINGS
# ═════════════════════════════════════════════════════════════════
TTS = {
    "provider": "elevenlabs",
    "cache_enabled": False,  # CRITICAL: No caching
    "voice_settings": {
        "it": "default",
        "en": "default"
    }
}

# ═════════════════════════════════════════════════════════════════
# SYSTEM PROMPTS (GENERATED FROM CONFIG)
# ═════════════════════════════════════════════════════════════════
def get_system_prompt(lang: str) -> str:
    """Generate system prompt from configuration"""
    
    if lang == "it":
        return f"""Sei {ASSISTANT['name']}, {ASSISTANT['role']}.
Rispondi SOLO in italiano. Massimo 1-3 frasi, sempre diretto e preciso.

APPARTAMENTI COHEN HOUSE:
- BOHO: 100m², 10 persone, €500/notte, terrazza vista Etna e mare
- VINTAGE: 90m², 8 persone, €450/notte, stile barocco, balcone Isola Bella
- SHABBY: 90m², 8 persone, €450/notte, shabby chic con colori pastello

POSIZIONE: Via Nazionale, 20 metri da Isola Bella
SUPERMERCATO: Piano terra Cohen House, di fronte Isola Bella
SPIAGGIA: Isola Bella a 20 metri (30 secondi a piedi)

CHECK-IN/OUT CON SISTEMA EKEY:
- Check-in: dalle 15:00, NESSUNA tassa per arrivo tardivo
- Sistema EKEY: codice digitale personale, entrata 24/7
- Check-out: ore 10:00 standard
- Check-out tardivo: GRATUITO se approvato (contatta concierge)
- Concierge controlla prenotazioni e coordina pulizie

TRASPORTI:
- Autobus Catania: dopo Hotel Panoramic, €5-7, 70 min
- Autobus Messina: ingresso Isola Bella, €4-6, 50 min
- Stazione treni: Taormina-Giardini, 3 km, taxi €15-20
- Aeroporto Catania: 50 km, transfer €80, taxi €70, bus €8

PRENOTAZIONE DIRETTA: Risparmia 20-25% su {COHEN_HOUSE['contact']['website']}
CONTATTO: {COHEN_HOUSE['contact']['email']} | WhatsApp {COHEN_HOUSE['contact']['whatsapp']}

NOME: "Mi chiamo {ASSISTANT['name']}, il concierge magico!"
MAI DIRE: "Come posso aiutarti" o "Posso fare altro"
"""
    
    else:  # English
        return f"""You are {ASSISTANT['name']}, {ASSISTANT['role']}.
Reply ONLY in English. Maximum 1-3 sentences, always direct and precise.

COHEN HOUSE APARTMENTS:
- BOHO: 100m², 10 guests, €500/night, terrace with Etna & sea view
- VINTAGE: 90m², 8 guests, €450/night, baroque style, Isola Bella balcony
- SHABBY: 90m², 8 guests, €450/night, shabby chic with pastels

LOCATION: Via Nazionale, 20 meters from Isola Bella
SUPERMARKET: Ground floor Cohen House, opposite Isola Bella
BEACH: Isola Bella 20 meters (30 seconds walk)

CHECK-IN/OUT WITH EKEY SYSTEM:
- Check-in: from 15:00, NO late arrival fee
- EKEY system: personal digital code, 24/7 entry
- Check-out: 10:00 standard
- Late check-out: FREE if approved (contact concierge)
- Concierge checks bookings and coordinates cleaning

TRANSPORT:
- Bus to Catania: after Hotel Panoramic, €5-7, 70 min
- Bus to Messina: Isola Bella entrance, €4-6, 50 min
- Train station: Taormina-Giardini, 3 km, taxi €15-20
- Catania airport: 50 km, transfer €80, taxi €70, bus €8

DIRECT BOOKING: Save 20-25% at {COHEN_HOUSE['contact']['website']}
CONTACT: {COHEN_HOUSE['contact']['email']} | WhatsApp {COHEN_HOUSE['contact']['whatsapp']}

NAME: "I'm {ASSISTANT['name']}, the magical bear concierge!"
NEVER SAY: "How can I assist" or "Anything else"
"""

# ═════════════════════════════════════════════════════════════════
# COMMON GUEST QUESTIONS & ANSWERS
# ═════════════════════════════════════════════════════════════════
FAQ = {
    "it": {
        "Dove si trova Cohen House?": "Via Nazionale, 20 metri da Isola Bella.",
        "C'è un supermercato vicino?": "Sì, al piano terra di Cohen House!",
        "Quanto costa?": "BOHO €500/notte, VINTAGE e SHABBY €450/notte. Risparmia 20% prenotando direttamente!",
        "Come arrivo dall'aeroporto?": "Transfer privato €80, taxi €70, o bus €8. Transfer prenotabile con noi.",
        "C'è parcheggio?": "Sì, parcheggio gratuito in strada vicino (circa 50m).",
        "C'è WiFi?": "Sì, WiFi gratuito ad alta velocità in tutti gli appartamenti.",
        "Accettate animali?": "Piccoli animali su richiesta, €30 pulizia.",
        "Posso fumare?": "No all'interno, sì su balcone/terrazza.",
        "C'è aria condizionata?": "Sì, in tutte le stanze.",
        "Dov'è la spiaggia?": "Isola Bella a 20 metri, 30 secondi a piedi!",
        "Come funziona il check-in?": "Sistema EKEY - ricevi codice digitale, entri quando vuoi, nessuna tassa per arrivo tardivo.",
        "Posso arrivare tardi?": "Sì! Sistema EKEY permette entrata 24/7, nessuna tassa.",
        "Posso fare check-out tardivo?": "Sì, GRATUITO se approvato. Contatta concierge per verificare disponibilità.",
        "C'è tassa per check-out tardivo?": "No tassa, ma devi chiedere approvazione al concierge."
    },
    "en": {
        "Where is Cohen House?": "Via Nazionale, 20 meters from Isola Bella.",
        "Is there a supermarket nearby?": "Yes, ground floor of Cohen House!",
        "How much does it cost?": "BOHO €500/night, VINTAGE & SHABBY €450/night. Save 20% booking direct!",
        "How do I get from the airport?": "Private transfer €80, taxi €70, or bus €8. We can arrange transfer.",
        "Is there parking?": "Yes, free street parking nearby (about 50m).",
        "Is there WiFi?": "Yes, free high-speed WiFi in all apartments.",
        "Do you accept pets?": "Small pets by request, €30 cleaning fee.",
        "Can I smoke?": "No inside, yes on balcony/terrace.",
        "Is there air conditioning?": "Yes, in all rooms.",
        "Where is the beach?": "Isola Bella 20 meters away, 30 seconds walk!",
        "How does check-in work?": "EKEY system - you receive digital code, enter anytime, no late arrival fee.",
        "Can I arrive late?": "Yes! EKEY system allows 24/7 entry, no fee.",
        "Can I have late check-out?": "Yes, FREE if approved. Contact concierge to check availability.",
        "Is there a late check-out fee?": "No fee, but you must get concierge approval."
    }
}

# ═════════════════════════════════════════════════════════════════
# END OF CONFIGURATION
# ═════════════════════════════════════════════════════════════════
