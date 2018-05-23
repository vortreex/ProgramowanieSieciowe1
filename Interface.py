import socket
Buffer = 1024
Serwer = 's'
Klient = 'k'
Port = 5555

class interface(object):
	def __init__(self):
		self.selectCounter = 0
		self.selectCounterLimit = 2
		self.rola = ''

	def serverSelect(self):
		print('Chcesz byc klientem czy serwerem (k/s)?')
		self.rola = input()
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
		except socket.error as sockerr:
			print('Error occured: ' + str(sockerr))
			exit(0)

		if self.rola == 'k':
			print('Jestes klientem')
			s.settimeout(5)
			try:
				s.connect((input('Podaj adres IP serwera: '), Port))
			except socket.timeout as timeout:
				print('Error occured: ' + str(timeout))
				exit(0)
			except socket.gaierror as err:
				print('Error occured: ' + str(err))
				exit(0)

			return s, self.rola
		elif self.rola == 's':
			print('Jestes serwerem')
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			try:
				s.bind((str(socket.INADDR_ANY), Port))
			except socket.error as err:
				print('Error occured: ' + str(err))
				exit(0)
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

