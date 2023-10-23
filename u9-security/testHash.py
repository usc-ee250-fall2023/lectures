import hashlib

def hash_file(filename):
    """Returns the SHA-256 hash of the contents of a file."""
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        data = f.read()
        h.update(data)
    return h.hexdigest()

def write_string_to_file(string, filename):
    """Writes a string to a file."""
    with open(filename, 'w') as f:
        f.write(string)

def write_hash_to_file(hash_value, filename):
    """Writes a hash value to a file."""
    with open(filename, 'w') as f:
        f.write(hash_value)

def read_hash_from_file(filename):
    """Reads a hash value from a file."""
    with open(filename, 'r') as f:
        return f.read().strip()

def verify_hash(text_filename, hash_filename):
    """Verifies if the hash of the contents of a text file matches the hash value stored in another file."""
    text_hash = hash_file(text_filename)
    stored_hash = read_hash_from_file(hash_filename)
    return text_hash == stored_hash

# Example usage
string = "Hello World!"
string2 = "Hello World!"
text_filename = "text.txt"
text2_filename = "text2.txt"
hash_filename = "hash.txt"

write_string_to_file(string, text_filename)
write_string_to_file(string2, text2_filename)
text_hash = hash_file(text_filename)
write_hash_to_file(text_hash, hash_filename)

if verify_hash(text2_filename, hash_filename):
    print("The hash matches!")
else:
    print("The hash does not match.")
