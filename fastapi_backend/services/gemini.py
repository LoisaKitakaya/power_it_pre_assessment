import os
import json
from typing import Dict
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash-001"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=GEMINI_API_KEY)


class ErrorResponse(BaseModel):
    """
    Pydantic model for error response
    """

    error: str
    status_code: int


# Service function to interact with Gemini AI


def get_gemini_response(query: str) -> Dict:
    """
    Sends query to Gemini AI and returns structured recipe response.
    """

    prompt = f"""
    You are a recipe and meal planning assistant. For the user query: "{query}",
    provide a structured recipe in JSON format with the following fields:
    - answer: A brief summary of the recipe (string)
    - details: An object containing:
      - recipe_name: Name of the recipe (string)
      - ingredients: List of ingredients (array of strings)
      - instructions: List of cooking steps (array of strings)
      - tips: Optional list of cooking tips (array of strings)
      - prep_time: Estimated preparation time (string)
    Ensure the response is concise, practical, and tailored to the query.
    """

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        if not response.text:
            return ErrorResponse(error="Empty response from Gemini AI", status_code=500)

        try:
            result = json.loads(response.text.strip("```json\n```"))

        except json.JSONDecodeError:
            return ErrorResponse(
                error="Invalid JSON response from Gemini AI", status_code=500
            )

        return result

    except Exception as e:
        return ErrorResponse(error=f"Gemini AI error: {str(e)}", status_code=500)
