from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trainer
from .validator import email_validator, validate_file_extension
from django.contrib import messages
# Create your views here.
from django.db import IntegrityError


def index(request):
    return HttpResponse('hello hwo is going')


def add_instructor(request):
    if request.method == "POST":
        response1 = ""
        response2 = ""
        response3 = ""
        email = request.POST.get('email')
        optional_email = request.POST.get('optional_email')
        signature = request.POST.get('signature')
        if email:
            response1 = email_validator(email)
            if type(response1) != str:
                email = Trainer.objects.filter(email=email)
                if email:
                    print("first----- ")
                    messages.info(request,"email is already taken....")
                    return redirect('/instructor_app/add_instructor/')
                
            else:
                print("first else----- ")
                messages.info(request, response1)
                return redirect('/instructor_app/add_instructors/')
        if optional_email:
            response2 = email_validator(optional_email)
            if type(response2) != str:
                optional_email = Trainer.objects.filter(
                    optional_email=optional_email)
                if optional_email:
                    print('second-----------')
                    print("alread taken optional email ")
                    messages.info(request, response2)
                    return redirect('/instructor_app/add_instructor/')
            else:
                print("second else----- ")
                messages.info(request, response2)
                return redirect('/instructor/add_instructor/')
        if signature:
            response3 = validate_file_extension(signature)
            if type(response3) == str:
                print("thir===========")
                messages.info(request, response3)
                return redirect('/instructor_app/add_instructor/')
        print(response3,response2,response1)
        if (response1 == True) and (response2 == "" or response2 == True) and response3 == True:
            trainer_object = Trainer()
            trainer_object.T_name = request.POST['T_name']
            trainer_object.email = request.POST['email']
            trainer_object.optional_email = request.POST['optional_email']
            trainer_object.signature = request.POST['signature']
            try:
                trainer_object.save()
            except IntegrityError as e:
                messages.success(request, "This file is already taken!!!")
                return redirect('/instructor_app/add_instructor/')
            return redirect('user_management_app:homepage')
    return render(request, 'add_instructor.html')
