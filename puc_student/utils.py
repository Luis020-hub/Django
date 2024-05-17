from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

usuarios = ['admin', 'luis', 'professor']
senhas = ['123', '123456', '12345678']

for username, password in zip(usuarios, senhas):
    user = User.objects.get(username=username)
    user.password = make_password(password)
    user.save()
