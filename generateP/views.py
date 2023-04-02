from django.shortcuts import render
import random

def home(request):
    return render(request,'generate/home.html')


def password(request):
    
    character =  list('abcdefghijklmnñopqrstuvwxyz')
    generate_password = ''
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        character.extend(list('abcdefghijklmnñopqrstuvwxyz'.upper()))

    if request.GET.get('especial'):
        character.extend(list('^!"#$%&/()=?¡¿¨´´*+[{-_;:}]'))

    if request.GET.get('numbers'):
        character.extend(list('123456789'))

    for _ in range(length):
        generate_password += random.choice(character)
    return render(request,'generate/password.html',{'password':generate_password})