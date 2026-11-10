import re


def clean_text(text):
    """
    Resume text ko clean karta hai.
    """

    # Convert text to lowercase
    text = text.lower()

    # Replace unwanted characters with space
    text = re.sub(r'[^a-zA-Z0-9+#.\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()