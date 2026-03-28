import subprocess
import tempfile
import os

# 🐍 PYTHON
def run_python_code(code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(code.encode())
            path = f.name

        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True,
            timeout=5
        )

        os.remove(path)

        return {"output": result.stdout, "error": result.stderr}

    except Exception as e:
        return {"error": str(e)}


# 💻 C++
def run_cpp_code(code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp") as f:
            f.write(code.encode())
            cpp_path = f.name

        exe_path = cpp_path.replace(".cpp", ".exe")

        compile = subprocess.run(
            ["g++", cpp_path, "-o", exe_path],
            capture_output=True,
            text=True
        )

        if compile.returncode != 0:
            return {"error": compile.stderr}

        run = subprocess.run(
            [exe_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        os.remove(cpp_path)
        os.remove(exe_path)

        return {"output": run.stdout, "error": run.stderr}

    except Exception as e:
        return {"error": str(e)}


# ☕ JAVA
def run_java_code(code):
    try:
        filename = "Main.java"

        with open(filename, "w") as f:
            f.write(code)

        compile = subprocess.run(
            ["javac", filename],
            capture_output=True,
            text=True
        )

        if compile.returncode != 0:
            return {"error": compile.stderr}

        run = subprocess.run(
            ["java", "Main"],
            capture_output=True,
            text=True,
            timeout=5
        )

        os.remove("Main.java")
        os.remove("Main.class")

        return {"output": run.stdout, "error": run.stderr}

    except Exception as e:
        return {"error": str(e)}


# 🌐 JAVASCRIPT
def run_js_code(code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".js") as f:
            f.write(code.encode())
            path = f.name

        result = subprocess.run(
            ["node", path],
            capture_output=True,
            text=True,
            timeout=5
        )

        os.remove(path)

        return {"output": result.stdout, "error": result.stderr}

    except Exception as e:
        return {"error": str(e)}


# 🔥 MAIN CONTROLLER
def run_code(code, language):
    if language == "Python":
        return run_python_code(code)

    elif language == "C++":
        return run_cpp_code(code)

    elif language == "Java":
        return run_java_code(code)

    elif language == "JavaScript":
        return run_js_code(code)

    else:
        return {"error": f"{language} not supported"}