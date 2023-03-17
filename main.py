import openai
import os
from git import Repo

from pathlib import Path

PATH_TO_BLOG_REPO = Path(
    "/home/jarvis/openai_course/iamlearningdevops.github.io/.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"

PATH_TO_CONTENT.mkdir(parents=True, exist_ok=True)

def update_blog(commit_message="Update blog"):
    repo = Repo(PATH_TO_BLOG_REPO)
    repo.git.add(A=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()
    
with open(PATH_TO_BLOG/"index.html", "w") as f:
    f.write("<h1>Automated</h1>")
    
update_blog()

