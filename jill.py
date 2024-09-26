import hashlib
import argparse

# Gives an argument in argparse that allows you to put two different arguements
parser = argparse.ArgumentParser()
parser.add_argument("password_file")
parser.add_argument("dictionary_file")
args = parser.parse_args()
passwords = args.password_file
dictionary = args.dictionary_file

hashes = []
names = []
output = []
# Opens up the password file and reads each line
with open(passwords) as f:
    encrypt = f.readlines()

# For every line in the file, it splits the lines into names and hashes and saves them into a list.
for line in encrypt:
    hash = line.split(':')[1].rstrip("\n")
    name = line.split(':')[0]
    hashes.append(hash)
    names.append(name)

# Opens up the wordlist.txt file
with open (dictionary) as x:
    encrypt = x.readlines()
# Saves the line that you are on
for index, line in enumerate(encrypt):
    sha256_hash = hashlib.sha256()
    password = (line.replace('\n', ''))
    # hashes every password in there in SHA 256 format
    sha256_hash.update(password.encode('utf-8'))
    # If the password in the wordlist.txt matches the hash in the passwords.txt file...
    if str(sha256_hash.hexdigest()) in hashes:
        # Prints the outcome in "names:password"
        output.append([hashes.index(str(sha256_hash.hexdigest())), f"{names[hashes.index(str(sha256_hash.hexdigest()))]}:{encrypt[index].rstrip("\n")}"])
output.sort()

for line in output:
    print(line[1])