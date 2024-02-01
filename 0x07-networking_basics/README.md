# Networking Basics #0

This repository contains information and scripts related to fundamental networking concepts. The tasks cover topics such as the OSI model, types of networks, MAC and IP addresses, UDP and TCP protocols, and TCP/UDP ports.

## Tasks:

### 0. OSI Model
* [0-OSI_model](./0-OSI_model): Text file answering the following questions:
  * What is the OSI model?
    - The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology.

  * How is the OSI model organized?
    - From the lowest to the highest level

### 1. Types of Network
* [1-types_of_network](./1-types_of_network): Text file answering the following questions:
  * What type of network is a computer in a local connected to?
    - LAN

  * What type of network could connect an office in one building to another office in a building a few streets away?
    - WAN

  * What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?
    - Internet

### 2. MAC and IP Address
* [2-MAC_and_IP_address](./2-MAC_and_IP_address): Text file answering the following questions:
  * What is a MAC address?
    - The unique identifier of a network interface

  * What is an IP address?
    - Is to devices connected to a network what a postal address is to houses

### 3. UDP and TCP
* [3-UDP_and_TCP](./3-UDP_and_TCP): Text file answering the following questions:
  * Which statement is correct for the TCP box?
    - It is a protocol that is transferring data in a fast way and might lose data along in the process.

  * Which statement is correct for the UDP box?
    - It is a protocol that is transferring data in a fast way and might lose data along in the process.

  * Which statement is correct for the TCP worker?
    - May I increase the rate at which I am sending you boxes?

### 4. TCP and UDP Ports
* [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports): Bash script that displays listening ports.
  - Displays listening sockets.
  - Shows the PID and name of the program to which each socket belongs.

### 5. Is the Host on the Network
* [5-is_the_host_on_the_network](./5-is_the_host_on_the_network): Bash script that pings an IP address received as an argument 5 times.
  - Usage: `5-is_the_host_on_the_network {IP_ADDRESS}`.
