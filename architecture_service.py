import os
import json
import google.generativeai as genai
from models import ArchitectureResponse


# Load prompt
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "../prompts/architecture_prompt.txt")
with open(PROMPT_PATH, "r") as f:
    BASE_PROMPT = f.read()

def generate_architecture(description: str, api_key: str = None) -> ArchitectureResponse:
    """
    Generates system architecture using Google Gemini (or mock if no key).
    """
    if not api_key:
        api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        # Fallback Mock Response for demo purposes if no key provided
        print("Warning: No API Key provided. Returning mock response.")
        return ArchitectureResponse(
            frontend="React + Vite",
            backend="FastAPI",
            database="PostgreSQL",
            cache="Redis",
            queue="RabbitMQ",
            storage="AWS S3",
            auth="OAuth2 / JWT",
            deployment="Docker + AWS",
            explanation="[MOCK MODE] No API Key provided. Architecture chosen for standard scalable web setup. React for dynamic UI, FastAPI for high-performance async backend, and PostgreSQL for robust relational data."
        )

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-pro")
        
        full_prompt = BASE_PROMPT.replace("{{APP_DESCRIPTION}}", description)
        
        response = model.generate_content(full_prompt)
        text_response = response.text
        
        # Clean up potential markdown formatting from LLM (e.g. ```json ... ```)
        clean_text = text_response.strip()
        if clean_text.startswith("```json"):
            clean_text = clean_text[7:]
        if clean_text.endswith("```"):
            clean_text = clean_text[:-3]
        
        data = json.loads(clean_text)
        
        return ArchitectureResponse(**data)

    except Exception as e:
        print(f"Error generating architecture: {e}")
        # Return fallback on error
        return ArchitectureResponse(
            frontend="Error Generating",
            backend="Error",
            database="Error",
            cache="Error",
            queue="Error",
            storage="Error",
            auth="Error",
            deployment="Error",
            explanation=f"An error occurred while calling the AI model: {str(e)}"
        )
