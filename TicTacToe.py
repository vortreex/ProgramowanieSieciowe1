import Interface 
import Game
import pickle

[sockt, rola] = Interface.interface.start().serverSelect()
TicTacToe = Game.game.start()
TicTacToe.wyswietlPlansze()

if rola == Interface.Serwer:
	conn, addr = sockt.accept()
	while True:
		TicTacToe.wybierzPole(rola)
		conn.send(pickle.dumps(TicTacToe))
		TicTacToe = pickle.loads(conn.recv(Interface.Buffer)) 
		TicTacToe.wyswietlPlansze()
		TicTacToe.victoryConditionCheck()
		if TicTacToe.victoryFlagX or TicTacToe.victoryFlagO or TicTacToe.victoryFlagTie:
			conn.close()
			sockt.close()
			exit(0)
	##Server
elif rola == Interface.Klient:
	while True:
		TicTacToe = pickle.loads(sockt.recv(Interface.Buffer))
		TicTacToe.wyswietlPlansze()
		TicTacToe.victoryConditionCheck()
		TicTacToe.wybierzPole(rola)
		if TicTacToe.victoryFlagX or TicTacToe.victoryFlagO or TicTacToe.victoryFlagTie:
			sockt.close()
			exit(0)
		sockt.send(pickle.dumps(TicTacToe))

	##klient

