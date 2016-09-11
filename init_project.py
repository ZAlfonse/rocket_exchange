import random

SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

secret = file('env', 'w')
secret.write('SECRET_KEY=' + SECRET_KEY)
secret.close()
