from git import Repo
import os

def clone_repo(repo_url):
    path = "temp_repo"

    if os.path.exists(path):
        return path

    Repo.clone_from(repo_url, path)
    return path


def read_files(repo_path):
    code_data = ""

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        code_data += f.read() + "\n\n"
                except:
                    pass

    return code_data