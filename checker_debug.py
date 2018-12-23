import bitstream
import socket
import time

IN_UDP_PORT = 5000
out_udp_port = 5000
stream = bitstream.BitStream()
in_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# in_sock.bind(('127.0.0.1', IN_UDP_PORT))
out_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# out_sock.bind(('127.0.0.1', out_udp_port))
host = '127.0.0.1'
port = 5001
addr = (host, port)
# i=0
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
    print('run')
    for i in range(len(access_code)):
        print(access_code[i])
        out_sock.sendto(access_code[i], addr)

# # print(i,buf)
# # i+=1
# if len(buf) < 32:
#     # print(len(access_code))
#     nf_buf_data = in_sock.recv(1)
#     buf.append(nf_buf_data)
#     # print(len(buf))
#     # print('buf is not full')
# elif len(buf) == 32 and buf != access_code:
#     buf.pop(0)
#     f_buf_data = in_sock.recv(1)
#     buf.append(f_buf_data)
#     # print('not match')
# elif buf == access_code:
#     print('match')
#     while True:
#         transfer_data = in_sock.recv(1)
#         out_sock.sendto(transfer_data, addr)
