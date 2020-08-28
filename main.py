import socket
import time
import random
import decimal


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":

    ip = "10.0.0.201"
    port = 1337
    counter = 0
    while counter < 24:

        cal_value = counter * 0.5
        print("READ VALUE:{}".format(cal_value))

        # random_value = float(decimal.Decimal(random.randrange(0, 99)) / 100)
        random_value = cal_value * 0.10
        print("RANDOM VALUE:{}".format(random_value))

        actual_value = cal_value + random_value
        print("ACTUAL VALUE:{}".format(actual_value))

        sendvalue = "SENDCALVALUES=" + str(counter) + "," +  str(cal_value) + ","  + str(actual_value)

        print("Sending: " + sendvalue)
        client(ip, port, sendvalue)
        time.sleep(0.020)
        counter = counter + 1

    client(ip, port, "READCALVALUES=")
