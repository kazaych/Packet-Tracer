import socket
import keyboard


def uncut_buf(raw, cat):  # take data from socket and check that only one asterix packet in eth frame
    if raw[0:2] == cat:
        p_len = int(hex(int(raw[2:6], 16)), 16) * 2  # calc len of packet
        pck_cut = raw[0:p_len]
        if (len(raw) - len(pck_cut)) > 0:
            return raw, 1
        else:
            return pck_cut, 0
    else:
        return raw, 1


def buffer_cut(raw, cat):  # take data from buffer only if It's not only one asterix frame in one eth frame
    pck_list = []
    while len(raw) > 0:
        pck_begin = raw.find(cat)
        pck_len = int(hex(int(raw[pck_begin + 2: pck_begin + 6], 16)), 16) * 2  # calc len of packet
        frame = raw[pck_begin:pck_len]
        pck_list.append(frame)
        raw = raw[pck_len:]  # cut frame from raw
    return pck_list


print('Input Asterix cat. num')
input_cat = str(hex(int(input())))
cat_num = input_cat[2:]
print('Input port UDP')
udp_port = int(input())


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', udp_port))  # open socket
raw_buf = ''  # buffering data if not one cat  packet in eth frame
while True:
    data = sock.recv(1515)
    raw_str_buf = str(data.hex())
    pck, flg = uncut_buf(raw_str_buf, cat_num)
    if flg == 1:  # if in uncut_buf not one cat packet ++ to raw buf
        raw_buf = raw_buf + pck  # add buffer
    else:
        if raw_buf != '':
            packets = buffer_cut(raw_buf, cat_num)
            if packets != 0:
                for packet in packets:
                    print('mapped from buffer', packet)
                    print(150 * '-')
            raw_buf = ''
        else:
            print('mapped', pck)
            print(150 * '-')
    if keyboard.is_pressed('q'): # press q to stop socket
        print('q has pressed end of program')
        break
