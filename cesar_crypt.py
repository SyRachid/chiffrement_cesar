from chiffrement import codage

print("'''''''Bienvenue dans le chiffrement de Cesar'''''''''")
key = input("Entrez votre clé de chiffrement en entier : ")
if key.isdigit() == False :
    print("Vérifier le format de la clé et réésayer")
else:
    message = input("entrer votre message :")
    print('le message crypté est le suivant: ')
    print(codage(message,int(key)))
    
