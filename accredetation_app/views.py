from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
# Create your views here.
from .models import Accriditaion
from django.contrib import messages
from trainer_app.validator import validate_file_extension
from django.db import IntegrityError
def add_accreditation(request):
    if request.method == "POST":
        name_of_accreditation = request.POST.get('name_of_accreditation')
        expiry_date = request.POST.get('expiry_date')
        accreditation_logo = request.POST.get('accreditation_logo')
        print(expiry_date,"-------------------")
        if accreditation_logo:
            response3 = validate_file_extension(accreditation_logo)
            if type(response3) == str:
                messages.info(request, response3)
                return redirect('/accreditation_app/add_accreditation/')
        try:
            trainer_object = Accriditaion()
            trainer_object.name_of_accreditation = name_of_accreditation
            trainer_object.expiry_date = expiry_date
            trainer_object.accreditation_logo  = accreditation_logo
            trainer_object.save()
            messages.success(request,"add accreditation successfully!!!")
            return redirect('user_management_app:homepage')
        except IntegrityError as e:
            messages.success(request, "This file is already taken!!!")
            return redirect('/accreditation_app/add_accreditaion/')
    return render(request,'add_accreditation.html',{'expiry_date':request.GET.get('expiry_date')})
    