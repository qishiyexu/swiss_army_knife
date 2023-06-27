from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import clientFromString
from twisted.internet import reactor
import time
import random
import string

PAYLOAD_NUM = 10
CONNECT_STRING = 'tcp:172.23.119.14:8888'


def gen_strings():
    str = ''.join(random.choice(string.ascii_lowercase+'_'+'_') for _ in range(PAYLOAD_NUM))
    return str

 
class EchoClientProtocol(Protocol):
	def connectionMade(self):
		self.packet_num = 1
		self.make_packet()
	# 	print('current packet %s' % self.cur_packet)
		self.transport.write(self.cur_packet)
	def dataReceived(self, data):
   #     print('> From Server:%s' % data)
		if data == self.cur_packet:
			self.packet_num += 1
			self.make_packet()
			if self.packet_num % 1000 == 0:
				print('current packet %s' % self.cur_packet)
			self.transport.write(self.cur_packet)
		else:
			print('packet not equal! send: %s, recv: %s' %(self.cur_packet, data))

	#    reactor.stop()

	def make_packet(self):
		tmp_str = gen_strings()
		self.cur_packet = 'PACKET_NUM=%d.payload=%s' % (self.packet_num, tmp_str)
		self.cur_packet = bytes(self.cur_packet, encoding = "utf8")


 
class EchoClientFactory(ClientFactory):
	protocol = EchoClientProtocol
 
if __name__ == '__main__':
	#construct 10 client endpoints
	for i in range(10):
		clientFromString(reactor, CONNECT_STRING)\
				.connect(
						EchoClientFactory()
						)
	reactor.run()
