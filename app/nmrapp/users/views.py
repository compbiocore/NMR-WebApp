from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import StorageInsert 
from django.core.files.storage import FileSystemStorage 
from django.http import HttpResponse
#from .models import Credentials 
import os 
#from django.http import FileResponse
#from django.http import Http404
import time
import glob
from wsgiref.util import FileWrapper
import mimetypes
from django.utils.encoding import smart_str
from django.contrib.messages import get_messages

# Navigates user to home page 
def home(request):
    return render(request, 'users/home.html')

# Handles registration and storage of user credentials 
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if not os.path.exists(os.path.join('/app/myusers', form.cleaned_data.get('username'))):
                os.makedirs(os.path.join('/app/myusers', form.cleaned_data.get('username')))
                os.makedirs(os.path.join('/app/myusers/', form.cleaned_data.get('username'),'/nmr_web_analyses'))
                os.makedirs(os.path.join('/app/myusers/', form.cleaned_data.get('username'),'/user_uploaded'))
            username = form.cleaned_data.get('username')
            #userrecord=Credentials()
            #userrecord.user=username
            #userrecord.pword=form.cleaned_data.get('password1')
            #userrecord.save()
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# Displays profile information to user when they navigate to profile page 
@login_required()
def profile(request):
    path = f"/app/myusers/{request.user.username}/user_uploaded/"
    if len(os.listdir(path)) > 0:
        files_list =os.listdir(path)
    else:
        files_list=["No files have been uploaded by this user yet"]
    return render(request, 'users/profile.html', {'userFiles': files_list})

# Renders the upload page for the user 
@login_required()
def upload(request):
    return render(request, 'users/upload.html')

# Handles the analysis and storage of nmr data 
@login_required()
def analysis(request):
    if request.method=='POST':
        os.makedirs(os.path.join('/app/tmp', request.user.username))
        uploaded_files = request.FILES["mydata"]
        uploaded_files2 = request.FILES["myfile"]
        fs =FileSystemStorage()
        fs.save(uploaded_files.name, uploaded_files)
        fs.save(uploaded_files2.name, uploaded_files2)
        #messages.success(request, 'Your files have been uploaded and are being processed!')
        #return render(request, 'users/analysis.html')
        # This makes sure you return the latest file 
        while len(os.listdir('/app/tmp')) > 0:
            time.sleep(1)
        #messages.success(request, 'Your files have been analyzed and are ready for download!')
        return download_file(request)
    else:
        return render(request, 'users/analysis.html')

# Handles file uploads 
@login_required()
def Insertrecord(request):
    if request.method=='POST' and request.POST.get('user_name') and request.FILES['file_upload']: 
        saverecord=StorageInsert()
        saverecord.user_name=request.POST.get('user_name')
        #saverecord.first_name=request.POST.get('first_name')
        #saverecord.last_name=request.POST.get('last_name')
        saverecord.folder=request.FILES['file_upload']
        saverecord.save()
        messages.success(request, 'Database Successfuly Updated!')
        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html')
    
# Handles file downloads after data are analyzed 
# if you want files to be accessible only to owners 
# you probably should force user to login before download
@login_required()
def download_file(request):
    dirName = f"/app/myusers/{request.user.username}/nmr_web_analyses" 
    if len(os.listdir(dirName)) > 0:
        list_of_files = glob.glob(dirName+'/*.zip') # * means all if need specific format then *.csv
        zipFile = max(list_of_files, key=os.path.getmtime)
        # somewhere here you need to check if user has access to the file
        # if files ownership based solely on {user_name} dir in filesystem
        # then it is enough to check if file exists  
        response = HttpResponse(open(zipFile, 'rb'), content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename=download.zip'
        return response
    else:
        return render(request, 'users/analysis.html')

# Serve users their stored data 
@login_required()
def serve_file(request):
    if request.method=='POST' and request.POST.get('filename'):
        file_to_retrieve=request.POST.get('filename')
        dirUpload = f"/app/myusers/{request.user.username}/user_uploaded/"
        if os.path.isfile(dirUpload + file_to_retrieve):
            file_path = dirUpload + file_to_retrieve
            file_wrapper = FileWrapper(open(file_path,'rb'))
            file_mimetype = mimetypes.guess_type(file_path)
            response = HttpResponse(file_wrapper, content_type=file_mimetype )
            response['X-Sendfile'] = file_path
            response['Content-Length'] = os.stat(file_path).st_size
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_to_retrieve) 
            #zip_file = open(dirUpload, 'rb')
            #return FileResponse(zip_file)
            return response
        else: 
            messages.error(request, 'File Does Not Exist!')
            return render(request, 'users/retrieve.html')
    return render(request, 'users/retrieve.html')
    

    #else:
        #return render(request, 'users/retrieve.html')  

        