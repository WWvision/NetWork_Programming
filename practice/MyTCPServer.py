class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('',port))
        self.sock.listen(5)
        
    def Accept(self):
        self.client_sock, self.client_addr = self.sock.accept()
        return self.client_sock, self.client_addr
    
    if __name__ == '__main__':
        sock = TCPServer(8888)
        client_socket, addr = sock.Accept()
        print('Connected By ', addr)
        client_socket(b'Hello Client')
        client_socket.close()