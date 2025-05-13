from cryptography.fernet import Fernet
import os

Result = {}

key = b'4Q0lIQfKnHwRI-oNIG-5AtFfc2V6QrIw3yfh4Ja00OU='
f2 = Fernet(key)
with open('_internal/enc_list.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
decrypted = f2.decrypt(encrypted)
with open('ListeSecrete2023.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

f= open("ListeSecrete2023.txt","r")
contents =f.readlines()
for line in contents :
    give = ""
    receive = ""
    turn = 0
    for c in line :
        if c!= ' ' and turn == 0:
            give+=c
        elif c!=' ':
            receive+=c
        else :
            turn = 1
    Result.update({give : receive})


f.close()

if os.path.exists("ListeSecrete2023.txt"):
    os.remove("ListeSecrete2023.txt")

Mdp = {"TropBien5204" : "Yuzu", "emuotoridegenshinimpact" : "Ryu", "Scarawife" : "Malau", "Zizimoisi" : "Kassy", "Skz_h" : "Sarah", "Itsmuffintime" : "Kora", "géfroi" : "Audrey"}
def main() :
    mot = input("Bien le bonjour!\nCe petit programme te permettra de connaitre ton rôle lors de ce Secret Santa édition 2023.\nDe qui seras-tu le père Noël?\nPour le savoir, je t'invite à rentrer ton mot de passe, te donnant accès à ton tirage : ")
    while mot not in Mdp :
        print("\n")
        mot = input("Mince, tu as dû te tromper, le mot de passe incorrect :'( Tente de le rentrer à nouveau ? : ")
    print("\n")
    print(Mdp.get(mot),"cette année tu es le père Noël de",Result.get(Mdp.get(mot)))
    print("\n")
    test = input("Maintenant que tu sais qui est ton Secret Child, bonne chance pour son cadeau!\n")

if __name__ == "__main__":
    main()