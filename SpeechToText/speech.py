import speech_recognition as sr
import pyttsx3

def listen_speech():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start Speaking...")
        audio = mic.listen(source)
        text = mic.recognize_google(audio)
        return text

def speak_text(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


print("-------- Voice to Voice Converter ----------")

while True:
    try:
        user_choice = input("\nPress ENTER to start speaking (or type 'exit' to quit): ")

        if user_choice.lower() == "exit":
            print("Goodbye!")
            break

        text = listen_speech()
        print("You said:", text)
        speak_text(text)
        print("Voice played successfully")

    except Exception as e:
        print("Error: Could not recognize your speech.")
        print("Reason:", e)
