from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import clientFromString
from twisted.internet import reactor
 
class EchoClientProtocol(Protocol):
    def connectionMade(self):
        self.transport.write('> To Server:Hello server')
    def dataReceived(self, data):
        print('> From Server:%s' % data)
        reactor.stop()
 
class EchoClientFactory(ClientFactory):
	protocol = EchoClientProtocol
 
if __name__ == '__main__':
	#construct 10 client endpoints
	for i in xrange(10):
		clientFromString(reactor,'tcp:192.168.90.192:9105')\
				.connect(
						EchoClientFactory()
						)
	reactor.run()
