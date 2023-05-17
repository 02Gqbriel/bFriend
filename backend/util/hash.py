from werkzeug.security import check_password_hash, generate_password_hash

def hashPassword(password: str):
    return generate_password_hash(password)

def comparePassword(password: str, hash: str):
    return