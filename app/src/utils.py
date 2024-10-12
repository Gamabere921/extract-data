# Funciones utilitarias pueden ser agregadas aquí.
# Por ejemplo, una función para encriptar contraseñas.
def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
