import face_recognition
import numpy as np
import json
import os
from datetime import datetime
import base64
from PIL import Image
import io

class FaceRecognitionSystem:
    def __init__(self):
        self.known_faces_file = "data/known_faces.json"
        self.known_face_encodings = []
        self.known_face_names = []
        self.known_face_data = {}
        
        os.makedirs("data", exist_ok=True)
        self.load_known_faces()
        print(f"✅ Face Recognition ready ({len(self.known_face_names)} known faces)")
    
    def load_known_faces(self):
        if os.path.exists(self.known_faces_file):
            try:
                with open(self.known_faces_file, 'r') as f:
                    data = json.load(f)
                
                self.known_face_encodings = [np.array(enc) for enc in data.get('encodings', [])]
                self.known_face_names = data.get('names', [])
                self.known_face_data = data.get('data', {})
                
                print(f"📂 Loaded {len(self.known_face_names)} known faces")
            except Exception as e:
                print(f"⚠️ Error loading faces: {e}")
    
    def save_known_faces(self):
        try:
            data = {
                'encodings': [enc.tolist() for enc in self.known_face_encodings],
                'names': self.known_face_names,
                'data': self.known_face_data
            }
            
            with open(self.known_faces_file, 'w') as f:
                json.dump(data, f)
            
            print(f"💾 Saved {len(self.known_face_names)} faces")
        except Exception as e:
            print(f"❌ Error saving: {e}")
    
    def recognize_face_from_base64(self, image_base64):
        try:
            # Decode base64
            image_data = base64.b64decode(image_base64.split(',')[1] if ',' in image_base64 else image_base64)
            image = Image.open(io.BytesIO(image_data))
            frame = np.array(image.convert('RGB'))
            
            # Find faces
            face_locations = face_recognition.face_locations(frame)
            
            if not face_locations:
                return {'recognized': False, 'error': 'No face detected'}
            
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            
            if not face_encodings:
                return {'recognized': False, 'error': 'Could not encode face'}
            
            face_encoding = face_encodings[0]
            
            # Check known faces
            if len(self.known_face_encodings) > 0:
                matches = face_recognition.compare_faces(
                    self.known_face_encodings, 
                    face_encoding,
                    tolerance=0.6
                )
                
                face_distances = face_recognition.face_distance(
                    self.known_face_encodings, 
                    face_encoding
                )
                
                if True in matches:
                    best_match_index = np.argmin(face_distances)
                    
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        
                        if name not in self.known_face_data:
                            self.known_face_data[name] = {
                                'visit_count': 0,
                                'first_visit': datetime.now().isoformat()
                            }
                        
                        self.known_face_data[name]['visit_count'] += 1
                        self.known_face_data[name]['last_visit'] = datetime.now().isoformat()
                        self.save_known_faces()
                        
                        print(f"👤 Recognized: {name} (visit #{self.known_face_data[name]['visit_count']})")
                        
                        return {
                            'recognized': True,
                            'name': name,
                            'is_new': False,
                            'visit_count': self.known_face_data[name]['visit_count'],
                            'last_visit': self.known_face_data[name].get('last_visit')
                        }
            
            print(f"👤 New face detected")
            return {
                'recognized': False,
                'is_new': True,
                'encoding': face_encoding.tolist()
            }
            
        except Exception as e:
            print(f"❌ Face recognition error: {e}")
            return {'recognized': False, 'error': str(e)}
    
    def register_new_face(self, name, encoding):
        try:
            self.known_face_encodings.append(np.array(encoding))
            self.known_face_names.append(name)
            self.known_face_data[name] = {
                'visit_count': 1,
                'first_visit': datetime.now().isoformat(),
                'last_visit': datetime.now().isoformat()
            }
            
            self.save_known_faces()
            print(f"✅ Registered: {name}")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

face_system = FaceRecognitionSystem()
