# ai_translator.py
import os
import google.generativeai as genai
from dotenv import load_dotenv


class AITranslator:
    """
    Uses Gemini AI to simplify medical information into plain language.
    """

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def simplify_text(self, text):
        """
        Converts complex medical text into simple language.
        """

        try:
            if not text or text.strip() == "":
                return "No information available to simplify."

            prompt = f"""
            You are a medical assistant AI.

            Rewrite the following medical information in very simple, everyday English.
            Avoid medical jargon. Make it easy for a non-medical person to understand.

            Text:
            {text}
            """

            response = self.model.generate_content(prompt)

            return response.text.strip()

        except Exception as e:
            return f"AI simplification failed: {str(e)}"
