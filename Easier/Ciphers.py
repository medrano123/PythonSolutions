#  File: Ciphers.py
#  Description: The purpose of this assignment is to demonstrate my knowledge
#  of arrays, by creating a subtistution cipher that takes a list of messages
#  along with a key, and then the program should interchange each character
#  in relation to its spot in the 1-26 alphabet index. Then print that, and do
#  the inverse to recieve back the original phrase, and then print that out.
#  Student's Name: Giovanni Medrano


def main():
    
    plaintextMessages = [
        ["This is the plaintext message.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Let the Wookiee win!",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["I used to think I was indecisive, but now I'm not too sure.",
         "mqncdaigyhkxflujzervptobws"],
        ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
         "bludcmhojaifxrkzenpsgqtywv"] ]

    codedMessages = [
        ["Uijt jt uif dpefe nfttbhf.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
         "mqncdaigyhkxflujzervptobws"] ]
#  Creates the loop that goes through each list and using the key translates
#  to the new output.

    for i in range(len(plaintextMessages)):
        plaintext = plaintextMessages[i][0]
        key = plaintextMessages[i][1]
        ciphertext = encode(key, plaintext)
        print('plaintext: ' + plaintext)
        print('encoded: ' + ciphertext)
        print('re-decoded: ' + decode(key, ciphertext))
        print()
        
#  Does the inverse in order to achieve the original text back using the opposite
#  of above.

    for i in range(len(codedMessages)):
        ciphertext = codedMessages[i][0]
        key = codedMessages[i][1]
        plaintext = decode(key,ciphertext)
        print('encoded: ' + ciphertext)
        print('decoded: ' + plaintext)
        print()


#  The first step is to find the proper transformation between the original
#  to the encrypted key, and this is done by looking at the hex number
#  of the character and manipulating it.

def encode(key, plaintextMessages):
    ciphertext = ''
    for i in plaintextMessages:
        if ( i <= 'z' and i >= 'a'):
            new_Index = ord(i) - ord('a')
            i = key[new_Index]
        elif ( i <= 'Z' and i >= 'A'):
            new_Index = ord(i) - ord('A')
            i = key[new_Index]
            i = chr(ord(i) - ord('a') + ord('A'))
        ciphertext += i
    return ciphertext

#  Does the inverse of the operation above in order to recieve the original
#  text back.
def decode(key, ciphertext):
    plaintext = ''
    for i in ciphertext:
        if i.isalpha():
            original_Index = key.index(i.lower())
            if ( i <= 'z' and i >= 'a'):
                i = chr(ord('a') + original_Index)
            elif ( i <= 'Z' and i >= 'A'):
                i = chr(ord('A') + original_Index)
        plaintext = plaintext + i
    return plaintext

main()
