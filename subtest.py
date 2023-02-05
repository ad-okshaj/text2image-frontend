import subprocess

def run_remote_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def main():
    # Connect to remote server
    run_remote_command("ssh 4nm19is120@gpu.nmamit.in")

    # # Start the Docker Container
    # run_remote_command("docker start my_container")

    # Run the Python Project
    run_remote_command("docker exec -it lightningsliver bin/bash; ls")

    # Close the connection
    run_remote_command("exit")

if __name__ == "__main__":
    main()