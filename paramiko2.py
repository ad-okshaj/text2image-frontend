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

# # Run the "ls" command inside the Docker container
# stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver ls")
# print(stdout.read().decode())

# # Change to the "Repo" directory inside the Docker container and run "ls" again
# stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master && ls'")
# print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master/ && python3 generate_images_original.py --data_set=flowers --t_dim=100 --image_size=128 --data_set=flowers --z_dim=100 --n_classes=24 --caption_vector_length=4800 --batch_size=128  --checkpoints_dir=Data/training/TAC_128/checkpoints --images_per_caption=30 --data_dir=Data && cd Data && rm download.zip && zip -r download.zip images_generated_from_text/* && ls'")
print(stdout.read().decode())

sftp = ssh.open_sftp()
sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/download.zip', 'download.zip')
sftp.close()

# Close the SSH connection
ssh.close()

# Extracts zip file.
import shutil
shutil.unpack_archive('./download.zip')

