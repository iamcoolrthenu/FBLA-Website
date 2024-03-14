import google.generativeai as genai
import os  # for environment variables and OS system commands
import sys # for optional command-line args

def setup_model():
  # Set up the model with certain parameters
  generation_config = {
      "temperature": 0.9,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
  }
  
  safety_settings = [
      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
  ]
  
  return genai.GenerativeModel(
      model_name="gemini-1.0-pro",
      generation_config=generation_config,
      safety_settings=safety_settings,
  )

def configure_api_key():
  key_passed_as_arg = len(sys.argv) > 1
  # Set up the API key
  if key_passed_as_arg:
    api_key = sys.argv[1] # second argument is api_key (since first is script name)
  elif key := os.getenv("GEMINI_API_KEY") is not None:
    api_key = key
  elif key := os.getenv("API_KEY") is not None:
    api_key = key
  else:
    print("Environment Variable \"GEMINI_API_KEY\" or \"API_KEY\" not set, nor was the api key passed as an argument.")
    api_key = input("Enter API KEY:\n> ")
  
  return api_key