from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import time

# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

message = b"How did we beat Cal by only 1 point"

def doEncrypt(msg):
    print(f"Message: {msg}")
    print("")

    # Symmetric Key Encryption
    print("Generating symmetric key")
    print("")
    key = Fernet.generate_key()
    print("key", key)
    print("")

    # Save Symmetric Key to File
    with open("symmetric_key.key", "wb") as key_file:
        key_file.write(key)

    cipher_suite = Fernet(key)
    encrypted_msg = cipher_suite.encrypt(msg)

    # h = hashlib.sha256()
    # h.update(encrypted_msg)
    # myhexdigest =  h.hexdigest()
    # digest = h.digest()
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash)
    hasher.update(encrypted_msg)
    digest = hasher.finalize()
    print(f"Digest: {digest}")

    # Asymmetric Key Encryption
    print("Generating key pair")
    print("")
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
    # print(f"Private Key: {private_pem}")
    # print("")

    public_key = private_key.public_key()

    # Print Public Key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # print(f"Public Key: {private_pem}")
    # print("")

    # Save Private Key to File
    with open("private_key.pem", "wb") as key_file:
        key_file.write(private_pem)

    # Save Private Key to File
    with open("public_key.pem", "wb") as key_file:
        key_file.write(public_pem)

    encrypted_hash = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(chosen_hash)
    )

    signed_enc_msg =  encrypted_hash + encrypted_msg
    print(f"len enc hash: {len(encrypted_hash)}")
    print(f"len signed enc hash: {len(signed_enc_msg)}")
    print(f"signed_enc_msg: {signed_enc_msg}")
    # Save Encrypted Text to File
    with open("encrypted_message.bin", "wb") as bin_file:
        bin_file.write(signed_enc_msg)



# # Save Encrypted Text to File
# with open("asymmetric_encrypted_text.bin", "wb") as text_file:
#     text_file.write(digest_and_message)




def doDecrypt():

    # Read Encrypted Text from File
    with open("encrypted_message.bin", "rb") as bin_file:
        recv_encrypted_msg = bin_file.read()
        recv_encrypted_hash = recv_encrypted_msg[:256]
        recv_encrypted_msg = recv_encrypted_msg[256:]

    # Read Public Key from File
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # h = hashlib.sha256()
    # h.update(recv_encrypted_msg)
    # myhexdigest =  h.hexdigest()
    # digest = h.digest()
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash)
    hasher.update(recv_encrypted_msg)
    digest = hasher.finalize()
    print(f"Digest: {digest}")

    # raises an InvalidSignature exception if signatures don't match
    public_key.verify(
        recv_encrypted_hash,
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(chosen_hash)
    )
    print("Success: received and computed digest match!")


    # print(f"Recv decrypted Digest: {recv_digest}")

    # h = hashlib.sha256()
    # h.update(recv_encrypted_msg)
    # myhexdigest =  h.hexdigest()
    # computed_digest = h.digest()
    # print(f"Recv Computed Digest: {computed_digest}")

    # if(recv_digest != computed_digest):
    #     print(f"Failure - received digest: {recv_digest} does not match computed digest: {computed_digest}")
    #     return
    # else:
    #     print("Success: received and computed digest match!")

    # Read Symmetric Key from File
    with open("symmetric_key.key", "rb") as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    print("Decrypt message")
    decrypted_text = cipher_suite.decrypt(recv_encrypted_msg)

    print(f"Decrypted Text: {decrypted_text}")
    print("")



doEncrypt(message)
doDecrypt()