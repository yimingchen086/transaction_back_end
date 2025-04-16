import os
from dotenv import load_dotenv

load_dotenv()

# SSH config
SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = int(os.getenv("SSH_PORT", 22))
SSH_USERNAME = os.getenv("SSH_USERNAME")
SSH_PKEY = os.path.expanduser(os.getenv("SSH_PKEY"))

# 遠端DB config
HOSTNAME = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_NAME")

DB_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{HOSTNAME}:{DB_PORT}/{DATABASE}"

# 本地 DB
LOCAL_HOSTNAME = os.getenv("LOCAL_DB_HOST", "127.0.0.1")
LOCAL_DB_PORT = int(os.getenv("LOCAL_DB_PORT", 5432))
LOCAL_USERNAME = os.getenv("LOCAL_DB_USERNAME", "postgres")
LOCAL_PASSWORD = os.getenv("LOCAL_DB_PASSWORD", "yourlocalpassword")
LOCAL_DATABASE = os.getenv("LOCAL_DB_NAME", "budget_local")

LOCAL_DB_URI = f"postgresql://{LOCAL_USERNAME}:{LOCAL_PASSWORD}@{LOCAL_HOSTNAME}:{LOCAL_DB_PORT}/{LOCAL_DATABASE}"
