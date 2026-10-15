from google import genai
from gemini_helper import generate_with_retry


def generate_quiz(client: genai.Client, prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "Please provide a valid topic or content to generate a quiz."

    formatted_prompt = (
        "Generate a 3-question multiple-choice quiz based on the following topic/text.\n\n"
        "Formatting Instructions:\n"
        "- Format each question clearly with options labeled (A, B, C, D).\n"
        "- At the very end, include an 'Answer Key' section with brief explanations for each correct answer.\n\n"
        f"Topic/Content:\n{prompt.strip()}"
    )
    try:
        return generate_with_retry(client, formatted_prompt)
    except Exception as e:
        raise RuntimeError(f"Quiz generation failed: {str(e)}")