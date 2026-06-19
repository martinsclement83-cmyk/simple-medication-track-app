# medication.py

import requests

class DrugNotFoundError(Exception):
    pass

class APIConnectionError(Exception):
    pass

class Medication:
    """
    Fetches medication information from the OpenFDA Drug Label API.
    """

    BASE_URL = "https://api.fda.gov/drug/label.json"

    def __init__(self, drug_name):
        self.drug_name = drug_name

    def fetch_info(self):
        """
        Retrieves medication details from OpenFDA.

        Returns:
            dict: usage, warnings, side effects, instructions
        """

        try:
            query = (
                f'{self.BASE_URL}?search=openfda.generic_name:"{self.drug_name}"'
                '&limit=1'
            )

            response = requests.get(query, timeout=10)
            data = response.json()

            # ❗ DRUG NOT FOUND CHECK
            if "results" not in data or not data["results"]:
                raise DrugNotFoundError("No information found for this drug")

            result = data["results"][0]

            return {
                "usage": self._extract_text(
                    result.get("indications_and_usage", [])
                ),
                "warnings": self._extract_text(
                    result.get("warnings", [])
                ),
                "side_effects": self._extract_text(
                    result.get("adverse_reactions", [])
                ),
                "instructions": self._extract_text(
                    result.get("dosage_and_administration", [])
                )
            }

        except requests.exceptions.RequestException:
            raise APIConnectionError("Network error. Please check your internet connection.")

    @staticmethod
    def _extract_text(field):
        """
        Converts FDA list fields into readable text.
        """

        if not field:
            return "Information not available."

        if isinstance(field, list):
            return " ".join(field)

        return str(field)