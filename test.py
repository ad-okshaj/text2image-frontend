import subprocess

def run_remote_command(command, host):
    ssh_command = f"ssh {host} {command}"
    result = subprocess.run(ssh_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode("utf-8")

ls_command = "docker exec lightningsliver ls"
remote_host = "4nm19is120@gpu.nmamit.in"

print(run_remote_command(ls_command, remote_host))
