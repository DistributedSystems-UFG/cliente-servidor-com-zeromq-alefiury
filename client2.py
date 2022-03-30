from pickle import dumps

import zmq

from constCS import *


def main() -> None:
    context = zmq.Context()
    s  = context.socket(zmq.REQ)

    p1 = "tcp://"+ HOST +":"+ PORT2
    s.connect(p1)

    # Inputs
    first_string = input("Input your first string: ")
    second_string = input("Input your second string: ")
    operation = input("Choose one of the following operations -> Concat, Equal, Distance: ")

    inputToServerRaw = (first_string, second_string, operation)
    inputToServer = dumps(inputToServerRaw)

    # Send some data
    s.send(inputToServer)
    # Receive the response
    data = s.recv(1024)
    # Print the results
    print('\n' + bytes.decode(data))


if __name__ == '__main__':
    main()