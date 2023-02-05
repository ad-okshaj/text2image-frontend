import paramiko

# create an SSH client
client = paramiko.SSHClient()

# automatically add the server's host key (this is insecure and not recommended in production)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server
client.connect('gpu.nmamit.in',port = 202, username='4nm19is120', password='27102022')

# execute a command on the server
stdin, stdout, stderr = client.exec_command('docker exec -it lightningsliver bin/bash')
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))
stdin4, stdout4, stderr4 = client.exec_command('ls')
print(stdout4.read().decode('utf-8'))
print(stderr4.read().decode('utf-8'))
stdin1, stdout1, stderr1 = client.exec_command('cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/')
print(stdout1.read().decode('utf-8'))
print(stderr1.read().decode('utf-8'))
stdin3, stdout3, stderr3 = client.exec_command('python3 generate_images_original.py --data_set=flowers --t_dim=100 --image_size=128 --data_set=flowers --z_dim=100 --n_classes=24 --caption_vector_length=4800 --batch_size=128  --checkpoints_dir=Data/training/TAC_128/checkpoints --images_per_caption=30 --data_dir=Data')

# print the output of the command
print(stderr3.read().decode('utf-8'))

# close the connection
client.close()