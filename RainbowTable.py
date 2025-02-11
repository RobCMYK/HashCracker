import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_rainbow_table(dictionary_file):
    rainbow_table = {}
    with open(dictionary_file, 'r') as file:
        for _ in range(11):  # Skip the first 11 lines
            next(file)
        for line in file:
            password = line.strip()
            hashed_password = hash_password(password)
            rainbow_table[hashed_password] = password
    return rainbow_table

def save_rainbow_table(rainbow_table, output_file):
    with open(output_file, 'w') as file:
        for hashed_password, password in rainbow_table.items():
            file.write(f"{hashed_password}:{password}\n")

if __name__ == "__main__":
    dictionary_file = 'dictionary.txt'
    output_file = 'rainbow.txt'
    rainbow_table = create_rainbow_table(dictionary_file)
    save_rainbow_table(rainbow_table, output_file)
    print(f"Rainbow table saved to {output_file}")