def open_text():
        pass
        #################################
        #  if (os.path.exists(r".\\text.txt") != True):
        #         import paramiko
        #         ssh = paramiko.SSHClient()
        #         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #         ssh.connect(
        #         hostname="gpu.nmamit.in",
        #         port=202,
        #         username="4nm19is120",
        #         password="27102022"
        #         )
        #         sftp = ssh.open_sftp()
        #         sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/text.txt', 'text.txt')
        #         sftp.close()
        #         ssh.close()
        #         text_file = open("text.txt", "r")
        #         content = text_file.read()
        #         Input.insert(END, content)
        #         text_file.close()
        # elif (os.path.exists(r".\\text.txt") == True):
        #         text_file = open("text.txt", "r")
        #         content = text_file.read()
        #         Input.insert(END, content)
        #         text_file.close()
        # else:
        #         print('Something\'s wrong. I can feel it.')
        #################################