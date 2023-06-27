from twisted.internet.protocol import Protocol,Factory
from twisted.internet import reactor
from twisted.internet.endpoints import serverFromString
 



LISTEN_PORT = 80
TRANSFER_HOST = '172.23.99.173'

transfer_client = None

class TcpClientFactory(ClientFactory):
	def startedConnecting(self, connector):
		print("Starting Connecting To Tcp Server", (connector.host, connector.port))

	def clientConnectionLost(self, connector, reason):
		print("Lost Connection from Tcp Server", (connector.host, connector.port), 'Reason:', reason)


	def clientConnectionFailed(self, connector, reason):
		print("Failed To Connect To Tcp Server", (connector.host, connector.port), 'Reason:', reason)


class TcpClient(Protocol):
	def connectionMade(self):
		addr = self.transport.addr  
		print("connected", self.transport.socket)
		client_ip = addr[0]
		transfer_client = self
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		str = "你好服务器，我是客户端 " + nowTime
		self.transport.write(str.encode("utf-8")) 

	def connectionLost(self, reason):
		addr = self.transport.addr  
		client_ip = addr[0]
		transfer_client = None 

	def dataReceived(self, tcp_data):
		addr = self.transport.addr 
		nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		try:
			msg = tcp_data.decode("utf-8")
			print("Received msg", msg, "from Tcp Server", addr)

			time.sleep(5)
			str = "来自客户端的响应 " + nowTime
			self.transport.write(str.encode("utf-8"))

		except BaseException as e:
			print("Comd Execute Error from", addr, "data:", tcp_data)
			str = "客户端发生异常 " + nowTime
			self.transport.write(str.encode("utf-8"))


class EchoServerProtocol(Protocol):
	def connectionMade(self):
		print('> New connection made,from client!')
		self.factory.conn = self.factory.conn + 1
		print('> Now conn=%d' % self.factory.conn)

		reactor.connectTCP(TRANSFER_HOST, LISTEN_PORT, TcpClientFactory())

 
	def dataReceived(self, data):
		print('> Data from client: %s'% data)
		self.transport.write(data)
 
		print('>Host: ',repr(self.transport.getHost()))
		print('>Peer: ',repr(self.transport.getPeer()))
		#Close connection with client
		self.transport.loseConnection()
		self.factory.conn = self.factory.conn - 1
	
class EchoServerFactory(Factory):
	protocol = EchoServerProtocol
	def __init__(self):
		self.conn = 0
 
if __name__ == '__main__':
	listen_str = 'tcp:%s' % LISTEN_PORT
	serverFromString(reactor, listen_str).\
			listen(
				EchoServerFactory()
					)
	reactor.run()
