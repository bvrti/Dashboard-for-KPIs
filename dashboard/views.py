from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    template = loader.get_template('dashboard/index.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='/login/')
def uploadImg(request):
    if request.method == 'POST':
        if request.FILES.get('upload1'):
            upload = request.FILES.get('upload1')
            name = '1.jpg'
        elif request.FILES.get('upload2'):
            upload = request.FILES.get('upload2')
            name = '2.jpg'
        elif request.FILES.get('upload3'):
            upload = request.FILES.get('upload3')
            name = '3.jpg'
        elif request.FILES.get('upload4'):
            upload = request.FILES.get('upload4')
            name = '4.jpg'
        elif request.FILES.get('upload5'):
            upload = request.FILES.get('upload5')
            name = '5.jpg'
        elif request.FILES.get('upload6'):
            upload = request.FILES.get('upload6')
            name = '6.jpg'
        fss = FileSystemStorage()
        file_rm = fss.delete(name)
        file = fss.save(name, upload)
        file_url = fss.url(file)
        return render(request, 'dashboard/upload.html', {'file_url': file_url})
    template = loader.get_template('dashboard/upload.html')
    return HttpResponse(template.render({}, request))

def logout(request):
    return redirect('../../dashboard/')