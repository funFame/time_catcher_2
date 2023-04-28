import os

from run import run

REPO: str = os.environ["GIT_REPO"]
GIT_PASS: str = os.environ["GIT_PASS"]

GIT_USER: str = os.environ.get("GIT_USER", "Hiro")
GIT_USERNAME: str = os.environ.get("GIT_USERNAME", "pythoneerHiro")  # u can set what ever u want
GIT_EMAIL: str = os.environ.get("GIT_EMAIL", "pythoneerHiro@gmail.com")

if len(REPO.split("/")) == 1:
    REPO = f"{GIT_USERNAME}/{REPO}"

REMOTE_URL: str = f"https://{GIT_USERNAME}:{GIT_PASS}@github.com/{REPO}.git"


def git_config(name: str, email: str):
    # allways execute after checkout
    if not os.path.exists(".git"):
        raise Exception("Not a git repository")


    run(["git", "config", "user.name", name])
    run(["git", "config", "user.email", email])


def checkout_repo(remote_url: str):
    temp_repo = "repo"
    if os.path.exists(temp_repo):
        raise FileExistsError(f"{temp_repo} exists")

    run(["git", "clone", remote_url, temp_repo])
    os.chdir(temp_repo)

# git_config(name, email)
