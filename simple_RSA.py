import math
import random
def is_prime(number):
    if number <2:
        return False
    for i in range(2,number //2+1):
        if number % i==0:
            return False
    return True

def prime_num(min_value,max_value):
    prime=random.randint(min_value,max_value)
    while not is_prime(prime):
        prime=random.randint(min_value,max_value)
    return prime

def gen_key(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randrange(1,phi)
    while math.gcd(e,phi)!=1:
        e=random.randrange(1,phi)
    d=pow(e,-1,phi)
    return ((e,n),(d,n))
def Encryption(pub,plain):
    e,n=pub
    cypher_text=[pow(ord(char),e,n) for char in plain]
    return cypher_text

def Decryption(pri,cipher_text):
    d,n=pri
    plain_text=[chr(pow(char,d,n))for char in cipher_text]
    return''.join(plain_text)


p=prime_num(100,200)
q=prime_num(100,150)
public_key,private_key=gen_key(p,q)
msg=input("Enter your message:\n")
e=Encryption(public_key,msg)
print("Encrypted message:-",e)
de=Decryption(private_key,e)
print("Decrypted message:-",de)
print("")
print("PRIVATE_KEY=",private_key)
print("PUBLIC_KEY=",public_key)