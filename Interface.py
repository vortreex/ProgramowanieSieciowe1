import socket
Buffer=1024
Serwer='s'
Klient='k'


class interface(object):
	def __init__(self):
		self.selectCounter=0
		self.selectCounterLimit=2
		self.hostAndPort=('127.0.0.1', 5555)
		self.rola=''

	def serverSelect(self):
		print('Chcesz byc klientem czy serwerem (k/s)?')
		self.rola = raw_input()
		if self.rola=='k':
			print('Jestes klientem')
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
			s.connect(self.hostAndPort)		
			return s, self.rola
		elif self.rola=='s':
			print('Jestes serwerem')
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
			s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
			s.bind(self.hostAndPort)
			s.listen(5)
			return s, self.rola

		else:
			self.selectCounter+=1
			if self.selectCounter>self.selectCounterLimit:
				print('Za duzo nieudanych prob, wyjscie z programu')
				exit()		
			else:
				self.serverSelect()

	@staticmethod
	def start():
		return interface()

