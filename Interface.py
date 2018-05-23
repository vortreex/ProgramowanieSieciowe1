import socket
import Error
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
			Error.errorPrint(sockerr)

		if self.rola == 'k':
			print('Jestes klientem')
			try:
				s.settimeout(5)
			except socket.error as sckt:
				Error.errorPrint(sckt)
			try:
				s.connect((input('Podaj adres IP serwera: '), Port))
			except socket.timeout as timeout:
				Error.errorPrint(timeout)
			except socket.gaierror as gerr:
				Error.errorPrint(gerr)
			except socket.error as err:
				Error.errorPrint(err)
			try:
				s.settimeout(None)
			except socket.error as sckt:
				Error.errorPrint(sckt)
			return s, self.rola

		elif self.rola == 's':
			print('Jestes serwerem')
			try:
				s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			except socket.error as socketOpt:
				Error.errorPrint(socketOpt)
			try:
				s.bind((str(socket.INADDR_ANY), Port))
			except socket.error as err:
				Error.errorPrint(err)
			try:
				s.listen(5)
			except socket.error as listen:
				Error.errorPrint(listen)
			return s, self.rola

		else:
			self.selectCounter += 1
			if self.selectCounter > self.selectCounterLimit:
				print('Za duzo nieudanych prob, wyjscie z programu')
				exit()		
			else:
				self.serverSelect()

	@staticmethod
	def start():
		return interface()

