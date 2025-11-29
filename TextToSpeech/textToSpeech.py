# pip install pyttsx3
import pyttsx3

speaker = pyttsx3.init()
says = input("Enter your word to speak : ")
speaker.say(says)
speaker.runAndWait()