# 三次握手的过程如下：

# 客户端发送SYN。
# 服务器响应SYN-ACK。
# 客户端发送ACK。

def client_send_syn():
    print("客户端：发送SYN")
    server_receive_syn()

def server_receive_syn():
    print("服务器：收到SYN，发送SYN-ACK")
    client_receive_syn_ack()

def client_receive_syn_ack():
    print("客户端：收到服务器SYN-ACK，发送ACK")
    server_receive_ack()

def server_receive_ack():
    print("服务器：收到ACK，连接建立")

client_send_syn()