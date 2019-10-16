from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def home(request):
    return render(request, 'main_app/home.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect('/')
    hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashpw)
    request.session['logged_in'] = True
    request.session['user_id'] = user.id
    return redirect('/main')

def login(request):
    print(request.POST)
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect('/')
    user = User.objects.filter(email = request.POST['email'])
    request.session['logged_in'] = True
    request.session['user_id'] = user[0].id
    print("test")
    return redirect('/main')

def main(request):
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        # 'total_likes': Quote.objects.get(id=).liked_users.all().count
    }
    return render(request, 'main_app/main.html',context)

def weight_index(request):
    return HttpResponse(render(request,'main_app/weight.html'))

def strength_index(request):
    return HttpResponse(render(request,'main_app/strength.html'))

def exercise_index(request):
    return HttpResponse(render(request,'main_app/exercise.html'))
