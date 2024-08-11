from dechiffrement import decryptage
from logo import skull

print(skull)
print("'''''''''''''''''Brute force de cesar par analyse frequentielle''''''''''''''''''''''")
print("''''''''''''''''''powered  by Rachid Sanogo''''''''''''''''''''''''''''''''''''''''''''")
message = input('message: ')
# lettre_magique = input('entrez la lettre la plus frequente de votre langue: ')
message_clair,key, plusfrequent = decryptage(message)
print("la clé est : ",key)
print("la lettre la plus fréquente est", plusfrequent)
print("message en clair est :  ",message_clair)        
