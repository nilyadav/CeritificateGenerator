import re
import os
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import trainer_app.models
def email_validator(email):
    if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$",email):
        return f"{email} is not write formate supported"
    return True
    

def validate_file_extension(value):
    ext = os.path.splitext(value)[1]  # [0] returns path+filename
    # valid_extensions = ['.pdf', '.doc', '.docx',
    #                     '.jpg', '.png', '.xlsx', '.xls']
    print("ext",ext)
    valid_extensions = ['.jpg', '.png','.avif']
    if not ext.lower() in valid_extensions:
        return f"File Extension is not valid"
    return True
        
