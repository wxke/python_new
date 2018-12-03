
# -*- coding:UTF-8 -*-

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="127.0.0.1",port=22)
stdin , stdout ,stderr = ssh.exec_command("df")

result = stdout.read()

ssh.close()


