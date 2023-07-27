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
import AI
import facial_recognition

def makeup_bot():
    triggered = True
    if triggered == True:
        face = facial_recognition.detect_face()
        skin_type = AI.analyze_skin_type(face)
      # Makeup Bot Code
import AI
import facial_recognition

def makeup_bot():
    #Get facial recognition of person
    face_data = facial_recognition.get_data()

    #Use AI to analyze face data
    skin_type = AI.analyze(face_data)

    #Show person how to use makeup based on skin type
    makeup_tutorials = AI.generate_tutorials(skin_type)
