import zipfile


def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        # print('wrong password!')
        return


def main():
    zfile = zipfile.ZipFile('file.zip')     # 'file.zip' - the file we try to extract.
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess: # if not None
            print("Password = {}".format(password))
            break


if __name__ == "__main__":
    main()