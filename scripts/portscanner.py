import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_target = 'localhost'
http_port = 80
ssh_port = 22
https_port = 443

open_port = []
 
for i in range(1, 10000):

	try:

		print('connecting to {}:{}'.format(host_target, i))
		sock.connect(('localhost', i))
		print("port %s open"%i)
		open_port.append(i)

		if i == http_port:
			print('http port is open')

		elif i == ssh_port: 
			print('ssh port is open')

		elif i == https_port:
			print('https port is open')

	except Exception as err:
		print('{}:{} --> closed'.format(host_target, i))

print(open_port)
