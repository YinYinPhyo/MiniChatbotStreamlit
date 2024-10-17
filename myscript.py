import os

# Get the OpenAI API key from environment
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("No API key found in environment variables")
else:
    print("API key found:", openai_api_key)
