import os
import paramiko
import requests
import shutil
from replicate import Client


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
                hostname="gpu.nmamit.in",
                port=202,
                username="4nm19is120",
                password="27102022"
                )
stdin, stdout, stderr = ssh.exec_command(f"docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master/ && python3 connection.py --data_set=flowers --t_dim=100 --image_size=128 --data_set=flowers --z_dim=100 --n_classes=24 --caption_vector_length=4800 --batch_size=128  --checkpoints_dir=Data/training/TAC_128/checkpoints/ --images_per_caption=30 --data_dir=Data --text=a_red_flower && cd Data && zip -r download.zip images_generated_from_text/* && ls'")
print(stdout.read().decode())
sftp = ssh.open_sftp()
sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/download.zip', 'download.zip')
sftp.close()
ssh.close()