import ast

def check_syntax(code):
    try:
        ast.parse(code)
        return "No syntax errors ✅"
    except Exception as e:
        return f"Syntax Error ❌: {str(e)}"