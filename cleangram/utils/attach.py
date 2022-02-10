import secrets


def attach(file, files):
    token = secrets.token_urlsafe(6)
    files[token] = file
    return f"attach://{token}"
