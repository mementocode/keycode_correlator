import socket
import bitstream
import time
import binascii

IN_UDP_PORT = 5001
out_udp_port = 5000
stream = bitstream.BitStream()
in_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
in_sock.bind(('127.0.0.1', IN_UDP_PORT))
out_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# out_sock.bind(('127.0.0.1', out_udp_port))

buf = []

access_code = [b'\x00', b'\x00', b'\x00', b'\x01',
               b'\x01', b'\x00', b'\x01', b'\x00',
               b'\x01', b'\x01', b'\x00', b'\x00',
               b'\x01', b'\x01', b'\x01', b'\x01',
               b'\x01', b'\x01', b'\x01', b'\x01',
               b'\x01', b'\x01', b'\x00', b'\x00',
               b'\x00', b'\x00', b'\x00', b'\x01',
               b'\x01', b'\x01', b'\x00', b'\x01']
while True:
    tstart = time.time()
    if len(buf) < len(access_code):
        nf_buf_data = in_sock.recv(1)
        buf.append(nf_buf_data)
        tcheck1 = time.time()
        # print(tcheck1 - tstart)
    elif len(buf) == len(access_code) and buf != access_code:
        buf.pop(0)
        f_buf_data = in_sock.recv(1)
        buf.append(f_buf_data)
        tcheck2 = time.time()
    elif buf == access_code:
        # print('locked')
        for i in range(508):
            out_data = []
            tloop1 = time.time()
            # print(tstart - tloop1)
            for i in range(8):
                stream.write(in_sock.recv(1))
                data = list(str(stream.read(8)))
                new_data = list(data[7])
                out_data.extend(new_data)
                if len(out_data) == 8:
                    bytetime = time.time()
                    transfer_data = ''.join(out_data)
                    transfer_data = str(hex(int(transfer_data, 2)))
                    transfer_data = transfer_data[2:]
                    if len(transfer_data) < 2:
                        transfer_data = transfer_data + '0'
                    transfer_data = str(binascii.unhexlify(transfer_data))
                    print(transfer_data[2])
                    printime = time.time()
                    print(printime - bytetime)
                    # print(hex(int(transfer_data,2)))
                    # import to file
                    # with open("recovered.txt", "a",) as f:
                    #    f.write(transfer_data.decode("utf-8") )

        buf = []
