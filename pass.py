import streamlit as st
import bcrypt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize a single Argon2 hasher instance
argon2_hasher = PasswordHasher()

# Bcrypt functions
def hash_password_bcrypt(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password_bcrypt(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Argon2 functions
def hash_password_argon2(password: str) -> str:
    return argon2_hasher.hash(password)

def verify_password_argon2(password: str, hashed: str) -> bool:
    try:
        return argon2_hasher.verify(hashed, password)
    except VerifyMismatchError:
        return False

# Streamlit app
def main():
    st.title("Password Hashing and Verification using Bcrypt and Argon2")

    password = st.text_input("Enter a password to hash:", type="password")
    if password:
        # Bcrypt
        hashed_bcrypt = hash_password_bcrypt(password)
        st.write("Bcrypt Hashed Password:")
        st.code(hashed_bcrypt.decode())

        password_to_verify_bcrypt = st.text_input("Re-enter the password to verify with Bcrypt:", type="password", key="bcrypt")
        if password_to_verify_bcrypt:
            is_bcrypt_valid = verify_password_bcrypt(password_to_verify_bcrypt, hashed_bcrypt)
            st.write(f"Bcrypt Verification Result: {is_bcrypt_valid}")

        # Argon2
        hashed_argon2 = hash_password_argon2(password)
        st.write("Argon2 Hashed Password:")
        st.code(hashed_argon2)

        password_to_verify_argon2 = st.text_input("Re-enter the password to verify with Argon2:", type="password", key="argon2")
        if password_to_verify_argon2:
            is_argon2_valid = verify_password_argon2(password_to_verify_argon2, hashed_argon2)
            st.write(f"Argon2 Verification Result: {is_argon2_valid}")

if __name__ == "__main__":
    main()
