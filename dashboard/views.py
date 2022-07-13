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

def indexSmt(request):
    template = loader.get_template('dashboard/index_smt.html')
    return HttpResponse(template.render({}, request))

def indexCba(request):
    template = loader.get_template('dashboard/index_cba.html')
    return HttpResponse(template.render({}, request))

def indexFa(request):
    template = loader.get_template('dashboard/index_fa.html')
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

@login_required(login_url='/login/')
def uploadImgSmt(request):
    if request.method == 'POST':
        if request.FILES.get('upload1'):
            upload = request.FILES.get('upload1')
            name = 'smt/1.jpg'
        elif request.FILES.get('upload2'):
            upload = request.FILES.get('upload2')
            name = 'smt/2.jpg'
        elif request.FILES.get('upload3'):
            upload = request.FILES.get('upload3')
            name = 'smt/3.jpg'
        elif request.FILES.get('upload4'):
            upload = request.FILES.get('upload4')
            name = 'smt/4.jpg'
        elif request.FILES.get('upload5'):
            upload = request.FILES.get('upload5')
            name = 'smt/5.jpg'
        elif request.FILES.get('upload6'):
            upload = request.FILES.get('upload6')
            name = 'smt/6.jpg'
        fss = FileSystemStorage()
        file_rm = fss.delete(name)
        file = fss.save(name, upload)
        file_url = fss.url(file)
        return render(request, 'dashboard/upload_smt.html', {'file_url': file_url})
    template = loader.get_template('dashboard/upload_smt.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='/login/')
def uploadImgCba(request):
    if request.method == 'POST':
        if request.FILES.get('upload1'):
            upload = request.FILES.get('upload1')
            name = 'cba/1.jpg'
        elif request.FILES.get('upload2'):
            upload = request.FILES.get('upload2')
            name = 'cba/2.jpg'
        elif request.FILES.get('upload3'):
            upload = request.FILES.get('upload3')
            name = 'cba/3.jpg'
        elif request.FILES.get('upload4'):
            upload = request.FILES.get('upload4')
            name = 'cba/4.jpg'
        elif request.FILES.get('upload5'):
            upload = request.FILES.get('upload5')
            name = 'cba/5.jpg'
        elif request.FILES.get('upload6'):
            upload = request.FILES.get('upload6')
            name = 'cba/6.jpg'
        fss = FileSystemStorage()
        file_rm = fss.delete(name)
        file = fss.save(name, upload)
        file_url = fss.url(file)
        return render(request, 'dashboard/upload_cba.html', {'file_url': file_url})
    template = loader.get_template('dashboard/upload_cba.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='/login/')
def uploadImgFa(request):
    if request.method == 'POST':
        if request.FILES.get('upload1'):
            upload = request.FILES.get('upload1')
            name = 'fa/1.jpg'
        elif request.FILES.get('upload2'):
            upload = request.FILES.get('upload2')
            name = 'fa/2.jpg'
        elif request.FILES.get('upload3'):
            upload = request.FILES.get('upload3')
            name = 'fa/3.jpg'
        elif request.FILES.get('upload4'):
            upload = request.FILES.get('upload4')
            name = 'fa/4.jpg'
        elif request.FILES.get('upload5'):
            upload = request.FILES.get('upload5')
            name = 'fa/5.jpg'
        elif request.FILES.get('upload6'):
            upload = request.FILES.get('upload6')
            name = 'fa/6.jpg'
        fss = FileSystemStorage()
        file_rm = fss.delete(name)
        file = fss.save(name, upload)
        file_url = fss.url(file)
        return render(request, 'dashboard/upload_fa.html', {'file_url': file_url})
    template = loader.get_template('dashboard/upload_fa.html')
    return HttpResponse(template.render({}, request))


def logout(request):
    return redirect('../../dashboard/')