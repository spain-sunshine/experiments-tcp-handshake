# 四次挥手的过程如下：

# 客户端发送FIN。
# 服务器响应ACK。
# 服务器发送FIN。
# # 客户端响应ACK。

# SYN(synchronous建立联机)
# ACK(acknowledgement 确认)
# PSH(push传送)
# FIN(finish结束)
# RST(reset重置)
# URG(urgent紧急)
# Sequence number(顺序号码，用小写seq代替)
# Acknowledge number(确认号码，用小写ack代替)

def client_send_fin():
    print("客户端：发送FIN")
    server_receive_fin()

def server_receive_fin():
    print("服务器：接收FIN，发送ACK")
    client_receive_ack()

def client_receive_ack():
    print("客户端：收到ACK")

def server_send_fin():
    print("服务器：发送FIN")
    client_receive_fin()

def client_receive_fin():
    print("客户端：接收FIN，发送ACK")
    server_final_ack()

def server_final_ack():
    print("服务器：收到ACK，连接终止")

client_send_fin()

