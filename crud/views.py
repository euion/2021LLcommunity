from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Crud, Info, Qna
from .forms import CrudUpdate, InfoUpdate, QnaUpdate

# Create your views here.
# index.html
def index(request):
    cruds = Crud.objects.order_by('-pub_date')[:5]
    infos = Info.objects.order_by('-pub_date')[:5]
    qnas = Qna.objects.order_by('-pub_date')[:5]
    content = {
        'cruds':cruds,
        'infos':infos,
        'qnas':qnas
    }
    return render(request,'index.html', content)

# 자유게시판~~
def free(request):
    cruds = Crud.objects.all().order_by('-pub_date')
    return render(request, 'free.html', {'cruds':cruds})
    
def detail(request, crud_id):
    crud_detail = get_object_or_404(Crud, pk=crud_id)
    content = {
        'crud' : crud_detail,
    }
    return render(request, 'detail.html' , content)

def new(request):
    return render(request, 'new.html')

def create(request):
    crud = Crud()
    crud.title = request.GET['title']
    crud.body = request.GET['body']
    crud.name = request.GET['name']
    crud.pub_date = timezone.datetime.now()
    crud.save()
    return redirect('/crud/' + str(crud.id))

def delete(request, crud_id):
    crud = Crud.objects.get(id=crud_id)
    crud.delete()
    return redirect('/free/')

def edit(request, crud_id):
    crud = Crud.objects.get(id=crud_id)

    if request.method =='POST':
        form = CrudUpdate(request.POST)
        if form.is_valid():
            crud.title = form.cleaned_data['title']
            crud.body = form.cleaned_data['body']
            crud.name = request.GET['name']
            crud.pub_date=timezone.now()
            crud.save()
            return redirect('/detail/' + str(crud.id))
    else:
        form = CrudUpdate(instance = crud)
 
        return render(request,'edit.html', {'form':form})

# 정보게시판~~
def infoList(request):
    infos = Info.objects.all().order_by('-pub_date')
    return render(request, 'infoList.html', {'infos':infos})

def infoDetail(request, info_id):
    info_detail = get_object_or_404(Info, pk=info_id)
    return render(request, 'infoDetail.html' , {'info' : info_detail})

def infoNew(request):
    return render(request, 'infoNew.html')

def infoCreate(request):
    info = Info()
    info.title = request.GET['title']
    info.body = request.GET['body']
    info.name = request.GET['name']
    info.pub_date = timezone.datetime.now()
    info.save()
    return redirect('/info/' + str(info.id))

def infoDelete(request, info_id):
    info = Info.objects.get(id=info_id)
    info.delete()
    return redirect('/infoList/')

def infoEdit(request, info_id):
    info = Info.objects.get(id=info_id)

    if request.method =='POST':
        form = InfoUpdate(request.POST)
        if form.is_valid():
            info.title = form.cleaned_data['title']
            info.body = form.cleaned_data['body']
            info.name = request.GET['name']
            info.pub_date=timezone.now()
            info.save()
            return redirect('/infoDetail/' + str(info.id))
    else:
        form = InfoUpdate(instance = info)
 
        return render(request,'infoEdit.html', {'form':form})

# 질문 게시판~~
def qnaList(request):
    qnas = Qna.objects.all().order_by('-pub_date')
    return render(request,'qnaList.html', {'qnas': qnas})

def qnaDetail(request, qna_id):
    qna_detail = get_object_or_404(Qna, pk=qna_id)
    return render(request, 'qnaDetail.html' , {'qna' : qna_detail})

def qnaCreate(request):
    qna = Qna()
    qna.title = request.GET['title']
    qna.body = request.GET['body']
    qna.name = request.GET['name']
    qna.pub_date = timezone.datetime.now()
    qna.save()
    return redirect('/qna/' + str(qna.id))

def qnaDelete(request, qna_id):
    qna = Qna.objects.get(id=qna_id)
    qna.delete()
    return redirect('/qnaList/')

def qnaEdit(request, qna_id):
    qna = Qna.objects.get(id=qna_id)

    if request.method =='POST':
        form = QnaUpdate(request.POST)
        if form.is_valid():
            qna.title = form.cleaned_data['title']
            qna.body = form.cleaned_data['body']
            qna.name = request.GET['name']
            qna.pub_date=timezone.now()
            qna.save()
            return redirect('/qnaDetail/' + str(qna.id))
    else:
        form = QnaUpdate(instance = qna)
 
        return render(request,'qnaEdit.html', {'form':form})
    
def qnaNew(request):
    return render(request, 'qnaNew.html')