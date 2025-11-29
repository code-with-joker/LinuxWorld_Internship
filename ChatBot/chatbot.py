import google.generativeai as genai

# Enter your Gemini API key here
key = "ENTER-YOUR-GEMINI-API-KEY" 
genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-2.5-flash")

while True:
    user = input("Enter your message (type 'exit' to stop): ")

    if user.lower() == "exit":
        print("GOOD BYE !!")
        break

    response = model.generate_content(user)

    print("BOT:", response.text)
