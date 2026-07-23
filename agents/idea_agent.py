from agents.base_agent import run_agent

from config import FAST_MODEL

from utils.prompts import IDEA_ANALYZER_PROMPT


def idea_analyzer_agent(startup_idea):

    return run_agent(

        system_prompt=IDEA_ANALYZER_PROMPT,

        user_input=startup_idea,

        model=FAST_MODEL,

        temperature=0.2,

        max_tokens=700

    )