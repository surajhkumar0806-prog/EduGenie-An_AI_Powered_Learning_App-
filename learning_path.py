from google import genai
from gemini_helper import generate_with_retry


def generate_roadmap(client: genai.Client, prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "Please provide a topic or skill to generate a learning path."

    formatted_prompt = (
        "Create a comprehensive, step-by-step learning roadmap to master the following topic/skill.\n\n"
        "Formatting Instructions:\n"
        "- Break the roadmap down into clear chronological stages (e.g., Phase 1: Beginner, Phase 2: Intermediate, Phase 3: Advanced).\n"
        "- Include key topics, recommended project ideas, and estimated timelines for each phase.\n"
        "- Use bullet points and clear Markdown headers.\n\n"
        f"Topic/Skill:\n{prompt.strip()}"
    )
    try:
        return generate_with_retry(client, formatted_prompt)
    except Exception as e:
        raise RuntimeError(f"Learning path generation failed: {str(e)}")