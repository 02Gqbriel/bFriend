from werkzeug.security import check_password_hash, generate_password_hash


def hash_password(password: str):
    return generate_password_hash(password)


def compare_password(password: str, hash: str):
    return check_password_hash(hash, password)
