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
		if TicTacToe.victoryFlagX or TicTacToe.victoryFlagO or TicTacToe.victoryFlagTie:
			TicTacToe.victoryConditionCheck()
			conn.close()
			sockt.close()
			exit(0)

elif rola == Interface.Klient:
	while True:
		TicTacToe = pickle.loads(sockt.recv(Interface.Buffer))
		TicTacToe.wyswietlPlansze()
		if TicTacToe.victoryFlagX or TicTacToe.victoryFlagO or TicTacToe.victoryFlagTie:
			TicTacToe.victoryConditionCheck()
			sockt.close()
			exit(0)
		TicTacToe.wybierzPole(rola)
		sockt.send(pickle.dumps(TicTacToe))
