import Pyro4

from classes import *

if __name__=='__main__':
    game = Game()
    daemon = Pyro4.Daemon(host="0.0.0.0", port=5150)
    Pyro4.Daemon.serveSimple(
        {game: "test.game"},
        ns=False,
        daemon=daemon,
    )


