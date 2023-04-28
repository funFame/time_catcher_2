import os
import time
import subprocess

from conf_git import *
from run import run
from conf import SLEEP_TIME

checkout_repo(REMOTE_URL)
git_config(GIT_USER,GIT_EMAIL)

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

    time.sleep(SLEEP_TIME)
