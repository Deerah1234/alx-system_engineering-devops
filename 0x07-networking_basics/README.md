# [0x07. Networking basics #0]()

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone:

	OSI Model
		What it is
		How many layers it has
		How it is organized

	What is a LAN
		Typical usage
		Typical geographical size

	What is a WAN
		Typical usage
		Typical geographical size

	What is the Internet
		What is an IP address
		What are the 2 types of IP address
		What is localhost
		What is a subnet
		Why IPv6 was created

	TCP/UDP
		What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
		What is the main difference between TCP and UDP
		What is a port
		Memorize SSH, HTTP and HTTPS port numbers
		What tool/protocol is often used to check if a device is connected to a network

## Mandatory tasks

### Tasks 0 - 3 contain multiple choice questions.

### [Task 4](https://github.com/leulyk/alx-system_engineering-devops/blob/main/0x07-networking_basics/4-TCP_and_UDP_ports)

Write a Bash script that displays listening ports:

	That only shows listening sockets
	That shows the PID and name of the program to which each socket belongs

### [Task 5](https://github.com/leulyk/alx-system_engineering-devops/blob/main/0x07-networking_basics/5-is_the_host_on_the_network)

Write a Bash script that pings an IP address passed as an argument.

	Requirements:

	Accepts a string as an argument
	Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
	Ping the IP 5 times
