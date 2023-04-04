import secrets
import string as s

# ! Transformar o módulo secrets no random, porém não mais pseudoaleatório
rd = secrets.SystemRandom()

senha = ''.join(rd.choices(s.ascii_letters+s.digits+s.punctuation, k=12))

print(senha)
