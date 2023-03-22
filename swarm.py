import socket 
import threading
import time

class Drone:
    def __init__(self, ip_address, port, local_port):
        self.ip_address = ip_address
        self.port = port
        self.local_port = local_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', local_port))
        
    def send(self, message, delay=3):
        try:
            self.sock.sendto(message.encode(), (self.ip_address, self.port))
            print(f"{self.ip_address}: Sending message - {message}")
        except Exception as e:
            print(f"{self.ip_address}: Error sending message - {str(e)}")
        time.sleep(delay)
        
    def receive(self):
        # Continuously loop and listen for incoming messages
        while True:
            # Try to receive the message otherwise print the exception
            try:
                response, ip_address = self.sock.recvfrom(128)
                print(f"{self.ip_address}: Received message - {response.decode(encoding='utf-8')}")
            except Exception as e:
                # If there's an error close the socket and break out of the loop
                self.sock.close()
                print(f"{self.ip_address}: Error receiving message - {str(e)}")
                break

    @staticmethod
    def send_swarm(drones, message, delay=0):
        threads = []
        for drone in drones:
            if drone is not None:
                t = threading.Thread(target=drone.send, args=(message, delay))
                threads.append(t)
                t.start()
        
        # wait for all threads to complete
        for t in threads:
            t.join()
    
    @staticmethod
    def close_connection(drones):
        for drone in drones:
            if drone is not None: 
                drone.sock.close()


# Send the message to Tello and allow for a delay in seconds
def sendSwarm(sockets, addresses, message, delay):
  # Try to send the message otherwise print the exception
    for socket,address in sockets,addresses :
        try:
            socket.sendto(message.encode(), address)
            print("Sending message: " + message)
        except Exception as e:
            print("Error sending: " + str(e))

    # Delay for a user-defined period of time
    time.sleep(delay)
    
def send(socket, address, message, delay):
  # Try to send the message otherwise print the exception
    try:
        socket.sendto(message.encode(), address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

    # Delay for a user-defined period of time
    time.sleep(delay)


# Receive the message from Tello
def receive(socket):
    # Continuously loop and listen for incoming messages
    while True:
        # Try to receive the message otherwise print the exception
        try:
            response, ip_address = socket.recvfrom(128)
            print("Received message: from Tello EDU: " + response.decode(encoding='utf-8'))
        except Exception as e:
            # If there's an error close the socket and break out of the loop
            socket
            print("Error receiving: " + str(e))
            break