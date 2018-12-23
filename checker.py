import socket
import bitstream

IN_UDP_PORT = 5001
out_udp_port = 5000
stream = bitstream.BitStream()
in_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
in_sock.bind(('127.0.0.1', IN_UDP_PORT))
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
    if len(buf) < 32:
        # print(len(access_code))
        nf_buf_data = in_sock.recv(1)
        buf.append(nf_buf_data)
        # continue
    elif len(buf) == 32 and buf != access_code:
        buf.pop(0)
        f_buf_data = in_sock.recv(1)
        buf.append(f_buf_data)
        # continue
    elif buf == access_code:
        print('locked')
        buf = []
        for i in range(480):
            out_data = []
            for i in range(8):
                stream.write(in_sock.recv(1))
                data = list(str(stream.read(8)))
                new_data = list(data[7])
                out_data.extend(new_data)
                if len(out_data) == 8:
                    transfer_data = ''.join(out_data)
                    print(hex(int(transfer_data,2)))
                    # import to file
                    #with open("recovered.txt", "a",) as f:
                    #    f.write(transfer_data.decode("utf-8") )
