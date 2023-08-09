import subprocess
from invoke import task


@task
def check_rosetta(c):
    """
    Check if Rosetta is enabled.
    If not, print an error message and exit.
    """
    try:
        result = subprocess.run(
            ["sysctl", "-n", "sysctl.proc_translated"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            print("Rosetta is enabled.")
        else:
            print("Rosetta is not enabled. Please enable Rosetta and try again.")
            exit(1)
    except subprocess.CalledProcessError:
        print("Rosetta is not enabled. Please enable Rosetta and try again.")
        exit(1)
