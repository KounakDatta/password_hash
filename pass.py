import bcrypt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize a single Argon2 hasher instance
argon2_hasher = PasswordHasher()

# Bcrypt functions
def hash_password_bcrypt(password: str) -> bytes:
    """
    Hashes a password using Bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password_bcrypt(password: str, hashed: bytes) -> bool:
    """
    Verifies a password against a Bcrypt hash.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Argon2 functions
def hash_password_argon2(password: str) -> str:
    """
    Hashes a password using Argon2.
    """
    return argon2_hasher.hash(password)

def verify_password_argon2(password: str, hashed: str) -> bool:
    """
    Verifies a password against an Argon2 hash.
    """
    try:
        return argon2_hasher.verify(hashed, password)
    except VerifyMismatchError:
        return False

# Main function to interact with the user
def main():
    print("Password Hashing and Verification using Bcrypt and Argon2")
    print("---------------------------------------------------------")
    password = input("Enter a password to hash: ")

    # Bcrypt hashing and verification
    hashed_bcrypt = hash_password_bcrypt(password)
    print(f"\nBcrypt Hashed Password: {hashed_bcrypt.decode()}")
    password_to_verify = input("Re-enter the password to verify with Bcrypt: ")
    is_bcrypt_valid = verify_password_bcrypt(password_to_verify, hashed_bcrypt)
    print(f"Bcrypt Verification Result: {is_bcrypt_valid}")

    # Argon2 hashing and verification
    hashed_argon2 = hash_password_argon2(password)
    print(f"\nArgon2 Hashed Password: {hashed_argon2}")
    password_to_verify = input("Re-enter the password to verify with Argon2: ")
    is_argon2_valid = verify_password_argon2(password_to_verify, hashed_argon2)
    print(f"Argon2 Verification Result: {is_argon2_valid}")

if __name__ == "__main__":
    main()
