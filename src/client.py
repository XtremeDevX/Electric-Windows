from Classes.Config import Config
from colorama import Fore
import hashlib
import socket
import sys

HOST = '127.0.0.1'
PORT = 65432

filepath = r'C:\Users\tejas\Desktop\test.electric'
configuration = Config.generate_configuration(filepath, False)
print(Fore.LIGHTGREEN_EX + 'No Syntax Errors Found!' + Fore.RESET)
str_dict = f'{configuration.dictionary}'
byte_dict = str_dict.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(Fore.LIGHTRED_EX + 'Electric Servers Are Not Responding!' + Fore.RESET)
        sys.exit()
    s.sendall(byte_dict)
    while True:
        data = s.recv(1024)
        if data:
            if not data.decode().endswith('ERROR'):
                if 'Validating Electric Packages' in data.decode():
                    print(Fore.LIGHTCYAN_EX + '↓ ' + data.decode() + '        ↓' + Fore.RESET)
                    continue
                if 'Validating Node or Npm Modules' in data.decode():
                    print(Fore.LIGHTCYAN_EX + '↓ ' + data.decode() + '      ↓' + Fore.RESET)
                    continue
                if 'Validating Python Or Pip Modules' in data.decode():
                    print(Fore.LIGHTCYAN_EX + '↓ ' + data.decode() + '    ↓' + Fore.RESET)
                    continue
                if 'Validating Editor Extensions' in data.decode():
                    print(Fore.LIGHTCYAN_EX + '↓ ' + data.decode() + '        ↓' + Fore.RESET)
                    continue
                if 'Valid Configuration, Signing Config!' in data.decode():
                    print(Fore.LIGHTGREEN_EX + data.decode() + Fore.RESET)
                    s.close()
                    break
                print(Fore.LIGHTGREEN_EX + data.decode() + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + data.decode().replace('ERROR', '') + Fore.RESET)
                s.close()
                sys.exit()

# Sign File And Exit
md5 = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
sha256_hash = hashlib.sha256()
with open(filepath,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)

sha256 = sha256_hash.hexdigest()
with open(filepath, 'r') as f:
    l = [line.strip() for line in f.readlines()]

    if '# --------------------Checksum Start-------------------------- #' in l and '# --------------------Checksum End--------------------------- #' in l:
        print(Fore.LIGHTRED_EX + f'File Already Signed, Aborting Signing!' + Fore.RESET)
        sys.exit()

with open(filepath, 'a') as f:
    f.writelines([

        '\n# --------------------Checksum Start-------------------------- #',
        '\n',
        f'# {md5}',
        '\n',
        f'# {sha256}',
        '\n',
        '# --------------------Checksum End--------------------------- #'
    ])

print(Fore.LIGHTGREEN_EX + f'Successfully Signed {filepath}.')
