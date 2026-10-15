from google import genai
from gemini_helper import generate_with_retry


def get_answer(client: genai.Client, prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "Please provide a valid question or prompt."

    formatted_prompt = (
        "Answer the following question clearly with detailed explanations "
        f"and practical examples:\n\n{prompt.strip()}"
    )
    try:
        return generate_with_retry(client, formatted_prompt)
    except Exception as e:
        raise RuntimeError(f"Q&A generation failed: {str(e)}")