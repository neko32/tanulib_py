from tlib.core import exec_cmd

def is_localstack_running(container_name:str = "tlib_localstack") -> bool:
    result_code, stdout, _ = exec_cmd(['docker', 'ps'])
    if result_code != 0:
        raise Exception("docker ps command failed. Docker has not installed yet?")
    return container_name in stdout
