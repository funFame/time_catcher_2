import sys
import time
from datetime import timedelta, datetime

from conf import SLEEP_TIME
from conf_git import *
from conf_log import log
from run import run


def now(utc_offset=timedelta(hours=5, minutes=30)) -> datetime:  # default ist
    now_utc = datetime.utcnow()
    # utc_offset = datetime.timedelta(hours=5, minutes=30)
    now_ist = now_utc + utc_offset
    # print(f"UTC time: {now_utc}")
    # print(f"IST time: {now_ist}")
    return now_ist


def main():
    checkout_repo(REMOTE_URL)
    git_config(GIT_USER, GIT_EMAIL)

    remove_cmds = [
        ["rm", "-rf", ".github"],
        ["rm", "-rf", " requirements.txt"],
        ["rm", "-rf", "main.py"],
        ["git", "add", "."],
        ["git", "commit", "-m", "removed unnecessary files"]
    ]


    while True:
        t = time.time()
        now_ = now(timedelta(hours=5, minutes=30))

        with open("time.txt", 'w') as f1:
            f1.write(str(now_))

        commit_msg = f"time: {str(now_)}"

        commands = [
            ["git", "add", "time.txt"],
            ["git", "commit", "-m", commit_msg],
            ["git", "push"]
        ]

        for cmd in commands:
            res, err = run(cmd)

            if res:
                log.info(" ".join(cmd), res)

            if cmd[1] == "push":
                if "rejected" in err:
                    log.critical(err)
                    log.warning("existing blissfully")
                    sys.exit(0)
            if err:
                log.error(err)

        time.sleep(SLEEP_TIME)
        # print(f"commited  {commit_msg}")


if __name__ == "__main__":
    main()
