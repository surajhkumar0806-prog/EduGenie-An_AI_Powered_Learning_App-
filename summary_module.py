from google import genai
from gemini_helper import generate_with_retry


def summarize_text(client: genai.Client, prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "Please provide text to summarize."

    formatted_prompt = (
        "Summarize the following text clearly and concisely.\n\n"
        "Formatting Guidelines:\n"
        "- Provide a brief 1-2 sentence overview first.\n"
        "- List the key takeaways as bullet points.\n"
        "- Keep the language simple and easy to understand.\n\n"
        f"Text to Summarize:\n{prompt.strip()}"
    )
    try:
        return generate_with_retry(client, formatted_prompt)
    except Exception as e:
        raise RuntimeError(f"Summary generation failed: {str(e)}")