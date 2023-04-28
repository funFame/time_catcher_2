import os
import time
import subprocess

from run import run

gitPass = os.environ["GIT_PASS"]
userName = os.environ.get("GIT_USERNAME", "pythoneerHiro")

email = os.environ.get("GIT_EMAIL", "pythoneerHiro@gmail.com")

remote_url = f"https://{userName}:{gitPass}@github.com/pythoneerHiro/__time-catcher.git"

name = "Hiro"

run(["git", "clone", remote_url, "repo"])

os.chdir("repo")

run(["git", "config", "user.name", name])
run(["git", "config", "user.email", email])

sleepTime = os.getenv("SLEEP_TIME", 0.000001)
sleepTime = float(sleepTime)

while True:
    t = time.time()
    with open("time.txt", 'w') as f1:
        f1.write(str(t))

    commit_msg = f"time: {t}"

    commands = [
        ["git", "add", "time.txt"],
        ["git", "commit", "-m", commit_msg],
        ["git", "push"]
    ]

    for cmd in commands:
        run(cmd)

    # print(f"commited  {commit_msg}")

    time.sleep(sleepTime)
