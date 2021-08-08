import pyDes

print("Welcome to Crypto Chat's DES Encryptor/Decryptor")

data = input("Enter message to be encrypted/decrypted: ")
# print(data)
# res = bytes(data, 'utf-8')
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

choose = input("Type '1' for encryption and '2' for decrytion.")
if(choose=='1'):
    d = k.encrypt(data)
    # print(d)
    print ("Your Encrypted message is: %r" % d)
    
elif(choose=='2'):
    res = data.encode('utf-8')
    # print(str(res))
    c = res.decode('unicode-escape').encode('ISO-8859-1')
    # print(c)
    print ("Your decrypted message is: %r" % k.decrypt(c))
else:
    print("You entered the wrong option.")
    print("Thank you for using the DES Encryptor. Goodbye!")
