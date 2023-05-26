import subprocess
from typing import Tuple, Union

from conf_log import log


def run(cmd: Union[list, str], **kwargs) -> Tuple[str, str]:
    if type(cmd) == str:
        cmd = cmd.split(" ")
    res = subprocess.run(
        cmd,
        capture_output=False,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)

    output = res.stdout.decode('utf-8').strip()
    log.info(output)

    err = res.stderr.decode("utf-8").strip()
    if err != "":
        # raise Exception(" ".join(cmd),err)
        log.error(err)

    return output, err
