import logging
import time

from conf import SLEEP_TIME
from conf_git import *
from run import run


def main():
    checkout_repo(REMOTE_URL)
    git_config(GIT_USER, GIT_EMAIL)

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
            res, err = run(cmd)

            if res:
                logging.info(" ".join(cmd), res)

            if cmd[1] == "push":
                if "rejected" in err:
                    logging.critical(err)
                    logging.warning("restarting the repo")
                    return main()
            if err:
                logging.error(err)

        time.sleep(SLEEP_TIME)
        # print(f"commited  {commit_msg}")


if __name__ == "__main__":
    main()
