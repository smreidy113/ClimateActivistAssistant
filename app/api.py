

# Load Gemini API key from environment variable
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CIVIC_API_KEY = os.getenv("CIVIC_API_KEY")
CIVIC_ADDRESS = os.getenv("CIVIC_ADDRESS")


def fetch_api_data(user_info):
    # Placeholder for web API call logic
    return {"message": "API data would be here", "user_info": user_info}

def get_representatives(address, api_key):
    """
    Connects to Google Civic Information API and returns representative info for a given address.
    Args:
        address (str): The address to look up.
        api_key (str): Your Google Civic API key.
    Returns:
        dict: The response from the Civic API or error message.
    """
    import requests
    url = "https://www.googleapis.com/civicinfo/v2/representatives"
    params = {
        "key": api_key,
        "address": address
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def call_gemini_api(prompt, api_key):
    """
    Connects to Google Gemini API and returns the model's response.
    Args:
        prompt (str): The input prompt for Gemini.
        api_key (str): Your Gemini API key.
    Returns:
        dict: The response from Gemini or error message.
    """
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
