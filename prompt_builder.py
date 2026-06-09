# The function to build the prompt
def build_prompt(user_input, tone, audience, format_type):
    return f"""
ROLE:
You are a professional AI writing assistant

TASK:
Write or generate content based on users request

USER INPUT:
{user_input}

REQUIREMENTS:
-Tone: {tone}
-Target audience:{audience}
Format:{format_type}

INSTRUCTIONS: 
-Make the contents clear, engaging and well structured
-Adapt language to suit the audience
-maintain the requested tone consistently
-output only final result(no explanations)

Generate content now:
"""
