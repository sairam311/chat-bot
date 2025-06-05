import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client with the API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_llama(user_input):
    """Function to interact with Llama-3.3-70B-Versatile via Groq's API."""
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Updated to Llama-3.3-70B-Versatile
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Llama-3.3-70B-Versatile, optimized for conversation, tool use, and reasoning."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}. Check your API key, model availability, or rate limits at console.groq.com."

def start_chatbot():
    """Function to start the chatbot interface."""
    print("👋 Welcome to Sassy.ai Chatbot (via Groq API)! Type 'exit' to end the chat.")
    print("Ask anything, and I'll respond with insights from Llama-3.3-70B.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Sassy.ai: Goodbye! Thanks for chatting! 👋")
            break
        if not user_input.strip():
            print("Sassy.ai: Please enter a message.")
            continue
        response = chat_with_llama(user_input)
        print(f"Sassy.ai: {response}\n")

if __name__ == "__main__":
    # Check if API key is set
    api_key = os.getenv("GROQ_API_KEY")
    #print(f"API Key: {api_key[:5] if api_key else 'None'}... (partially hidden for security)")  # Debug: Show first 5 chars
    if not api_key:
        print("Error: GROQ_API_KEY not found. Please set it in the .env file.")
    else:
        start_chatbot()