# Tello Swarm
A simple Python package for controlling multiple DJI Tello drones at once using the official Tello SDK.

## Installation
To install, simply run:

```python 
pip install tello_swarm
```

## Usage
### Initializing the Drones
To initialize a single drone, create a Drone object and pass in its IP address, command and video ports. For example:

```python 
from tello_swarm import Drone

drone1 = Drone('192.168.0.126', 8889, 9010)
drones = [drone1]
```

To initialize multiple drones, create a Drone object for each drone and add them to a list. For example:

```python 
from tello_swarm import Drone

drone1 = Drone('192.168.0.129', 8889, 9010)
drone2 = Drone('192.168.0.101', 8889, 9011)
drone3 = Drone('192.168.0.206', 8889, 9012)
drone4 = Drone('192.168.0.96', 8889, 9013)
drones = [drone1, drone2, drone3, drone4]
```

### Sending Commands to the Drones
To send a command to the drones, call the send method of the Drone object. For example, to put the drones into command mode and then take off:

```python 
from tello_swarm import Drone

# Create and start a listening thread for each drone
for drone in drones:
    receive_thread = threading.Thread(target=drone.receive)
    receive_thread.daemon = True
    receive_thread.start()

# Put Tello drones into command mode
Drone.send_swarm(drones, 'command', 3)
Drone.send_swarm(drones, 'takeoff', 3)
```

The code above will create a thread for each drone and start listening for responses from the drones. Then it will send a command to put the drones in command mode, followed by a command to take off, and finally a command to land. Lastly, it will close all sockets.

### Example: Flying a Square
Here's an example of how to make a swarm of drones fly in a square using the Drone class:

```python 
# Create and start a listening thread for each drone
for drone in drones:
    receive_thread = threading.Thread(target=drone.receive)
    receive_thread.daemon = True
    receive_thread.start()

# Put Tello drones into command mode
Drone.send_swarm(drones, 'command', 3)

# Takeoff
Drone.send_swarm(drones, 'takeoff', 3)

box_leg_distance = 60
yaw_angle = 90

# Loop and create each leg of the box
for i in range(4):
    # Fly forward
    Drone.send_swarm(drones, "forward " + str(box_leg_distance), 3)
    # Yaw right
    Drone.send_swarm(drones, "cw " + str(yaw_angle), 3)

Drone.send_swarm(drones, 'land', 3)

# Close all sockets
Drone.close_connection(drones)
```

## Conclusion
The Drone class makes it easy to control a swarm of Tello drones from Python. With this class, you can send commands to multiple drones simultaneously and even make them fly in formations. Happy flying!
