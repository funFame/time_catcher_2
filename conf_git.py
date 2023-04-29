import os

from conf_log import log
from run import run

GIT_PASS: str = os.environ["GIT_PASS"].strip()

REPO: str = os.environ.get("GIT_REPO", "__time-catcher").strip()

GIT_USER: str = os.environ.get("GIT_USER", "Hiro").strip()
GIT_USERNAME: str = os.environ.get("GIT_USERNAME", "pythoneerHiro").strip()  # u can set what ever u want
GIT_EMAIL: str = os.environ.get("GIT_EMAIL", "pythoneerHiro@gmail.com").strip()

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

    res, err = run(["git", "clone", remote_url, temp_repo])

    log.info(res)

    if err:
        log.error(err)

        if "fatal" in err:
            log.critical(err)
            raise FileNotFoundError(f"remote url doesn't exist")

    os.chdir(temp_repo)

# git_config(name, email)
