def encrypt_text(plaintext, c):
    ans = ""
    # iterate over the given text
    for x in range(len(plaintext)):
        ch = plaintext[x]

        # check if space is there then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) + c - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly

        else:
            ans += chr((ord(ch) + c - 97) % 26 + 97)

    return ans


plaintext = input("Enter Your Full Name : ")
c = 11
print("Plain Text Entered : " + plaintext)
print("Ceaser cipher using shift (C=P+11) : " + str(c))
print("Cipher Text is : " + encrypt_text(plaintext, c))

