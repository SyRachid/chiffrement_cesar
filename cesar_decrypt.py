from dechiffrement import decryptage

print("'''''''''''''''''Brute force de cesar par analyse frequentielle''''''''''''''''''''''")
message = input('message: ')
# lettre_magique = input('entrez la lettre la plus frequente de votre langue: ')
message_clair,key, plusfrequent = decryptage(message)
print("la clé est : ",key)
print("la lettre la plus fréquente est", plusfrequent)
print("message en clair est :  ",message_clair)        
