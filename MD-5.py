import hashlib
str=str(input("Enter Message:-"))
print("Message Digest Using MD-5:",hashlib.md5(str.encode()).hexdigest())
print("Message Digest Using SHA-1:",hashlib.sha1(str.encode()).hexdigest())