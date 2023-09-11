import AI
import facial_recognition

def makeup_bot():
    triggered = True
    if triggered:
        face = facial_recognition.detect_face()
        skin_type = AI.analyze_skin_type(face)
      # Makeup Bot Code
import AI
import facial_recognition

def makeup_bot():
    #Get facial recognition of person
    face_data = facial_recognition.get_data()
    face_shape = facial_recognition.get_data
    #Use AI to analyze face data
    skin_tone = AI.analyze(face_data)

    #Show person how to use makeup based on skin tone and facial shape.
    makeup_tutorials = AI.generate_tutorials(skin_tone)
