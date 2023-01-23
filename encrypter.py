#program for encrypting and decrypting

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          ]

def encrypt(plain_text,shift):
    cipher_text=""
    for i in text:
        '''
        This is correct when we don't want to include only alphabets
         e.g zullu 
        a=ord(text[i])+shift
        texts+=chr(a)
        '''
        position=alphabet.index(i)
        newpos=position+shift
        cipher_text+=alphabet[newpos]
    print(f"The encrypted text is : {cipher_text}")
    

def decrypt(cipher_text,shift):
    plain_text=""
    for i in text:
        '''
        This is correct when we don't want to include only alphabets
         e.g zullu 
        a=ord(text[i])+shift
        texts+=chr(a)
        '''
        position=alphabet.index(i)
        newpos=position-shift
        plain_text+=alphabet[newpos]
    print(f"The encrypted text is : {plain_text}")
    



    
direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")

if(direction=="encode"):
    text=input("Type your message").lower()
    shift=int(input("Type the shift number:\n"))
    encrypt(text,shift)
    
else:
    text=input("Type your encrypted message").lower()
    shift=int(input("Type the shift number:\n"))
    decrypt(text,shift)

        
        
    
        


          
