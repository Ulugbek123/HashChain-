import hashlib

#Gets the seed from the user
seed = input('Enter your word to hash: ')
#MD5 Hash
MD5HASH = hashlib.md5(seed.encode()).hexdigest()
#Challenge HASH
Challenge = "c89aa2ffb9edcc6604005196b5f0e0e4"
#Prints the HASHES
print(MD5HASH)

#Loops the hashes until it reaches the original seed hash (Program knows orignal hash of "ecsc" (Or Your input seed) due to import hashlib Which contains millions of hashes
while MD5HASH != Challenge:
    MD5HASH = hashlib.md5(MD5HASH.encode()).hexdigest()  # calculate next hash
    print(MD5HASH)


print("This is the hash chain for the your seed ")
