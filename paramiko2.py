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

# Run the "ls" command inside the Docker container
stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver ls")
print(stdout.read().decode())

# Change to the "folder1" directory inside the Docker container and run "ls" again
stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master && ls'")
print(stdout.read().decode())

# Close the SSH connection
ssh.close()