from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import *
from .forms import CrudUpdate, InfoUpdate, QnaUpdate
from account.models import Profile

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
    paginator = Paginator(cruds, 5) # 페이지네이션 구현
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, 'free.html', {'cruds' : posts})
    
def detail(request, crud_id):
    crud_detail = get_object_or_404(Crud, pk=crud_id)
    # ============ 댓글 불러오는 부분 ==============
    try:
        comments = CrudComment.objects.filter(crud_id=crud_id)
        try:
            comments = comments.objects.all()
        except AttributeError: # 댓글이 하나밖에 없을때 예외 처리
            pass
    except CrudComment.DoesNotExist: # 댓글이 존재하지 않을때 예외 처리
        comments = None
    # ==============================================
    content = {
        'crud' : crud_detail,
        "comments" : comments,
    }
    return render(request, 'detail.html' , content)

def new(request):
    return render(request, 'new.html')

def create(request):
    if 'name' in request.session:
        crud = Crud()
        crud.title = request.GET['title']
        crud.body = request.GET['body']
        crud.pub_date = timezone.datetime.now()

        profile_id = request.GET['profile_id']
        profile = get_object_or_404(Profile, pk=profile_id)
        crud.profile_id = profile

        crud.save()
        return redirect('/crud/' + str(crud.id))

def delete(request, crud_id):
    if 'name' in request.session:
        crud = Crud.objects.get(id=crud_id)
        crud.delete()
        return redirect('/free/')

def edit(request, crud_id):
    if 'name' in request.session:
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

def crudComment(request): # 댓글 관련 함수
    if request.method == "POST":
        if request.POST["method"] == "POST": # 댓글 생성
            pub_date = timezone.now()
            crud_id = request.POST["crud_id"]
            crud = get_object_or_404(Crud, pk=crud_id)
            profile_id = request.POST["profile_id"]
            profile = get_object_or_404(Profile, pk=profile_id)
            body = request.POST["body"]
            crud_comment = CrudComment(profile_id=profile, pub_date=pub_date, body=body, crud_id=crud)
            crud_comment.save()        
            return redirect('/crud/' + str(crud_id))
        
        # elif request.POST["method"] == "PUT":

        elif request.POST["method"] == "DELETE": # 댓글 삭제
            comment_id = request.POST["comment_id"]
            crud_id = request.POST["crud_id"]
            comment = get_object_or_404(CrudComment, pk=comment_id)
            comment.delete()
            return redirect('/crud/' + str(crud_id))        

    else: # POST 이외 방식으로 접근시 메인 화면으로 이동
        print("http 메소드:", request.method)
        return redirect("index")



# 정보게시판~~
def infoList(request):
    infos = Info.objects.all().order_by('-pub_date')
    paginator = Paginator(infos, 5) # 페이지네이션 구현
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, 'infoList.html', {'infos':posts})

def infoDetail(request, info_id):
    info_detail = get_object_or_404(Info, pk=info_id)
    # ============ 댓글 불러오는 부분 ==============
    try:
        comments = InfoComment.objects.filter(info_id=info_id)
        try:
            comments = comments.objects.all()
        except AttributeError: # 댓글이 하나밖에 없을때 예외 처리
            pass
    except InfoComment.DoesNotExist: # 댓글이 존재하지 않을때 예외 처리
        comments = None
    # ==============================================
    content = {
        'info' : info_detail,
        'comments' : comments,
    }
    return render(request, 'infoDetail.html' , content)

def infoNew(request):
    return render(request, 'infoNew.html')

def infoCreate(request):
    info = Info()
    info.title = request.GET['title']
    info.body = request.GET['body']
    
    profile_id = request.GET['profile_id']
    profile = get_object_or_404(Profile, pk=profile_id)
    info.profile_id = profile

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

def infoComment(request): 
    if request.method == "POST":
        if request.POST["method"] == "POST": # 댓글 생성
            pub_date = timezone.now()
            info_id = request.POST["info_id"]
            info = get_object_or_404(Info, pk=info_id)
            profile_id = request.POST["profile_id"]
            profile = get_object_or_404(Profile, pk=profile_id)
            body = request.POST["body"]
            info_comment = InfoComment(profile_id=profile, pub_date=pub_date, body=body, info_id=info)
            info_comment.save()        
            return redirect('/info/' + str(info.id))

        # elif request.POST["method"] == "PUT":

        elif request.POST["method"] == "DELETE": # 댓글 삭제
            comment_id = request.POST["comment_id"]
            info_id = request.POST["info_id"]
            comment = get_object_or_404(InfoComment, pk=comment_id)
            comment.delete()
            return redirect('/info/' + str(info_id))   

    else: # POST 이외 방식으로 접근시 메인 화면으로 이동
        return redirect("index")


# 질문 게시판~~
def qnaList(request):
    qnas = Qna.objects.all().order_by('-pub_date')
    paginator = Paginator(qnas, 5) # 페이지네이션 구현
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request,'qnaList.html', {'qnas': posts})

def qnaDetail(request, qna_id):
    qna_detail = get_object_or_404(Qna, pk=qna_id)
    # ========== 댓글 불러오는 부분 ==============
    try:
        comments = QnaComment.objects.filter(qna_id=qna_id)
        try:
            comments = comments.objects.all()
        except AttributeError: # 댓글이 하나 밖에 없을때 예외 처리
            pass
    except QnaComment.DoesNotExist: # 댓글이 존재하지 않을때 예외 처리
        comments = None
    # ===========================================
    content = {
        'qna' : qna_detail,
        'comments' : comments,
    }
    return render(request, 'qnaDetail.html' , content)

def qnaCreate(request):
    if 'name' in request.session:
        qna = Qna()
        qna.title = request.GET['title']
        qna.body = request.GET['body']

        profile_id = request.GET['profile_id']
        profile = get_object_or_404(Profile, pk=profile_id)
        qna.profile_id = profile

        qna.pub_date = timezone.datetime.now()
        qna.save()
        return redirect('/qna/' + str(qna.id))

def qnaDelete(request, qna_id):
    if 'name' in request.session:
        qna = Qna.objects.get(id=qna_id)
        qna.delete()
        return redirect('/qnaList/')

def qnaEdit(request, qna_id):
    if 'name' in request.session:
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

def qnaComment(request): # 댓글 생성
    if request.method == "POST":
        if request.POST["method"] == "POST": # 댓글 생성
            pub_date = timezone.now()
            qna_id = request.POST["qna_id"]
            qna = get_object_or_404(Qna, pk=qna_id)
            profile_id = request.POST["profile_id"]
            profile = get_object_or_404(Profile, pk=profile_id)
            body = request.POST["body"]
            qna_comment = QnaComment(profile_id=profile, pub_date=pub_date, body=body, qna_id=qna)
            qna_comment.save()        
            return redirect('/qna/' + str(qna_id))  

        # elif request.POST["method"] == "PUT":

        elif request.POST["method"] == "DELETE": # 댓글 삭제
            comment_id = request.POST["comment_id"]
            qna_id = request.POST["qna_id"]
            comment = get_object_or_404(QnaComment, pk=comment_id)
            comment.delete()
            return redirect('/qna/' + str(qna_id))  
        

    else: # POST 이외 방식으로 접근시 메인 화면으로 이동
        return redirect("index")