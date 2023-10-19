from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from tablib import Dataset
from import_excel_app.models import Excel
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Q
from trainer_app.models import Trainer
from accredetation_app.models import Accriditaion
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .servisse import read_data_from_excel
from django.shortcuts import get_object_or_404
from urllib.request import urlopen
import requests

from accredetation_app.models import filter_by_expiry_date
from trainer_app.models import filter_by_trainer_name

from django.http import HttpResponseRedirect
from django.urls import reverse
# @login_required(login_url='user_management_app:login')
# def import_excel(request):
#     if request.user.is_superuser:  
#         if request.method == "POST":
#             dataset = Dataset()
#             new_data = request.FILES['my_file']
#             if not new_data.name.endswith('xls'):
#                 messages.info(request, 'wrong formate')
#                 return render(request, 'excel/upload_excel.html')
#             imported_data = dataset.load(new_data.read(), format='xls')
#             ID_No_obj = Excel.objects.all().values('ID_No')
#             list_of_ids = []
#             if not ID_No_obj:
#                 print("no data=--------------")
#                 for data in imported_data:
#                     accredetation_obj = Accriditaion.objects.filter(expiry_date__exact = data[6])
#                     trainer_obj = Trainer.objects.filter(T_name__exact = data[7])
#                     if  not trainer_obj:
#                         print("-------------trainer")
#                         return redirect('trainer_app:add_instructor')
                        
#                     elif not accredetation_obj:
#                         print("---------------------accredetation")
#                         return redirect('accredetation_app:add_accreditaion') 
#                     read_data_from_excel(data,accredetation_obj,trainer_obj)
#             else:

#                 for kwargs in ID_No_obj:
#                     list_of_ids.append(kwargs['ID_No'])
#                 for data in imported_data:
#                     print(data[6])
#                     print(data[7])
#                     accredetation_obj = Accriditaion.objects.get(expiry_date__exact = data[6])
#                     trainer_obj = Trainer.objects.get(T_name__exact = data[7])
#                     print(accredetation_obj.id,trainer_obj.id,'---------------------------------------------')
#                     if str(data[0]) in list_of_ids:
#                         print("this data is exist---------")
#                         continue

#                     else:
#                         if  not trainer_obj:
#                             print("-------------trainer")
#                             print("hello world")
#                             return redirect('trainer_app:add_instructor')
                        
#                         elif not accredetation_obj:
#                             print("---------------------accredetation")
#                             return redirect('accredetation_app:add_accreditaion') 
#                         read_data_from_excel(data,int(trainer_obj.id),int(accredetation_obj.id))
#             messages.success(request,"uploaded successfully!!!")
#             return redirect('user_management_app:homepage')
#     return render(request, 'upload_excel.html')

@login_required(login_url='user_management_app:login')
def import_excel(request):
    if request.user.is_superuser:  
        if request.method == "POST":
            dataset = Dataset()
            new_data = request.FILES['my_file']
            if not new_data.name.endswith('xls'):
                messages.info(request, 'wrong formate')
                return render(request, 'upload_excel.html')
            imported_data = dataset.load(new_data.read(), format='xls')
            exist_object = Excel.objects.first()
            if not exist_object:
                for data in imported_data:
                    data = list(data)
                    accredetation_obj_id = filter_by_expiry_date(data[6])
                    print(accredetation_obj_id)
                    trainer_obj_id = filter_by_trainer_name(data[7])
                    print(trainer_obj_id)
                    if not accredetation_obj_id:
                        return redirect('accredetation_app:add_accreditaion') 
                        # url = reverse('accredetation_app:add_accreditaion')
                        # url_with_params = url + '?expiry_date={}'.format(data[6])
                        # return HttpResponseRedirect(url_with_params)
                        # # return redirect('accredetation_app:add_accreditaion',context) 
                    elif  not trainer_obj_id:
                        return redirect('trainer_app:add_instructor')
                    else:
                        data.append(accredetation_obj_id)
                        data.append(trainer_obj_id)
                        read_data_from_excel(data)
            else:
                for data in imported_data:
                    if not Excel.objects.filter(ID_No=data[0]).exists():
                        trainer_obj_id = filter_by_trainer_name(data[7])
                        accredetation_obj_id = filter_by_expiry_date(data[6])
                        if not accredetation_obj_id:
                            return redirect('accredetation_app:add_accreditaion') 
                        elif  not trainer_obj_id:
                            return redirect('trainer_app:add_instructor')
                        else:
                            data[8] = trainer_obj_id
                            data[9] = accredetation_obj_id
                            read_data_from_excel(data)
            messages.success(request,"uploaded successfully!!!")
            return redirect('user_management_app:homepage')
    return render(request, 'upload_excel.html')

@login_required(login_url='user_management_app:login')
def update_specific_delegates(request, id):
    try:
        excel = Excel.objects.get(id=id)
    except Excel.DoesNotExist:
        excel = None
    if request.method == "POST":
        excel.ID_No = request.POST['ID_No']
        excel.Name_Of_Delegates = request.POST['Name_Of_Delegates']
        excel.Certificate_No = request.POST['Certificate_No']
        excel.Course = request.POST['Course']
        excel.Company = request.POST['Company']
        excel.Instructor = request.POST['Instructor']
        excel.save()
        messages.success(request,"updated successfully")
        return redirect('user_management_app:homepage')
    else:
        return render(request, 'update_data.html', {'excel': excel})


@login_required(login_url='user_management_app:login')
def checked_delegates(request):
    if 'DeleteChecked' in request.GET.get('submit'):
        # excel = Excel.objects.all()
        if request.method == 'GET':
            if 'checklist' in request.GET:
                check_list = request.GET.getlist('checklist')
                Excel.objects.filter(id__in=check_list).delete()
                messages.success(request,"deleted successfully!!!")
            else:
                messages.success(request,"please first checked some delegates!!!")
        return render(request, 'index.html', {'excel': excel})
    elif 'DownloadChecked' in request.GET.get('submit'):
        if 'checklist' in request.GET:
            checked_list = request.GET.getlist('checklist')
            print(checked_list)
            excel = Excel.objects.filter(id__in=checked_list)
            template_path = 'home/d.html'
            response = HttpResponse(content_type="application/pdf")
            response['Content-Disposition'] = 'filename="certificate.pdf"'
            template = get_template(template_path)
            html = template.render({'home': None})
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('we had some errors <pre>' + html + '</pre>')
            messages.success(request,'generate pdf successfully!!!')
            for item in excel:
                item.pdf_url = request.build_absolute_uri(reverse('pdf_file', args=[item.id]))
                item.save()
            return response
        else:
            messages.success(request,'please checked some delegates!!!')
    return redirect(reverse("user_management_app:homepage"))

@login_required(login_url='user_management_app:login')
def serve_pdf(request, id):
    pdf_file = Excel.objects.get(id=id)
    pdf_content = requests.get(pdf_file.pdf_url).content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="/hello/{pdf_file.id}.pdf"'
    return response

@login_required(login_url='user_management_app:login')
def search_result(request):
    if request.method == "GET":
        if 'search' in request.GET:
            params = request.GET.get('search')
            query = (Q(Name_Of_Delegates__icontains=params) | Q(
                Course__icontains=params) | Q(Instructor__icontains=params))
            excel = Excel.objects.filter(query)
            if excel:
                return render(request, 'index.html', {'excel': excel})
        excel = Excel.objects.all()
        return render(request, 'index.html', {'excel': excel})


def error_404(request, exception):
    return render(request, 'not_found.html')



