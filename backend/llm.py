import os
import google.generativeai as genai
from backend.analyzer import check_syntax

# 🔐 SECURE API KEY (ENV VARIABLE SE)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_code(code):
    try:
        syntax_result = check_syntax(code)

        prompt = f"""
You are an expert code debugger.

Analyze this code:

{code}

Return STRICTLY in this format:

Bugs:
...

Fix:
...

Explanation:
...

Optimized Code:
...
"""

        response = model.generate_content(prompt)

        if not response.text:
            return "LLM returned empty response ❌"

        return f"{syntax_result}\n\n{response.text}"

    except Exception as e:
        return f"LLM Error ❌: {str(e)}"