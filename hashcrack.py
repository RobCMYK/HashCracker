from passlib.hash import sha512_crypt
def main():
    print("Running...")

    with open('dictionary.txt', 'r') as dict_file:
        dictionary = dict_file.read().splitlines()

    with open('shadow.txt', 'r') as shadow_file:
        shadow_entries = shadow_file.read().splitlines()
    
    found_any = False
    
    for entry in shadow_entries:
        parts = entry.split(':')
        username = parts[0]
        hashed_password = parts[1]

        if hashed_password in ['*', '!', '']:
            continue

        for word in dictionary:
            if sha512_crypt.verify(word, hashed_password):
                print(f"Found password for {username}: {word}")
                found_any = True
                break
    if not found_any:
        print("No passwords found")

if __name__ == '__main__':
    main()