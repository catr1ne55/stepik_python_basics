from simplecrypt import decrypt
import codecs

with open('/home/catr1ne55/Downloads/encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

with open('/home/catr1ne55/Downloads/passwords.txt', 'rb') as p:
    passwords = [s.decode("utf-8") for s in p.read().splitlines()]
    for psw in passwords:
        try:
            print(decrypt(psw, encrypted).decode('utf-8'))
        except Exception:
            print("error")

