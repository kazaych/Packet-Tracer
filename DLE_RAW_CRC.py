
class DLE_Packet:

    buff_data = []

    def __init__(self, DLE_start = '1002', DLE_end = '1003'):
        self.DLE_start = DLE_start
        self.DLE_end = DLE_end

    def is_self_packet(self, data):
        if data[:4] == self.DLE_start and data[-4:] == self.DLE_end:
            cut_data = data[4:-4]
            if self.buff_data != []:  # if buffer is not empty
                if data[:4] == self.DLE_start and data[-4:] == self.DLE_end:  # and if whole asterix packet in buffer
                    str_buffer = ''.join(self.buff_data)
                    cut_buffer = str_buffer[4:-4]
                    self.buff_data = []
                    return cut_data, cut_buffer
            return cut_data, None
        else:
            self.buffer(data)

    def buffer(self, data):
            self.buff_data.append(data)



