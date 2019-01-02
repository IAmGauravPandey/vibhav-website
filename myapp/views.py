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
from .models import UserProfile,Event,UserToken,Registration,EventRules
import random
import itertools

if(Event.objects.all().count() == 0):
        for i in range(14):
                name='event'+str(i)
                Event.objects.create(name=name)

# Create your views here.
def home(request):
        eventa=Event.objects.all()
        events=[]
        for ev in eventa:
                events.append(ev.name)
                print(ev.eventrules.about)
        print(events)
        if request.user.is_authenticated:
                
                u=UserProfile.objects.get(user=request.user)
                t=UserToken.objects.get(user=request.user)
                tokens=[]
                tokens.append(t.event1),tokens.append(t.event2),tokens.append(t.event3),tokens.append(t.event4),tokens.append(t.event5),tokens.append(t.event6),tokens.append(t.event7)
                tokens.append(t.event8),tokens.append(t.event9),tokens.append(t.event10),tokens.append(t.event11),tokens.append(t.event12),tokens.append(t.event13),tokens.append(t.event14)
                print(tokens)
                coin=u.coins
                mylist=zip(events,tokens,eventa)
                args={'coin':coin,'mylist':mylist}
                return render(request,'myapp/events.html',args)
        tokens=[5,5,5,5,5,5,5,5,5,5,5,5,5,5]
        mylist=zip(events,tokens,eventa)
        args={'mylist':mylist}
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
        if event=='Event1':
                regi.event1=x
        if event=='Event2':
                regi.event2=x
        if event=='Event3':
                regi.event3=x
        if event=='Event4':
                regi.event4=x
        if event=='Event5':
                regi.event5=x
        if event=='Event6':
                regi.event6=x
        if event=='Event7':
                regi.event7=x
        if event=='Event8':
                regi.event8=x
        if event=='Event9':
                regi.event9=x
        if event=='Event10':
                regi.event10=x
        if event=='Event11':
                regi.event11=x
        if event=='Event12':
                regi.event12=x
        if event=='Event13':
                regi.event13=x
        if event=='Event14':
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
                        y.coins=z+100
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
                        y.coins=z+100
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
                        y.coins=z+100
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
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event4='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='5':
                x=request.user.usertoken.event5
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event5='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='6':
                x=request.user.usertoken.event6
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event6='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='7':
                x=request.user.usertoken.event7
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event7='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='8':
                x=request.user.usertoken.event8
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event8='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='9':
                x=request.user.usertoken.event9
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event9='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='10':
                x=request.user.usertoken.event10
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event10='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='11':
                x=request.user.usertoken.event11
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event11='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='12':
                x=request.user.usertoken.event12
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event12='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='13':
                x=request.user.usertoken.event13
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event13='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        if event=='14':
                x=request.user.usertoken.event14
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.event14='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')