
path = r"C:\Users\mdzak\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\ultralytics\utils\git.py"
code = """
from pathlib import Path

def get_git_dir():
    return None

def get_git_origin_url():
    return None

def get_git_branch():
    return None

def get_git_head_oid():
    return None
    
def check_git_status():
    pass

class GitRepo:
    def __init__(self, *args, **kwargs):
        pass
    def get_commit_info(self):
        return {}
"""
with open(path, "w", encoding="utf-8") as f:
    f.write(code)
print("Patched git.py")
