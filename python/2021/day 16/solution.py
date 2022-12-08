
def hexa_to_packet(hexa_string):
	char_map = {
		'0' : "0000",
		'1' : "0001",
		'2' : "0010",
		'3' : "0011",
		'4' : "0100",
		'5' : "0101",
		'6' : "0110",
		'7' : "0111",
		'8' : "1000",
		'9' : "1001",
		'A' : "1010",
		'B' : "1011",
		'C' : "1100",
		'D' : "1101",
		'E' : "1110",
		'F' : "1111"
	}
	packet = "".join([char_map[x] for x in hexa_string])
	return packet

class Packet:
	packets = []
	char_map = {
		'0' : "0000",
		'1' : "0001",
		'2' : "0010",
		'3' : "0011",
		'4' : "0100",
		'5' : "0101",
		'6' : "0110",
		'7' : "0111",
		'8' : "1000",
		'9' : "1001",
		'A' : "1010",
		'B' : "1011",
		'C' : "1100",
		'D' : "1101",
		'E' : "1110",
		'F' : "1111"
		}

	def __init__(self, packet):
		Packet.packets.append(self)
		self.packet_version = int(packet[:3],2)
		self.type_id = int(packet[3:6],2)
        self.packet = packet[6:]
        if self.isLiteral():
            self.parseLiteral();

        # operator
		else:
            self.parseOperator();
			if self.packet[6] == '1':
				self.sub_packets = self.get_subpackets_1()
			else:
				self.sub_packets = self.get_subpackets_0()

    def parseOperator(self):
        l_id = int(self.packet[0],2)
        if (l_id == 0):
            bit_len = int(self.packet[1:16], 2)
            subpacks = self.packet[16:16+bit_len]
        else:
            n_subpack = int(self.packet[1:12], 2)
            subpacks = self.packet[12:]

        parsePacket(subpacks)

    def parsePacket(subpacks):
        tp_id = int(subpacks[3:6],2)


    def parseLiteral(self):
        self.data = ""
        j = 0;
        for i in range(0, len(self.packet), 5):
            data = self.packet[i:i+5]
            if (data[0] == '0'):
                self.data += data[1:]
                j = i+5
                break
            self.data += data[1:]
        self.data = int(self.data, 2)
        return self.packet[j:]

	def isLiteral(self):
        return (self.type_id == 4);

	def parse(self):
		if self.isLiteral():
			res = self.packet_version
		else:
			res = self.parse_operator()
		return res

	@classmethod
	def getVersionNumberSum(cls):
		return sum([x.packet_version for x in cls.packets])

def get_subpackets_0(packet):
	packet = packet[7:]
	length = int(packet[:15],2)
	packet = packet[15:]
	sub_packets = []
	while(length != 0):
		if int(packet[3:6],2) == 4:
			i = 6
			for k in range(0, len(packet[i:]), 5):
				part = packet[i+k:i+k+5]
				i += 5
				if part[0] == '0':
					sub_packets.append(packet[:i])
					length -= i
					break
		else:
			l_id = packet[6]
			if l_id == '0':
				s = get_subpackets_0(packet)
			else:
				s = get_subpackets_1(packet)
			length -= len(s[0])
			sub_packets.extend(s)
	return sub_packets

def get_subpackets_1(packet):
	packet = packet[7:]
	n = int(packet[:11],2)
	packet = packet[11:]
	sub_packets = []
	while (n != 0):
		if int(packet[3:6],2) == 4:
			i = 6
			for k in range(0, len(packet[i:]), 5):
				if len(packet) >= 5:
					part = packet[i+k:i+k+5]
					i += 5
					if part[0] == '0':
						sub_packets.append(packet[:i])
						packet = packet[i]
						n -= 1
						break
		else:
			if packet[6] == '0':
				s = get_subpackets_0(packet)
			else:
				s = get_subpackets_1(packet)
			if s != []:
				n -= 1
	return sub_packets

def part1():
	res = 0
	inp = open("input.txt", 'r').readline().strip()
	packet = hexa_to_packet(inp)

	pkt = Packet()

	# res += int(packet[:3],2)
	# t_id = int(packet[3:6],2)
	# if t_id != 4:
	# 	l_id = packet[6]
	# 	if l_id == '0':
	# 		for sub_packet in get_subpackets_0(packet):
	# 			res += int(sub_packet[:3],2)
	# 	else:
	# 		for sub_packet in get_subpackets_1(packet):
	# 			res += int(sub_packet[:3],2)
	# return res

print(part1())
