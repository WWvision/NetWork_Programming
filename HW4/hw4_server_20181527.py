import socket

port = 7625
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(1)
print('Waiting Client Connection...')

while True: 
    client_socket, addr = server_socket.accept()
    print('Connection from Client IP:', addr)
    client_socket.send(str(addr[0]).encode())
    while True:
        inp_data = client_socket.recv(1024).decode()
        return_val = 0
        result_msg = ''
        if not inp_data:
            break;
        
        try:
            inp_list = inp_data.split(' ')
            if len(inp_list)==3:
                try:
                    a = int(inp_list[0])
                    b = int(inp_list[2])
                except:
                    raise Exception('Data is not number. Please input number')
                else:
                    calc = inp_list[1]
                    if calc == '+':
                        return_val = a + b
                    elif calc == '-':
                        return_val = a - b
                    elif calc == '*':
                        return_val = a * b
                    elif calc == '/':
                        return_val = a / b
                        return_val = round(return_val, 1)
                    else:
                        raise Exception('Wrong Expression. Availabe Express is  +,-,*,/')
            else:
                raise Exception('Wrong Format. Please Input "a + b" : It is seperated by space')
        except Exception as Excp:
            result_msg = str(Excp).encode()
        except:
            err = 'Error: Receive Wrong Data. Try again'
            result_msg = err.encode()
        else:
            result_msg = str(return_val).encode()
        finally:
            client_socket.send(result_msg)
    client_socket.close()