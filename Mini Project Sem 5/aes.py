from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
BLOCK_SIZE = 32 # Bytes

key = 'abcdefghijklmnop'
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)

print("Welcome to Crypto Chat's AES encryptor/decryptor")

data = input("Enter your message: ")

print("What do you want to do?")
choose = input("Type '1' for encryption and '2' for decryption.")

if(choose=='1'):

    res = data.encode('utf-8')
    msg = cipher.encrypt(pad(res, BLOCK_SIZE))
    print("Your Encrypted message is:")
    print(msg)
    # print('\n')
    print("Thank you for choosing Crypto Chat's AES Encryption")
    # print(msg.hex())

elif(choose=='2'):
    res = data.encode('utf-8')
    c = res.decode('unicode-escape').encode('ISO-8859-1')
    decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    msg_dec = decipher.decrypt(c)
    print("Your Decrypted message is:")
    print(unpad(msg_dec, BLOCK_SIZE))
    # print('\n')
    print("Thank you for choosing Crypto Chat's AES Encryption/Decryption")

else:
    print("You entered the wrong option.")
    print("Thank you for using the AES Encryptor. Goodbye!")

