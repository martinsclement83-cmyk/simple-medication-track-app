# text_processor.py


import re


class TextProcessor:
    """
    Cleans and validates medication input using regex.
    """

    @staticmethod
    def clean_text(text):
        """
        Removes unwanted characters and formats input properly.
        """

        if not text:
            return ""

        # Remove special characters except letters, spaces, and hyphens
        cleaned = re.sub(r"[^a-zA-Z\s\-]", "", text)

        # Normalize whitespace
        cleaned = re.sub(r"\s+", " ", cleaned).strip()

        return cleaned.lower()

    @staticmethod
    def validate_name(text):
        """
        Validates that input looks like a medication name.
        """

        if not text:
            return False

        # Must contain only letters, spaces, or hyphens
        pattern = r"^[a-zA-Z\s\-]{2,50}$"

        if re.match(pattern, text):
            return True

        return False