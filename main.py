from google import genai 

client = genai.Client(
    api_key="YOUR_API_KEY"
)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents="Is Gemini 2.0 flash Experiences???"
)

print(response.text)

