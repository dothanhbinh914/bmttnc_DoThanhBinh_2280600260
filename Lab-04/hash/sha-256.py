import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8')) # Convert data to bytes and update into hash object
    return sha256_hash.hexdigest() # Returns the hex representation of the hash string\
        
data_to_hash = input("Enter data to hash using SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print("SHA-256 hash value:", hash_value)