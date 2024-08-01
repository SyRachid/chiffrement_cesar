from chiffrement import decalage, position

def nombre_occurence(texte,x):
    occur = 0
    for lettre in texte:
        if lettre == x:
            occur=occur+1
    return occur

def plus_frequent(texte):
    max_occur = 0
    plusf = ''
    for lettre in texte:
        if lettre.isalpha():
            occur = nombre_occurence(texte,lettre)
            if  occur > max_occur:
                plusf =  lettre
                max_occur = occur
    return plusf


def decryptage(code):
    texte_clair =''
    plusf = plus_frequent(code)
    if plusf.islower():
        decal = position(plusf)-position("e")
    if plusf.isupper():
        decal = position(plusf)-position("E")
    for lettre in code :
        texte_clair = texte_clair + decalage(lettre,-decal)
    return texte_clair, decal, plusf



# print(nombre_occurence('abccdrdécdef','c'))
#print(plus_frequent(''))