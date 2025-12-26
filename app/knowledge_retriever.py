import json
from pathlib import Path

class CohenHouseKnowledge:
    def __init__(self):
        knowledge_path = Path(__file__).parent / "cohen_house_knowledge.json"
        with open(knowledge_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    def get_location_info(self) -> str:
        loc = self.data['location']
        return f"""LOCATION:
- Address: {loc['address']}
- Mazzarò Beach: {loc['beach_mazzaro']}
- Isola Bella Beach: {loc['beach_isola_bella']}
- To Town Center: {loc['to_center_funicular']} or {loc['to_center_walking']}
- Supermarket: {loc['supermarket']}
"""
    
    def get_apartment_info(self, apt_name: str = None) -> str:
        apts = self.data['apartments']
        if apt_name and apt_name.lower() in apts:
            apt = apts[apt_name.lower()]
            return f"""{apt_name.upper()}: {apt['size_sqm']}m², {apt['guests_max']} guests, €{apt['price_per_night']}/night
Features: {', '.join(apt['features'])}"""
        else:
            return "\n".join([
                f"{name.upper()}: {apt['size_sqm']}m², {apt['guests_max']} guests, €{apt['price_per_night']}/night"
                for name, apt in apts.items()
            ])
    
    def get_transportation_info(self) -> str:
        trans = self.data['transportation']
        return f"""TRANSPORTATION:
From Airport: {trans['from_airport']['taxi']}
From Train: {trans['from_train_station']['taxi']}
In Taormina: {trans['in_taormina']['funicular']}
Walking to center: {trans['in_taormina']['walking']}
"""
    
    def get_beach_info(self) -> str:
        beaches = self.data['beaches']
        return f"""BEACHES:
Mazzarò: {beaches['mazzaro']['distance']} - {beaches['mazzaro']['type']}
Isola Bella: {beaches['isola_bella']['distance']} - {beaches['isola_bella']['type']}
"""
    
    def get_context_for_query(self, query: str) -> str:
        """Get relevant context based on query keywords"""
        query_lower = query.lower()
        context_parts = []
        
        # Always include basic location
        context_parts.append(self.get_location_info())
        
        # Check for specific topics
        if any(word in query_lower for word in ['beach', 'mare', 'spiaggia', 'mazzaro', 'mazzarò', 'isola', 'bella', 'isola bella']):
            context_parts.append(self.get_beach_info())
        
        if any(word in query_lower for word in ['apartment', 'appartamento', 'boho', 'vintage', 'shabby', 'price', 'prezzo', 'cost']):
            context_parts.append(self.get_apartment_info())
        
        if any(word in query_lower for word in ['come arrivare', 'how to get', 'transport', 'taxi', 'train', 'airport', 'centro', 'center', 'funivia', 'funicular']):
            context_parts.append(self.get_transportation_info())
        
        if any(word in query_lower for word in ['restaurant', 'ristorante', 'eat', 'mangiare', 'food', 'cibo']):
            restaurants = self.data['restaurants']
            context_parts.append(f"RESTAURANTS: {', '.join(restaurants['fine_dining'] + restaurants['casual'])}")
        
        return "\n".join(context_parts)

knowledge = CohenHouseKnowledge()
