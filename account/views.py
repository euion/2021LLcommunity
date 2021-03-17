from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def login(request):
    if not request.session.get('name'):
        if request.method == "POST":
            student_ID = request.POST.get('user_id', None)
            password = request.POST.get('password', None)
            
            res_data = {}
            if not student_ID and password:
                res_data['error'] = '모든 값을 입력하세요!'
            
            else:
                member_profile = Profile.objects.filter(user_id=student_ID)
                # print(member_profile[0])
                
                if check_password(password, member_profile[0].user_PW):
                    # session!
                    request.session['name'] = member_profile[0].name
                    request.session['profile_id'] = member_profile[0].id
                    request.session['user_id'] = member_profile[0].user_id
                    
                    # redirect!
                    return redirect('/')
                    
                else:
                    res_data['error'] = '비밀번호가 다릅니다!'
                
            return render(request, 'login.html', res_data)
        
        else:
            return render(request, 'login.html')
    else:
        return redirect('/')

def logout(request):
    if 'name' in request.session:
        request.session.clear()
    return redirect('/')

def signup(request):
    if request.method == "POST":
        #User 객체
        name = request.POST.get('name', None)
        user_id = request.POST.get('user_id', None)
        student_ID = request.POST.get('student_ID', None)
        major = request.POST.get('major', None)
        age = request.POST.get('age', None)
        term = request.POST.get('term', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        print(student_ID)
        res_data = {}
        if not (name and student_ID and password):
            res_data['error'] = '모든 값을 입력하세요'
            print(res_data['error'])

            return render(request, 'signup.html', res_data)

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            
            return render(request, 'signup.html', res_data)
        
        admin = 0

        profile = Profile(
            name = name,
            user_id = user_id,
            student_Number = student_ID,
            user_PW = make_password(password),
            major = major,
            age = age,
            term = term,
            admin = admin
        )
            
        profile.save()
                
        return redirect('/account/login')
    
    else:
        return render(request, 'signup.html')