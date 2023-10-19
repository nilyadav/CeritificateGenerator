from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import imp
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm #add this
from import_excel_app.models import Excel
from django.contrib import messages #import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


@login_required(login_url='user_management_app:login')
def homepage(request):
	excel = Excel.objects.all()
	return render(request,'index.html',{'excel':excel})


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            if User.objects.filter(email=email):
                error_message = 'The email is already taken. Please chose a diffrent email'
                return redirect('/signup/')
            try:
                # Your code that creates a new user
                user = User.objects.create_user(username=uname, email=email, password=pass1)
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e) and 'username' in str(e):
                    print(str(e))
                    print("aaaaaaa")
                    # Username already exists, show an error message to the user
                    error_message = 'This username is already taken. Please choose a different username.'
                messages.info(request,error_message)
                return redirect('/signup/')
            if user:
                user.save()
                messages.success(request,f"{uname} has successfully register!!!")
                return redirect('/')
        else:
            messages.info(request,"password and confrom password does'nt match!!")
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, f"{user} you have loged In successfully!" )
            return redirect('user_management_app:homepage')
        else:
            messages.error(request,f"Username or Password is incorrect!!!")
    return render (request,'signin.html')

@login_required
def LogoutPage(request):
    logout(request)
    return redirect('/')




import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


# def link_callback(uri, rel):
#         """
#         Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#         resources
#         """
#         result = finders.find(uri)
#         if result:
#                 if not isinstance(result, (list, tuple)):
#                         result = [result]
#                 result = list(os.path.realpath(path) for path in result)
#                 path=result[0]
#         else:
#                 sUrl = settings.STATIC_URL        # Typically /static/
#                 sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
#                 mUrl = settings.MEDIA_URL         # Typically /media/
#                 mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

#                 if uri.startswith(mUrl):
#                         path = os.path.join(mRoot, uri.replace(mUrl, ""))
#                 elif uri.startswith(sUrl):
#                         path = os.path.join(sRoot, uri.replace(sUrl, ""))
#                 else:
#                         return uri

#         # make sure that file exists
#         if not os.path.isfile(path):
#                 raise Exception(
#                         'media URI must start with %s or %s' % (sUrl, mUrl)
#                 )
#         return path
from django.http import HttpResponse
from django.views.generic import View
import datetime
from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('home/d.html',{
                 'pagesize':'A4',
                 'postingan_list' : data,
            })
        return HttpResponse(pdf, content_type='application/pdf')

# class GeneratePDF(View): 
#     def get(self, request, *args, **kwargs): 
#         template = get_template('invoice.html') 
#         context = { "invoice_id": 123, "customer_name": "John Cooper", "amount": 1399.99, "today": "Today", }
#         html = template.render(context) 
#         pdf = render_to_pdf('invoice.html', context) 
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf') 
#         filename = "Invoice_%s.pdf" %("12341231") 
#         content = "inline; filename='%s'" %(filename) 
#         download = request.GET.get("download") 
#         if download:
#             content = "attachment; filename='%s'" %(filename) 
#             response['Content-Disposition'] = content 
#             return response 
#         return HttpResponse("Not found")