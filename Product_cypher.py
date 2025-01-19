import math
def Sub_encr(text,key):
    Encrypted_text=""
    for char in text:
        if char.islower():
            Encrypted_text+=chr((ord(char)+key-ord("a"))%26+ord("a"))
        elif char.isupper():
           Encrypted_text+=chr((ord(char)+key-ord("A"))%26+ord("A")) 
        else:
            Encrypted_text+=char
    return Encrypted_text
def Sub_decr(text,key):
    Decrypted_text=""
    for char in text:
        if char.islower():
            Decrypted_text+=chr((ord(char)-key-ord("a"))%26+ord("a"))
        elif char.isupper():
           Decrypted_text+=chr((ord(char)-key-ord("A"))%26+ord("A")) 
        else:
            Decrypted_text+=char
    return Decrypted_text
def Tran_encr(text,key):
    Encrypted_text=[""]*key
    for col in range(key):
        po=col
        while po <len(text):
            Encrypted_text[col]+=text[po]
            po+=key
    return "".join(Encrypted_text)
def Tran_decr(text,key):
    nocol=math.ceil(len(text)/key)
    norow=key
    box=(nocol*norow)-len(text)
    Decrypted_text=[""]*nocol
    col=0
    row=0
    for symbol in text:
        Decrypted_text[col]+=symbol
        col+=1
        if(col==nocol)or(col==nocol-1 and row>=norow-box):
                         col=0
                         row+=1
    return"".join(Decrypted_text)
    
text=input("Enter you Message:\n")
key=int(input("Enter a key value between1-9:"))
suen=Sub_encr(text,key)
tren=Tran_encr(suen,key)
print("Message after encyption:\n",tren)
trde=Tran_decr(tren,key)
sude=Sub_decr(trde,key)
print("Original message is:\n",sude)