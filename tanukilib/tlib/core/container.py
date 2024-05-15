from tlib.core.core import exec_cmd
import os
from pathlib import Path


def is_docker_container_running(name: str) -> bool:
    """Check whether the specified docker container is up and running"""

    ret_code, stdout, _ = exec_cmd(
        ['docker', 'ps', '--format', '"{{.Names}}"'])
    if ret_code != 0:
        raise Exception("docker ps command failed")
    stdout = stdout.replace("\"", "")
    for container_name in stdout.splitlines():
        if name == container_name:
            return True
    return False


def list_running_docker_containers() -> list[str]:
    """List all running docker containers"""

    ret_code, stdout, _ = exec_cmd(
        ['docker', 'ps', '--format', '"{{.Names}}"'])
    if ret_code != 0:
        raise Exception("docker ps command failed")
    stdout = stdout.replace("\"", "")
    return stdout.splitlines()


def list_all_docker_containers() -> list[str]:
    """List all docker containers including stopped ones"""

    ret_code, stdout, _ = exec_cmd(
        ['docker', 'ps', '-a', '--format', '"{{.Names}}"'])
    if ret_code != 0:
        raise Exception("docker ps -a command failed")
    stdout = stdout.replace("\"", "")
    return stdout.splitlines()


def run_container(name: str) -> bool:
    """Run specified container"""

    home_dir = os.environ["TANULIB_HOME"]
    script = str(Path(home_dir).joinpath("scripts", f"{name}_start.bash"))
    ret_code, _, _ = exec_cmd(script)
    return ret_code == 0


def stop_container(name: str) -> bool:
    """Stop specified container"""

    home_dir = os.environ["TANULIB_HOME"]
    script = str(Path(home_dir).joinpath("scripts", f"{name}_stop.bash"))
    ret_code, _, _ = exec_cmd(script)
    return ret_code == 0
