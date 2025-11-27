import google.generativeai as genai

# Enter your Gemini API key here
key = "ENTER-YOUR-GEMINI-API-KEY"
genai.configure(api_key=key)

# Load the model
model = genai.GenerativeModel("gemini-2.5-flash")

while True:
    user = input("Enter your message (type 'exit' to close): ")

    if user.lower() == "exit":
        print("GOOD BYE !!")
        break

    # Send user input to Gemini
    response = model.generate_content(user)

    # Print the bot reply
    print("BOT:", response.text)
