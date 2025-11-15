import hashlib
import os

# Vakio, jota unittest voi muuttaa
CREDENTIALS_FILE = "credentials.txt"

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def load_credentials():
    if not os.path.exists(CREDENTIALS_FILE):
        return []
    with open(CREDENTIALS_FILE, "r") as f:
        return [line.strip().split(";") for line in f if line.strip()]

def save_credentials(lines):
    with open(CREDENTIALS_FILE, "w") as f:
        for parts in lines:
            f.write(";".join(parts) + "\n")

def register(username: str, password: str):
    lines = load_credentials()
    new_id = str(len(lines))
    hashed = hash_password(password)
    entry = [new_id, username, hashed]
    lines.append(entry)
    save_credentials(lines)

def login(username: str, password: str) -> bool:
    hashed = hash_password(password)
    for parts in load_credentials():
        if len(parts) == 3 and parts[1] == username and parts[2] == hashed:
            return True
    return False

def viewProfile(username: str):
    for parts in load_credentials():
        if len(parts) == 3 and parts[1] == username:
            return parts  # [id, username, hash]
    return None

def change_password(username: str, new_password: str):
    lines = load_credentials()
    for parts in lines:
        if len(parts) == 3 and parts[1] == username:
            parts[2] = hash_password(new_password)
    save_credentials(lines)

