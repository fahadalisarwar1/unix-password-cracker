import crypt

def test_password(crypted_password, dictionaryName):
    salt = crypted_password[:2]
    with open(dictionaryName, "r") as file:
        for word in file.readlines():
            word = word.strip('\n')
            cryptWord = crypt.crypt(word, salt)
            if cryptWord == crypted_password:
                print("[+] Found password : "+word + "\n")
                return
    print("[+] Couldn't crack password ")
    return


if __name__ == "__main__":
    print("[+] Cracking UNIX password")
    passFile = open("passwords.txt", "r")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            encrypted_pass = line.split(":")[1].strip(" ")
            print("[+] cracking password for ", user)
            test_password(encrypted_pass, "dictionary.txt")


    