from pickle import loads

import zmq

from constCS import *
from utils import levenshtein


def main() -> None:
    context = zmq.Context()
    s  = context.socket(zmq.REP)    # create reply socket

    p1 = f"tcp://{HOST}:{PORT1}" # how and where to connect
    p2 = f"tcp://{HOST}:{PORT2}" # how and where to connect
    s.bind(p1)                      # bind socket to address
    s.bind(p2)                      # bind socket to address

    while True:
        # Receive data from client
        data = s.recv(1024)

        inputData = loads(data)
        firstString, secondString, operation = inputData

        # Operations
        if operation == 'Concat':
            response = "Concatenated strings: " + firstString+secondString
        elif operation == 'Distance':
            response = "Levenshtein Distance: " + str(levenshtein(firstString, secondString))
        elif operation == 'Equal':
            if firstString==secondString:
                response = "Strings are equal"
            else:
                response = "Strings are not equal"

        else:
            response = "Operation does not exist"

        # Stop if client stopped
        if not data: break
        s.send(str.encode(response))


if __name__ == '__main__':
    main()