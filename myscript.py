# import openai
# from dotenv import load_dotenv
# import os

# # Load the .env file
# load_dotenv()

# # Get the API key from the environment variable
# openai.api_key = os.getenv('OPENAI_API_KEY')

# # Test API call
# try:
#     # Simple test query
#     response = openai.ChatCompletion.create(
#       engine="text-davinci-003",  # Choose the model you want to test
#       prompt="Say hello in a friendly way",
#       max_tokens=10
#     )
#     print(response.choices[0].text.strip())  # Print the model's response

# except Exception as e:
#     print(f"An error occurred: {e}")

# import os
# import openai
# # reading variables from .env file, namely API_KEY and ORG_ID.
# with open("myenv/.env") as env:
#     for line in env:
#         key, value = line.strip().split("=")
#         os.environ[key] = value

# # Initialize API key and organization id
# openai.api_key = os.environ.get("API_KEY")
# # openai.organization = os.environ.get("ORG_ID")
# # Calling the API to list models
# models = openai.models.list()
# print(models)

import os

# Get the OpenAI API key from environment
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("No API key found in environment variables")
else:
    print("API key found:", openai_api_key)
