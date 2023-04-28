import subprocess


def run(cmd: list):
    res = subprocess.run(cmd, capture_output=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                         )
    print(res.stdout.decode('utf-8'))

    err = res.stderr.decode("utf-8").strip()
    if err != "":
        # raise Exception(" ".join(cmd),err)
        print("ERR", err)