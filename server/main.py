import Pyro4
import server


def main():
    Pyro4.Daemon.serveSimple(
    {
        server.CountingSticks(): "countingsticks"
    },
    ns=True, verbose=True, host="192.168.1.111")

if __name__ == '__main__':
    main()