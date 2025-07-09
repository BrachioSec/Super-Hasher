import hashlib

def hash_char(char, algo):
    h = hashlib.new(algo)
    h.update(char.encode())
    return h.hexdigest()

def hash_word_reversed(word):
    algos = ['md5', 'sha1', 'sha256', 'sha3_512', 'blake2b']
    reversed_word = word[::-1]  # Reverse the word

    hashed_chars = []
    for i, char in enumerate(reversed_word):
        algo = algos[i % len(algos)]
        hashed_chars.append(hash_char(char, algo))

    return ''.join(hashed_chars)

def scramble_hash(s):
    words = s.split()
    hashed_words = [hash_word_reversed(word) for word in words]
    return ''.join(hashed_words)

if __name__ == "__main__":
    user_input = input("Enter the string you want to hash: ")
    result = scramble_hash(user_input)
    print("\nScrambled Hash Result:\n", result)
