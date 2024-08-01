from alphabet import *

def position(x):
    if x.isalpha():
      if x in alphabet:
          return ord(x)-ord('a')
      if x in alphabet_majuscule:
          return ord(x)-ord('A')
      else:
          return -1
    return -1

def decalage(x,n):
    pos = position(x) 
    if pos != -1:
        if x in alphabet:
            posi = (pos + n )%26
            decal =  chr(ord('a') + posi)
        if x in alphabet_majuscule:
            posi = (pos + n )%26
            decal =  chr(ord('A') + posi)
        return decal
    else:
        return x
        
    

def codage(texte,n):
    code = ''
    for lettre in texte:
        decal = decalage(lettre,n)
        code = code + decal
    return code


