import paramiko

# Create a new SSH client
ssh = paramiko.SSHClient()

# Automatically add the remote server's host key (for the first time only)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh.connect(
    hostname="gpu.nmamit.in",
    port=202,
    username="4nm19is120",
    password="27102022"
)

# Run the 'docker exec' command inside the container
stdin, stdout, stderr = ssh.exec_command(
    "docker exec lightningsliver ls"
)

# Print the output of the 'ls' command
print(stdout.read().decode("utf-8"))

# Close the SSH connection
ssh.close()
