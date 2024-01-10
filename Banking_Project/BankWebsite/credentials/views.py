from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid User")
            return redirect('register')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "Registration Successful. Please Enter Your Details.")
                return redirect('details')
        else:
            messages.info(request, "Password not Matching")

        return redirect('register')

    return render(request, "register.html")


def details(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']
        materials_provide = request.POST.getlist('materials_provide')

        messages.success(request, 'Application Accepted')
        return redirect('/')

    return render(request, 'details.html')
