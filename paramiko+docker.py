import docker
import paramiko

# Connect to the remote host using SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('gpu.nmamit.in',port = 202, username='4nm19is120', password='27102022')

# Set up a transport channel over the SSH connection
transport = ssh.get_transport()
docker_port = 2375
channel = transport.open_channel("direct-tcpip", ("127.0.0.1", docker_port), ("gpu.nmamit.in", docker_port))

# Connect to the remote Docker API using the transport channel
client = docker.DockerClient(base_url='tcp://127.0.0.1:%d' % docker_port)

# Find the existing container you want to run the `ls` command in
container = client.containers.get("lightningsliver")

# Run the `ls` command in the existing container
result = container.exec_run("ls")

# Print the output of the `ls` command
print(result.output.decode("utf-8"))

# Close the transport channel
channel.close()

# Close the SSH connection
ssh.close()
