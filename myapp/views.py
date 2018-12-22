from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib import admin,auth
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver
from django.contrib.auth import login,authenticate
from .models import UserProfile,Event,UserToken,Registration
import random

# Create your views here.
def home(request):
        if request.user.is_authenticated:
                events=Event.objects.all()
                u=UserProfile.objects.get(user=request.user)
                coin=u.coins
                args={'events':events,'coin':coin}
                return render(request,'myapp/events.html',args)
        events=Event.objects.all()
        args={'events':events}
        return render(request,'myapp/events.html',args)

def register(request):
    if request.method == 'POST':
        name=request.POST.get('id_name')
        username=request.POST.get('id_username')
        password1=request.POST.get('id_password1')
        branch=request.POST.get('id_branch')
        email=request.POST.get('id_email')
        phone=request.POST.get('id_phone')
        print('Something')
        if User.objects.filter(username=username).count()!=0:
                return HttpResponse('User Already Exist')
        user = User.objects.create_user(username=username, password=password1, email=email,)
        user.save()
        login(request,user)
        y=UserProfile.objects.get(user=request.user)
        y.name=name
        y.phone=phone
        y.branch=branch
        y.save()
        print('Registetred')
        return HttpResponse('Success')

def loginu(request):
        username=request.POST.get('username')
        password=request.POST.get('id_password')
        
        print('initiated')
        user=authenticate(username=username,password=password)
        if user is None:
                return HttpResponse('Wrong')
        print(user)
        login(request,user)
        return HttpResponse('Success')


def logout(request):
    auth.logout(request)
    return redirect('/')

def eventregister(request):
        team_name=request.POST.get('team_name')
        event=request.POST.get('event')
        print(team_name,event)
        if event == '-------':
                return HttpResponse('Wrong')
        x=random.randint(999,99999)*67
        events=Event.objects.all()
        regi=UserToken.objects.get(user=request.user)
        if event=='event1':
                regi.event1=x
        if event=='event2':
                regi.event2=x
        if event=='event3':
                regi.event3=x
        if event=='event4':
                regi.event4=x
        if event=='event5':
                regi.event5=x
        if event=='event6':
                regi.event6=x
        if event=='event7':
                regi.event7=x
        if event=='event8':
                regi.event8=x
        if event=='event9':
                regi.event9=x
        if event=='event10':
                regi.event10=x
        if event=='event11':
                regi.event11=x
        if event=='event12':
                regi.event12=x
        if event=='event13':
                regi.event13=x
        if event=='event14':
                regi.event14=x
        
        regi.save()
        Registration.objects.create(event=event,team_name=team_name,user=request.user,token=x)
        return HttpResponse('Success')

def verify(request):
        event=request.POST.get('event')
        coupon=request.POST.get('coupon')
        print(coupon)
        if event=='1':
                x=request.user.usertoken.event1
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=500+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event1='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='2':
                x=request.user.usertoken.event2
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=500+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event2='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='3':
                x=request.user.usertoken.event3
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=500+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event3='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='4':
                x=request.user.usertoken.event4
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=500+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event4='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')