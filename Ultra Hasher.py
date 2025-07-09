import hashlib
import random

def split_string(s, parts=5):
    length = len(s)
    chunk_size = length // parts
    chunks = []

    for i in range(parts):
        start = i * chunk_size
        # Add remaining chars to the last chunk
        end = start + chunk_size if i < parts - 1 else length
        chunks.append(s[start:end])

    return chunks

def hash_chunk(chunk, algo):
    h = hashlib.new(algo)
    h.update(chunk.encode())
    return h.hexdigest()

def scramble_hash(s):
    algos = ['md5', 'sha1', 'sha256', 'sha3_512', 'blake2b']
    chunks = split_string(s, len(algos))

    hashed_chunks = []
    for chunk, algo in zip(chunks, algos):
        hashed = hash_chunk(chunk, algo)
        hashed_chunks.append(hashed)

    # Shuffle the hashes
    random.shuffle(hashed_chunks)

    # Join and return
    return ''.join(hashed_chunks)

if __name__ == "__main__":
    user_input = input("Enter the string you want to hash: ")
    result = scramble_hash(user_input)
    print("\nScrambled Hash Result:\n", result)
