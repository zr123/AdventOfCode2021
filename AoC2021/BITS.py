from bitarray import bitarray, util


class BITS:

    def __init__(self, data):
        if type(data) is bitarray:
            self.data = data
        if type(data) is str:
            data = data.rstrip()
            self.data = util.hex2ba(data)

        self.version = util.ba2int(self.data[0:3])
        self.type_id = util.ba2int(self.data[3:6])
        self.payload = self.data[6:]

        self.sub_packets = []
        if self.type_id == 4:
            self.package_size = self.calculate_literal_package_size()
        else:
            self.length_type_id = self.payload[0]
            if self.length_type_id:
                self.sub_package_count = util.ba2int(self.payload[1:12])
                self.payload = self.payload[12:]
                i = 0
                while len(self.sub_packets) < self.sub_package_count:
                    sub_packet = BITS(self.payload[i:])
                    self.sub_packets.append(sub_packet)
                    i += sub_packet.package_size
                self.package_size = 7 + 11 + i
            else:
                self.package_length = util.ba2int(self.payload[1:16])
                self.payload = self.payload[16:]
                i = 0
                while i < self.package_length:
                    sub_packet = BITS(self.payload[i:])
                    self.sub_packets.append(sub_packet)
                    i += sub_packet.package_size
                self.package_size = 7 + 15 + self.package_length

    def get_value(self):
        # assumes the packet is type == 4
        i = 0
        value = bitarray()
        while self.payload[i]:
            value.extend(self.payload[i+1:i+5])
            i += 5
        value.extend(self.payload[i + 1:i + 5])
        return util.ba2int(value)

    def calculate_literal_package_size(self):
        # assumes the packet is type == 4
        size = 0
        while self.payload[size]:
            size += 5
        return size + 5 + 6

    def get_version_sum(self):
        version_sum = self.version
        for sub_packet in self.sub_packets:
            version_sum += sub_packet.get_version_sum()
        return version_sum
