import subprocess
from typing import Tuple

from conf_log import log


def run(cmd: list) -> Tuple[str, str]:
    res = subprocess.run(
        cmd,
        capture_output=False,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = res.stdout.decode('utf-8').strip()
    log.debug(output)

    err = res.stderr.decode("utf-8").strip()
    if err != "":
        # raise Exception(" ".join(cmd),err)
        log.error(err)

    return output, err
