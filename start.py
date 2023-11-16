import speech_recognition as sr
from response_generation import generate_response
from text_analysis import analyze_text

def voice_assistant():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
    while True:
        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source, timeout=2)

        try:
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)

            # Analyze user input using spaCy
            entities, pos_tags = analyze_text(user_input)
            print("Entities:", entities)
            print("POS Tags:", pos_tags)

            # Your response generation logic based on NLP analysis
            response = generate_response(user_input, entities, pos_tags)
            print("Response:", response)

            # Check for the exit command
            if "exit" in user_input:
                print("Exiting the voice assistant.")
                break  # Exit the loop

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    voice_assistant()
