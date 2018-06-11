import Interface 
import Game
import pickle
import Error
import socket

[sockt, rola] = Interface.interface.start().serverSelect()
TicTacToe = Game.game.start()
TicTacToe.wyswietlPlansze()

if rola == Interface.Serwer:
	try:
		conn, addr = sockt.accept()
	except socket.error as accerr:
		Error.errorPrint(accerr)
	while True:
		TicTacToe.wybierzPole(rola)
		try:
			conn.send(pickle.dumps(TicTacToe))
		except socket.error as senderr:
			Error.errorPrint(senderr)
		try:
			TicTacToe = pickle.loads(conn.recv(Interface.Buffer))
		except socket.error as recerr:
			Error.errorPrint(recerr)
		except EOFError as eofe:
			exit()
		TicTacToe.wyswietlPlansze()
		if TicTacToe.victoryFlagX or TicTacToe.victoryFlagO or TicTacToe.victoryFlagTie:
			TicTacToe.victoryConditionCheck()
			try:
				conn.close()
			except socket.error as clserr:
				Error.errorPrint(clserr)
			try:
				sockt.close()
			except socket.error as scktscls:
				Error.errorPrint(scktscls)
			exit(0)

elif rola == Interface.Klient:
	while True:
		try:
			TicTacToe = pickle.loads(sockt.recv(Interface.Buffer))
		except socket.error as recerr:
			Error.errorPrint(recerr)
		except EOFError as eofe:
			Error.ignoreError()
		TicTacToe.wyswietlPlansze()
		if TicTacToe.victoryFlagX or TicTacToe.victoryFlagO or TicTacToe.victoryFlagTie:
			TicTacToe.victoryConditionCheck()
			try:
				sockt.close()
			except socket.error as scktcls:
				Error.errorPrint(scktcls)
			exit(0)
		TicTacToe.wybierzPole(rola)
		try:
			sockt.send(pickle.dumps(TicTacToe))
		except socket.error as senderr:
			Error.errorPrint(senderr)