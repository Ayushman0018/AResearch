from django.shortcuts import render, redirect
from app1.models import *
from mailjet_rest import Client
import random
mail_key = "7a058ff7cfa626c9d7468adc04c97872"
mail_secret = "47c90d8b45e19132042e46733c44f292"
# exchange_rates = stripe.ExchangeRate.list()
mailjet = Client(auth=(mail_key,mail_secret), version='v3.1')
# Create your views here.
def home(request):
    context = {}
    if 'email' in request.session.keys():
        context['username'] = request.session['username']
    return render(request, 'index.html', context = context)

def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        if user.objects.filter(email=email).exists():
            person = user.objects.filter(email=email).first()
            if person.active == "TRUE":
                if person.psw == psw:
                    request.session['email'] = person.email
                    request.session['username'] = person.username
                    request.session['logged'] = True
                    return redirect('home')
                else:
                    context['result'] = "Incorrect Password"
            else:
                return redirect('otp')
        else:
            context['result'] = "Account not found."
    return render(request, 'login.html', context=context)

def signup(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        psw2 = request.POST.get('psw2')
        username = request.POST.get('username')
        if psw == psw2:
            a = user(email=email, psw=psw, username=username)
            a.save()
            request.session['email'] = a.email
            return redirect('otp')
        else:
            context['result'] = "Passwords do not match."
    return render(request, 'signup.html', context=context)

def otp(request):
    if not 'email' in request.session.keys():
        return redirect('login')
    email = request.session['email']
    person = user.objects.filter(email=email).first()
    context = {'email':email}
    if request.method == "POST":
        otp_code = request.POST.get('otp')
        print(otp_code, person.otp)
        if str(otp_code) == str(person.otp):
            person.active = "TRUE"
            request.session['email'] = person.email
            request.session['username'] = person.username
            person.save()
            return redirect('home')
        else:
            context['result'] = "Invalid OTP, please try again."
    else:
        person.otp = random.randint(100000, 999999)
        person.save()
        data = {
        'Messages': [
            {
            "From": {
                "Email": "ayushmanrajora44@gmail.com",
                "Name": "ANEOR"
            },
            "To": [
                {
                "Email": person.email,
                "Name": person.username
                }
            ],
            "Subject": "One Time Password for Asteroid (NEO) Research",
            "TextPart": f"Hi {person.username}, your One Time Password for logging in to ANEOR is: {person.otp}. Please do no share it with anyone else.",
            }
        ]
        }

        # Send the email
        result = mailjet.send.create(data=data)
    return render(request, "otp.html", context=context)