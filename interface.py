import socket
import sys
import threading



class interface:

	HOST 		= ''                 # Symbolic name meaning all available interfaces
	PORT 		= 50007              # Arbitrary non-privileged port
	s 		= None               # new socket just created init or existing socket passing by arg 
	state 		= None
	clients 	= []                 
	running 	= False              # a flag allowing listening foever 
	_t 		= None               # thread instance

	def __init__(self, sock=None, HOST='',PORT=50007):
		
		# Set Values
		self.HOST = HOST
		self.PORT = PORT
		# Create Socket
		if sock is None:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.bind((HOST, PORT))
		else:
			self.s = sock

	def _run(self, backlog=1): # The backlog argument specifies the maximum number of queued connections and should be at least 0;
		try:
			self.s.listen(backlog)
			self.state = 'listening'
			print 'listening'
			while running:
					client = serversocket.accept() # (clientsocket, address)
					clients.append(client)
					self.state = 'connected'
					print 'connected'
		except:
			self.state = None

	def run(self, backlog=1):
		running = True
		t = threading.Thread(target=self._run, args=(backlog,))
		t.start()
		self._t = t
		return t

	def send(self, msg): # Same as socket.sendall()?
		if not state:return False
		try:
			MSGLEN = len(msg)
			totalsent = 0
			while totalsent < MSGLEN:
				sent = self.s.send(msg[totalsent:])
				if sent == 0:
					raise RuntimeError("socket connection broken")
				totalsent = totalsent + sent
		except RuntimeError:
			self._client_dead()

	def recv(self,MSGLEN=2048):
		if not state:return False
		chunks = []
		bytes_recd = 0
		try:
			while bytes_recd < MSGLEN:
				chunk = self.s.recv(min(MSGLEN - bytes_recd, 2048))
				if chunk == '':
					print 'Remote client disconnected'
					raise RuntimeError("socket connection broken")
				chunks.append(chunk)
				bytes_recd = bytes_recd + len(chunk)
			return ''.join(chunks)
		except RuntimeError:
			self._client_dead()

	def _client_dead(self):
		clients = []

	def __del__(self):
		self.running = False
		if self._t: dir(self._t)
		if self.s: self.s.close()
		self.s = None
		print 'bye'

i = interface()
i.run()

while True:
	#interface run forever
	pass

	
