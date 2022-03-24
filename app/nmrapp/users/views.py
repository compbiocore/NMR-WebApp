from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import StorageInsert 
from django.core.files.storage import FileSystemStorage 
from django.http import HttpResponse

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required()
def upload(request):
    return render(request, 'users/upload.html')

@login_required()
def analysis(request):
    if request.method=='POST':
        uploaded_files = request.FILES["mydata"]
        uploaded_files2 = request.FILES["myfile"]
        fs =FileSystemStorage()
        fs.save(uploaded_files.name, uploaded_files)
        fs.save(uploaded_files2.name, uploaded_files2)
        messages.success(request, 'Your files have been uploaded and are being processed!')
        return render(request, 'users/analysis.html')
    else:
        return render(request, 'users/analysis.html')

@login_required()
def Insertrecord(request):
    if request.method=='POST' and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('parameter_1') and request.POST.get('parameter_2') and request.POST.get('file_path'):
        saverecord=StorageInsert()
        saverecord.first_name=request.POST.get('first_name')
        saverecord.last_name=request.POST.get('last_name')
        saverecord.parameter_1=request.POST.get('parameter_1')
        saverecord.parameter_2=request.POST.get('parameter_2')
        saverecord.file_path=request.POST.get('file_path')
        saverecord.save()
        messages.success(request, 'Database Successfuly Updated!')
        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html')

