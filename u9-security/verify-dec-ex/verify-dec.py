from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import sys

# The following function should take a signed (using 2048-bit RSA
# signature) and encrypted message (using Fernet symmetric cipher
# which is built on AES), and verify the signature and then decrypt
# the message. The encrypted signatures is at the **start** of the
# encrypted file/message.  Separate it from the remaining message 
# content.  Note: the signature is the same length (in bytes) as 
# the RSA key that was used to sign it.
#
# Refer to the following website for reference website:
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

def doDecrypt(enc_sign_file, sign_key_file, sym_key_file, out_msg_file):

    # Read Encrypted Text from File
    with open(enc_sign_file, "rb") as bin_file:
        raw_contents = bin_file.read()
        # Separate the hash and the remaining part of the message
        recv_encrypted_hash = (raw_contents[1:256]) # fill me in - remember we can splice with [start:end]
        recv_encrypted_msg =  (raw_contents[256:])  # fill me in - remember we can splice with [start:end]

    # Read Necessary Public/Private Signature Key from File
    with open(sign_key_file, "rb") as key_file:
        # Use the appropriate function "load_pem_private_key" or
        # "load_pem_public_key"
        sign_key = serialization.load_pem_public_key(  # fill in the appropriate function name.
            key_file.read(),
            backend=default_backend()
        )

    # Hash non-signature portion of the encrypted message
    h = hashes.SHA256()
    hasher = hashes.Hash(h)
    hasher.update(recv_encrypted_msg)                # fill me in - what should we hash?
    digest = hasher.finalize()
    print(f"Digest: {digest}")

    # raises an InvalidSignature exception if signatures don't match
    # Use the sign_key.verify() function
    sign_key.verify(
        digest,              # fill me in
        recv_encrypted_hash,              # fill me in
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(h)
    )
    print("Success: received and computed digest match!")


    print("Decrypt message")
    with open(sym_key_file, "rb") as key_file:
        key = key_file.read()

    # Now that we've verified the signature, decrypt the message content

    # some code here
    decrypted_text = # call the decrypt function appropriate to produce decrypted_text

    print(f"Decrypted Text: {decrypted_text}")
    print("")

    # Save the decrypted message
    with open(out_msg_file, "w") as out_file:
        out_file.write(str(decrypted_text, 'utf-8'))



if len(sys.argv) < 5:
    print("usage: verify-dec.py enc_sign_file sign_key_file sym_key_file out_msg_file")
    sys.exit(1)
doDecrypt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
