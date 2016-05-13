import Pyro4
import argparse
import server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ns_address", help="name service address")
    args = parser.parse_args()

    Pyro4.Daemon.serveSimple(
        {server.CountingSticks(): "countingsticks"},
        ns=True, verbose=True, host=args.ns_address)

if __name__ == '__main__':
    main()
