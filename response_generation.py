import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def generate_response(user_input, entities, pos_tags):
    # Your response generation logic based on NLP analysis
    # Add more sophisticated logic based on user input, entities, and POS tags
    # You can use if-else statements or more advanced decision-making techniques

    if any(entity[1] == "PERSON" for entity in entities):
        ans = f"Hello {entities[0][0]}! How can I assist you today?"
        speak_response(ans)
        return ans


    if any(tag[1] == "VERB" for tag in pos_tags):
        ans = "It seems like you mentioned a verb. How can I help you with that action?"
        speak_response(ans)
        return ans
    
    if any(tag[0] == "exit" for tag in pos_tags):
        ans = "Goodbye daddy!"
        speak_response(ans)
        return ans

    ans = "I'm sorry, I didn't understand that."
    speak_response(ans)
    return ans

def speak_response(response):
    # Use the text-to-speech engine to speak the response
    engine.say(response)
    engine.runAndWait()