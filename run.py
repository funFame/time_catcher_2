import logging
import subprocess
from typing import Tuple


def run(cmd: list) -> Tuple[str, str]:
    res = subprocess.run(
        cmd,
        capture_output=False,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = res.stdout.decode('utf-8').strip()
    logging.debug(output)

    err = res.stderr.decode("utf-8").strip()
    if err != "":
        # raise Exception(" ".join(cmd),err)
        logging.error(err)

    return output, err
