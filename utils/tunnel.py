# utils/tunnel.py
from sshtunnel import SSHTunnelForwarder
import config

def create_ssh_tunnel():
    tunnel = SSHTunnelForwarder(
        (config.SSH_HOST, config.SSH_PORT),
        ssh_username=config.SSH_USERNAME,
        ssh_pkey=config.SSH_PKEY,
        remote_bind_address=(config.HOSTNAME, config.DB_PORT),  # 通常是 127.0.0.1:5432
        local_bind_address=('127.0.0.1',)
    )
    tunnel.start()
    print(f"✅ SSH Tunnel started at 127.0.0.1:{tunnel.local_bind_port}")
    return tunnel
