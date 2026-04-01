from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm import analyze_code
from backend.executor import run_code
from github_analyzer import clone_repo, read_files

app = FastAPI()

class CodeRequest(BaseModel):
    code: str
    language: str = "Python"


@app.get("/")
def home():
    return {"message": "AI Code Debugger API Running 🚀"}


@app.post("/analyze")
def analyze(request: CodeRequest):
    try:
        result = analyze_code(request.code)
        return {"result": result}
    except Exception as e:
        return {"result": f"Backend Error ❌: {str(e)}"}


@app.post("/run")
def run(request: CodeRequest):
    try:
        result = run_code(request.code, request.language)
        return result
    except Exception as e:
        return {"error": str(e)}


@app.post("/analyze-repo")
def analyze_repo(repo_url: str):
    try:
        path = clone_repo(repo_url)
        code = read_files(path)

        result = analyze_code(code[:5000])
        return {"result": result}
    except Exception as e:
        return {"result": str(e)}