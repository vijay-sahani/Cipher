from random import randint
'''
Ceasor cipher also known as subsitutionn cipher was by julius cipher 
First used in miltary affairs 
The ceasor cipher involes replacing each letters of the alphabet with the letter standing down the alphabet
'''

letters=[chr(i) for i in range(97,123)]

key=randint(3,6)

print(key)
def caeser_Cipher(text):
    '''
    Transforming the plaintext in cipher text
    '''
    Cipher_text,text="",text.lower().strip()

    for i in range(len(text)):
        if text[i] in letters:
            val=letters.index(text[i])+key
            if val>=26:
                val=val%26
            Cipher_text+=letters[val]
        elif text[i] in "@!*#$%&();\"'":
            Cipher_text+=text[i]
        else:
            Cipher_text+=" "
    return Cipher_text



def decrypt_text(text,key):
    """
    Recovering the cipher text to plaintext.
    A key in required to dicipher text which was used the encrpyt the plaintext
    """
    diCipher_text,text="",text.lower()
    for i in range(len(text)):
        if text[i] in letters:
            val=letters.index(text[i])-key
            if val<0:
                val=26+val
            diCipher_text+=letters[val]
        elif text[i] in "@!*#$%&();\"'":
            diCipher_text+=text[i]
        else:
            diCipher_text+=" "
    return diCipher_text.capitalize()


if __name__ == "__main__":
    while True:
        a=caeser_Cipher(input(">"))
        print("Encrypted text is:",a)
        print("Decrypted text is:",decrypt_text(a,key))