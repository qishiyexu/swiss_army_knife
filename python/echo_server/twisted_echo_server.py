from twisted.internet.protocol import Protocol,Factory
from twisted.internet import reactor
from twisted.internet.endpoints import serverFromString
 
class EchoServerProtocol(Protocol):
	def connectionMade(self):
		print('> New connection made,from client!')
		self.factory.conn = self.factory.conn + 1
		print('> Now conn=%d' % self.factory.conn)
 
	def dataReceived(self, data):
	#	print('> Data from client: %s'% data)
		self.transport.write(data)
 
#		print('>Host: ',repr(self.transport.getHost()))
#		print('>Peer: ',repr(self.transport.getPeer()))
		#Close connection with client
	#	self.transport.loseConnection()
	#	self.factory.conn = self.factory.conn - 1
	
class EchoServerFactory(Factory):
	protocol = EchoServerProtocol
	def __init__(self):
		self.conn = 0
 
if __name__ == '__main__':
	print('> Listening on 8888...')
	serverFromString(reactor,'tcp:8888').\
			listen(
				EchoServerFactory()
					)
	reactor.run()
