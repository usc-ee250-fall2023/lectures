from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import sys

# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/


def doEncrypt(msg, pvt_key_file, pub_key_file, sym_key_file, enc_file):
    print(f"Message: {msg}")
    print("")

    # Symmetric Key Encryption
    print("Generating symmetric key")
    print("")
    key = Fernet.generate_key()
    print("key", key)
    print("")

    # Save Symmetric Key to File
    with open(sym_key_file, "wb") as key_file:
        key_file.write(key)

    # Fernet uses AES in CBC mode
    # https://cryptography.io/en/latest/fernet/
    cipher_suite = Fernet(key)
    encrypted_msg = cipher_suite.encrypt(msg)

    h = hashes.SHA256()
    hasher = hashes.Hash(h)
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


    # Save Private Key to File
    print("Writing Private and Public key files\n")
    with open(pvt_key_file, "wb") as key_file:
        key_file.write(private_pem)

    # Save Private Key to File
    with open(pub_key_file, "wb") as key_file:
        key_file.write(public_pem)

    # Encrypted hash is 256 bytes since RSA Private key is 2048 bits
    encrypted_hash = private_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(h)
    )

    # Append the 256 byte hash to the start of the message
    signed_enc_msg =  encrypted_hash + encrypted_msg
    print(f"len enc hash: {len(encrypted_hash)}")
    print(f"len signed enc hash: {len(signed_enc_msg)}")
    #print(f"signed_enc_msg: {signed_enc_msg}")
    # Save Encrypted Text to File
    with open(enc_file, "wb") as bin_file:
        bin_file.write(signed_enc_msg)


if len(sys.argv) < 6:
    print("usage: sign-enc.py msg_file pvt_key_file pub_key_file sym_key_file enc_file")
    sys.exit(1)
with open(sys.argv[1], "r") as msg_file:
    asc_msg = msg_file.read()
message = bytes(asc_msg, 'utf-8')
doEncrypt(message, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
