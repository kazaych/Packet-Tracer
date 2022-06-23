import socket
import keyboard
import UDP_socket


    def uncut_buf(self, raw, cat):
        if raw[0:2] == cat:
            p_len = int(hex(int(raw[2:6], 16)), 16) * 2  # calc len of packet
            pck_cut = raw[0:p_len]
            if (len(raw) - len(pck_cut)) > 0:
                  return raw, 1
            else:
                 return pck_cut, 0
        else:
             return raw, 1

    def buffer_cut(self, raw, cat):  #
        pck_list = []
        while len(raw) > 0:
            pck_begin = raw.find(cat)
            pck_len = int(hex(int(raw[pck_begin + 2: pck_begin + 6], 16)), 16) * 2  # calc len of packet
             frame = raw[pck_begin:pck_len]
             pck_list.append(frame)
             raw = raw[pck_len:]  # cut frame from raw
        return pck_list


input_cat = str(hex(int(input())))[2:]
port = int(input())
raw_buf = ''  # buffering data if not one cat  packet in eth frame

data = UdpSocket(4001)
data.sock =
while True:
    raw_str_buf = str(data.hex())
    pck, flg = uncut_buf(raw_str_buf, cat_num)
    if flg == 1:  # if in uncut_buf not one cat packet ++ to raw buf
        raw_buf = raw_buf + pck
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
    if keyboard.is_pressed('q'):  # press q to stop socket
        print('q has pressed end of program')
        break
