#Importando bibliotecas
import cryptocode
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import rsa


#Recebendo a chave
chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

#Perguntando a senha
senha = "teste"#input("Digite a senha: ")

#Criptografia 1, simétrica com cryptocode, usando String e um arranjo aleatório de bytes

msg_1 = cryptocode.encrypt(senha, chave)
print("Primeiro método: ")
print("Criptografado: ",msg_1)
print("Descriptografado: ",cryptocode.decrypt(msg_1, chave))

#Criptografia 2, simétrica com Fernet, usando bytes

#Criando variável em bytes para ser utilizada
bytes = os.urandom(16)
hash_alg = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=bytes,
    iterations=390000,
)
#Transformando String em Bytes
msg_enc = senha.encode()
key = base64.urlsafe_b64encode(hash_alg.derive(chave.encode()))
f = Fernet(key)
msg_2 = f.encrypt(msg_enc)

print("----------------------------------------------------------------------------")
print("Segundo método: ")
print("Criptografado: ",msg_2.decode())
print("Descriptografado: ",f.decrypt(msg_2).decode())


#Criptografia 3, combinando as duas criptografias anteriores, criando camada de proteção

hash_alg2 = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=bytes,
    iterations=390000,
)

#Encodando e encryptando a primeira mensagem encriptada com o segundo método e a utilizando como chave
key2 = base64.urlsafe_b64encode(hash_alg2.derive(msg_1.encode()))
f2 = Fernet(key2)
msg_3 = f2.encrypt(senha.encode())

print("----------------------------------------------------------------------------")
print("Terceiro método: ")
print("Criptografado 1: ",msg_3.decode())

#Encryptando a chave que ja foi encryptada, novamente
msg_3 = cryptocode.encrypt(str(msg_3.decode()), chave)

print("Criptografado 2: ",msg_3)

#Descriptografando nas duas camadas, com os 2 métodos
#Utilizando cryptocode
msg_3 = cryptocode.decrypt(str(msg_3), chave)
#Utilizando o objeto Fernet (f2)
msg_3 = f2.decrypt(msg_3).decode()

print("Descriptografado: ",msg_3)

