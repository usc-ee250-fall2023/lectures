from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import time

message = b"Four score and seven years ago our fathers brought forth, upon this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal"

# Symmetric Key Encryption
print("*********************************")
print("Let's first test Symmetric Key ")
print("*********************************")
key = Fernet.generate_key()
print("key", key)
print("")

# Save Symmetric Key to File
with open("symmetric_key.key", "wb") as key_file:
    key_file.write(key)

# Read Symmetric Key from File
with open("symmetric_key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

start_time = time.time()
encrypted_text = cipher_suite.encrypt(message)
end_time = time.time()
print(f"Symmetric Encryption Time: {end_time - start_time}")
print("")

# Save Encrypted Text to File
with open("symmetric_encrypted_text.txt", "wb") as text_file:
    text_file.write(encrypted_text)

# Read Encrypted Text from File
with open("symmetric_encrypted_text.txt", "rb") as text_file:
    encrypted_text = text_file.read()

start_time = time.time()
decrypted_text = cipher_suite.decrypt(encrypted_text)
end_time = time.time()
print(f"Symmetric Decryption Time: {end_time - start_time}")
print("")

print(f"Encrypted Text: {encrypted_text}")
print("")
print(f"Decrypted Text: {decrypted_text}")
print("")

print("*********************************")
print("Now for Asymmetric Key Encryption")
print("*********************************")

# Asymmetric Key Encryption
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Print Private Key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
print(f"Private Key: {private_pem}")
print("")

public_key = private_key.public_key()

# Print Public Key
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(f"Public Key: {public_pem}")
print("")



# Save Private Key to File
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_pem)

# Save Private Key to File
with open("public_key.pem", "wb") as key_file:
    key_file.write(public_pem)

# Read Public Key from File
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

# Read Private Key from File
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )


start_time = time.time()
encrypted_text = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
end_time = time.time()
print(f"Asymmetric Encryption Time: {end_time - start_time}")
print("")


# Save Encrypted Text to File
with open("asymmetric_encrypted_text.bin", "wb") as text_file:
    text_file.write(encrypted_text)

# Read Encrypted Text from File
with open("asymmetric_encrypted_text.bin", "rb") as text_file:
    encrypted_text = text_file.read()

start_time = time.time()
decrypted_text = private_key.decrypt(
    encrypted_text,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
end_time = time.time()
print(f"Asymmetric Decryption Time: {end_time - start_time}")
print("")

print(f"Encrypted Text: {encrypted_text}")
print("")
print(f"Decrypted Text: {decrypted_text}")
print("")


# Save Private Key to File
#with open("private_key.pem", "wb") as key_file:
#    key_file.write(private_pem)

# Read Private Key from File
#with open("private_key.pem", "rb") as key_file:
#    private_key = serialization.load_pem_private_key(
#        key_file.read(),
#        password=None,
#        backend=default_backend()
#    )

# Decrypt Message
#decrypted_text = private_key.decrypt(
#    encrypted_text,
#    padding.OAEP(
#        mgf=padding.MGF1(algorithm=hashes.SHA256()),
#        algorithm=hashes.SHA256(),
#        label=None
#    )
#)
#print(f"Decrypted Text: {decrypted_text}")

