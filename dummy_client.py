import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5000))
s.send('hello')
data = s.recv(2014)
while data:
	data = s.recv(1024)
	print data
	s.send('hello')
s.close()
print 'over'