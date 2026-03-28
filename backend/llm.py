

import google.generativeai as genai
from analyzer import check_syntax

# 🔑 API KEY
genai.configure(api_key="AIzaSyCO9CYCPiVhoZIbQNF5jKe093pzbhDI9uQ")

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