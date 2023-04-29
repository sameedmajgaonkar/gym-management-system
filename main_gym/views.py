from gym_management_website import settings
import socket
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Enquiry, Equipment, Plan, Member, Email
from django.core.mail import send_mass_mail
from .forms import EmailForm
# Create your views here.


def home(request):
    return render(request, 'main_gym/home.html')


def gallery(request):
    return render(request, 'main_gym/gallery.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main_gym/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main_gym/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(
                name=n, contact=c, emailid=e, age=a, gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'main_gym/add_enquiry.html', d)


def View_Enquiry(request):
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'main_gym/view_enquiry.html', d)


def Delete_Enquiry(request, pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        desc = request.POST['desc']
        try:
            Equipment.objects.create(
                name=n, price=p, unit=u, date=d, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'main_gym/add_equipment.html', d)


def View_Equipment(request):
    equ = Equipment.objects.all()
    d = {'equ': equ}
    return render(request, 'main_gym/view_equipment.html', d)


def Delete_Equipment(request, pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')


def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        try:
            Plan.objects.create(name=n, amount=a, duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'main_gym/add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'main_gym/view_plan.html', d)


def Delete_Plan(request, pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')


def Add_Member(request):
    error = ""
    plan1 = Plan.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        plan = Plan.objects.filter(name=p).first()
        try:
            Member.objects.create(name=n, contact=c, emailid=e, age=a, gender=g, plan=plan,
                                  joindate=joindate, expiredate=expiredate, initialamount=initialamount)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'plan': plan1}
    return render(request, 'main_gym/add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'main_gym/view_member.html', d)


def Delete_Member(request, pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')


socket.getaddrinfo('localhost', 8080)


def send_emails(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = Member.objects.all()
            emails = [(subject, message, settings.EMAIL_HOST, [
                       recipient.emailid]) for recipient in recipients]

            send_mass_mail(emails, fail_silently=False)

            for recipient in recipients:
                Email.objects.create(
                    subject=subject, message=message, member=recipient)

            return redirect('home')
    else:
        form = EmailForm()

    return render(request, 'main_gym/contact.html', {'form': form})
