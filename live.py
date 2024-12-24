import asyncio
from google import genai
from google.genai.types import SpeechConfig, VoiceConfig, PrebuiltVoiceConfig
import pyaudio
import websockets

model_id = "gemini-2.0-flash-exp"
client = genai.Client(
    api_key="YOUR_API_KEY",
    http_options={"api_version": "v1alpha"},
)

config = {
    "response_modalities": ["TEXT"],
    "speechConfig": SpeechConfig(
       voiceConfig=VoiceConfig(
           prebuiltVoiceConfig=PrebuiltVoiceConfig()
           )
    )
}

async def chat_with_gemini():
 async with client.aio.live.connect(model=model_id, config=config) as session:
    while True:
        message = input("You: ")
        await session.send(message, end_of_turn=True);

        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=24000,
                        output=True
                        )
        
        async for response in session.receive():
            if response.server_content and response.server_content.model_turn:
               for part in response.server_content.model_turn.parts:
                  stream.write(part.inline_data.data)
                
      
            

if __name__ == "__main__":
    asyncio.run(chat_with_gemini())