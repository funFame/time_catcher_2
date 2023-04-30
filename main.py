import math
import sys
import threading
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


def git_push():
    cmd = ["git", "push"]

    res, err = run(cmd)

    log.info(res)

    if "rejected" in err:
        log.critical(err)
        log.warning("existing blissfully")
        sys.exit(0)


def keep_pushing(interval=timedelta(minutes=1)):
    while True:
        git_push()
        time.sleep(interval.total_seconds())


def main():
    checkout_repo(REMOTE_URL)
    git_config(GIT_USER, GIT_EMAIL)

    NO_OF_COMMITS = float(os.getenv("NO_OF_COMMITS", math.inf))

    now_ = now(timedelta(hours=5, minutes=30))

    with open("time_catcher.log", 'a') as f1:
        f1.write(f"started time_catcher on {now_}")

    remove_cmds = [
        ["rm", "-rf", ".github"],
        ["rm", "-rf", "requirements.txt"],
        ["rm", "-rf", "main.py"],
        ["git", "add", "."],
        ["git", "commit", "-m", "removed unnecessary files"]
    ]

    print("cleaning unnecessary files")

    push_thread = threading.Thread(target=keep_pushing, args=(), daemon=True)
    push_thread.start()

    for cmd in remove_cmds:
        res, err = run(cmd)
        log.info(res)
        log.error(err)

    i = 0
    while True:
        i += 1

        now_ = now(timedelta(hours=5, minutes=30))

        with open("time.txt", 'w') as f1:
            f1.write(str(now_))

        commit_msg = f"time: {now_}"

        commands = [
            ["git", "add", "time.txt"],
            ["git", "commit", "-m", commit_msg],
        ]

        for cmd in commands:
            res, err = run(cmd)

            if res:
                log.info(" ".join(cmd), res)

            if err:
                log.error(err)

        if i == NO_OF_COMMITS:
            log.info(f"committed - {i} msgs. Thank you !")
            break

        time.sleep(SLEEP_TIME)
        # print(f"commited  {commit_msg}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.exception(e)
    finally:
        log.info("git pushing rest of the commits")
        git_push()
        log.info("pushed all th commits")
