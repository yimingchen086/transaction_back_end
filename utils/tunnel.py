from sshtunnel import SSHTunnelForwarder
import config
import os

def create_ssh_tunnel():
    tunnel = SSHTunnelForwarder(
        (config.SSH_HOST, config.SSH_PORT),
        ssh_username=config.SSH_USERNAME,
        ssh_pkey=os.path.expanduser(config.SSH_PKEY),
        remote_bind_address=('127.0.0.1', 5432),
        local_bind_address=('127.0.0.1', 0)  # 自動選擇一個可用 port
    )
    tunnel.start()
    return tunnel
