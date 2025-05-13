from cryptography.fernet import Fernet
import random
import os

Names = ["Yuzu", "Ryu", "Malau", "Kassy", "Audrey", "Sarah", "Kora"]
Namesmod = ["Yuzu", "Ryu", "Malau", "Kassy", "Audrey", "Sarah", "Kora"]
Result = {}


def attribution(prenom):
    i = random.randrange(len(Namesmod))
    while (Namesmod[i] == prenom) or (Namesmod[i] in Result.values()) or (Namesmod[i] == None) :
        i = random.randrange(len(Namesmod))
    return Namesmod[i]

def draw():
    for prenom in Names :
        choisi = attribution(prenom)
        Result.update({prenom : choisi})

draw()

f= open("ListeSecrete2023.txt","w")
for keys in Result :
    f.write(keys+" "+Result[keys]+"\n")
f.close()


key = Fernet.generate_key()
with open('unlock.key', 'wb') as unlock:
     unlock.write(key)
print(key)

f2 = Fernet(key)
with open('ListeSecrete2023.txt', 'rb') as original_file:
    original = original_file.read()
encrypted = f2.encrypt(original)
with open ('enc_list.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

if os.path.exists("ListeSecrete2023.txt"):
    os.remove("ListeSecrete2023.txt")
