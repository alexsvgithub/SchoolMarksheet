from multiprocessing import context
from shutil import register_archive_format
from django.shortcuts import redirect, render, HttpResponse
from home.models import firstTerm,secondTerm,DefaultValues,ObtainedMarks,DefaultValues,DefaultMinValues
from django.urls import reverse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
# from .forms import SignUpForm, EditProfileForm 

# Create your views here.
def index(request):
    dests = firstTerm.objects.all()
    context = {
        'dests':dests,
    }
    return render(request,'index.html',context)
    
    # return HttpResponse("THis is home page")

def marksheet(request):
    dests = firstTerm.objects.get(id=1)
    context = {
        'v':dests
    }
    return render(request,'marksheet.html',context)

def Details(request):
    if request.method == "POST":
        sem = request.POST.get('sem')
        std = request.POST.get('std')
        name = request.POST.get('name')
        m1 = request.POST.get('m1')
        m2 = request.POST.get('m2')
        m3 = request.POST.get('m3')
        h1 = request.POST.get('h1')
        h2 = request.POST.get('h2')
        h3 = request.POST.get('h3')
        e1 = request.POST.get('e1')
        e2 = request.POST.get('e2')
        e3 = request.POST.get('e3')
        mth1 = request.POST.get('mth1')
        mth2 = request.POST.get('mth2')
        mth3 = request.POST.get('mth3')
        sv1 = request.POST.get('sv1')
        sv2 = request.POST.get('sv2')
        sv3 = request.POST.get('sv3')
        ss1 = request.POST.get('ss1')
        ss2 = request.POST.get('ss2')
        ss3 = request.POST.get('ss3')
        k1 = request.POST.get('k1')
        k2 = request.POST.get('k2')
        k3 = request.POST.get('k3')
        kr1 = request.POST.get('kr1')
        kr2 = request.POST.get('kr2')
        kr3 = request.POST.get('kr3')
        ssk1 = request.POST.get('ssk1')
        ssk2 = request.POST.get('ssk2')
        ssk3 = request.POST.get('ssk3')
        hb1 = request.POST.get('hb1')
        hb2 = request.POST.get('hb2')
        hb3 = request.POST.get('hb3')
        vp1 = request.POST.get('vp1')
        vp2 = request.POST.get('vp2')
        vp3 = request.POST.get('vp3')
        mis1 = request.POST.get('mis1')
        mis2 = request.POST.get('mis2')
        mis3 = request.POST.get('mis3')
        miss1 = request.POST.get('miss1')
        miss2 = request.POST.get('miss2')
        miss3 = request.POST.get('miss3')
        rollNo = request.POST.get('rollNo')
        divi = request.POST.get('divi')
        
        #
    


        R = firstTerm(m1=m1,m2=m2,m3=m3,h1=h1,h2=h2,h3=h3,e1=e1,e2=e2,e3=e3,mth1=mth1,mth2=mth2,mth3=mth3,sv1=sv1,sv2=sv2,sv3=sv3,ss1=ss1,ss2=ss2,ss3=ss3,k1=k1,k2=k2,k3=k3,kr1=kr1,kr2=kr2,kr3=kr3,ssk1=ssk1,ssk2=ssk2,ssk3=ssk3,hb1=hb1,hb2=hb2,hb3=hb3,vp1=vp1,vp2=vp2,vp3=vp3,mis1=mis1,mis2=mis2,mis3=mis3,miss1=miss1,miss2=miss2,miss3=miss3,term=sem,std=std,name=name,rollNo=rollNo ,divi=divi, registerNo=rollNo)
        R.save()

    context = {
        'v':"--THis is variable--"
    }
    return redirect('/')
    # return render(request,'Details.html',context)

def Login(request):
    if request.method == 'POST':
        #if someone fills out form , Post it
        username = request.POST['un']
        password = request.POST['pd']
        user = authenticate(request, username=username, password=password)
        if user is not None:# if user exist
            login(request, user)
            messages.success(request,('Youre logged in'))
            return redirect('/') #routes to 'home' on successful login
        else:
            messages.success(request,('Error logging in'))
            return redirect('Login') #re routes to login page upon unsucessful login
    else:
        return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('Login')

def PlayingGround(request):
    if request.method == "POST":
        student = request.POST.get('student')
        what = request.POST.get('what')
        author = firstTerm.objects.filter(rollNo=student)
        # dests = firstTerm.objects.all()
        if(what == 'Details'):
            context = {
                'dests':author,
            }
            return render(request,'EditableDetails.html',context)
        else:
            author = ObtainedMarks.objects.filter(rollNo=student)
            context = {
                'dests':author,
            }
            return render(request,'EditableMarksheet.html',context)


        
        
    dests = firstTerm.objects.all()
    context = {
        'dests':dests,
    }
    return render(request,'PlayingGround.html',context)


def EditableDetails(request):
    if request.method == "POST":
        sem = request.POST.get('sem')
        std = request.POST.get('std')
        name = request.POST.get('name')
        m1 = request.POST.get('m1')
        m2 = request.POST.get('m2')
        m3 = request.POST.get('m3')
        h1 = request.POST.get('h1')
        h2 = request.POST.get('h2')
        h3 = request.POST.get('h3')
        e1 = request.POST.get('e1')
        e2 = request.POST.get('e2')
        e3 = request.POST.get('e3')
        mth1 = request.POST.get('mth1')
        mth2 = request.POST.get('mth2')
        mth3 = request.POST.get('mth3')
        sv1 = request.POST.get('sv1')
        sv2 = request.POST.get('sv2')
        sv3 = request.POST.get('sv3')
        ss1 = request.POST.get('ss1')
        ss2 = request.POST.get('ss2')
        ss3 = request.POST.get('ss3')
        k1 = request.POST.get('k1')
        k2 = request.POST.get('k2')
        k3 = request.POST.get('k3')
        kr1 = request.POST.get('kr1')
        kr2 = request.POST.get('kr2')
        kr3 = request.POST.get('kr3')
        ssk1 = request.POST.get('ssk1')
        ssk2 = request.POST.get('ssk2')
        ssk3 = request.POST.get('ssk3')
        hb1 = request.POST.get('hb1')
        hb2 = request.POST.get('hb2')
        hb3 = request.POST.get('hb3')
        vp1 = request.POST.get('vp1')
        vp2 = request.POST.get('vp2')
        vp3 = request.POST.get('vp3')
        mis1 = request.POST.get('mis1')
        mis2 = request.POST.get('mis2')
        mis3 = request.POST.get('mis3')
        miss1 = request.POST.get('miss1')
        miss2 = request.POST.get('miss2')
        miss3 = request.POST.get('miss3')
        rollNo = request.POST.get('rollNo')
        divi = request.POST.get('divi')
        id = request.POST.get('TheId')
        
        #
        firstTerm.objects.filter(rollNo=id).delete()
        

        R = firstTerm(m1=m1,m2=m2,m3=m3,h1=h1,h2=h2,h3=h3,e1=e1,e2=e2,e3=e3,mth1=mth1,mth2=mth2,mth3=mth3,sv1=sv1,sv2=sv2,sv3=sv3,ss1=ss1,ss2=ss2,ss3=ss3,k1=k1,k2=k2,k3=k3,kr1=kr1,kr2=kr2,kr3=kr3,ssk1=ssk1,ssk2=ssk2,ssk3=ssk3,hb1=hb1,hb2=hb2,hb3=hb3,vp1=vp1,vp2=vp2,vp3=vp3,mis1=mis1,mis2=mis2,mis3=mis3,miss1=miss1,miss2=miss2,miss3=miss3,term=sem,std=std,name=name,rollNo=rollNo ,divi=divi, registerNo=rollNo)
        R.save()

        
    return redirect('/')
    context = {
        'v':"--THis is variable--"
    }
    return render(request,'index.html',context)


def EditableMarksheet(request):
    if request.method == "POST":
        A1 = request.POST.get('A1')
        A2 = request.POST.get('A2')
        A3 = request.POST.get('A3')
        A4 = request.POST.get('A4')
        A5 = request.POST.get('A5')
        A6 = request.POST.get('A6')
        A7 = request.POST.get('A7')
        A8 = request.POST.get('A8')
        A9 = request.POST.get('A9')
        A10 = request.POST.get('A10')
        A11 = request.POST.get('A11')
        A12 = request.POST.get('A12')
        A13 = request.POST.get('A13')
        A14 = request.POST.get('A14')
        A15 = request.POST.get('A15')
        B1 = request.POST.get('B1')
        B2 = request.POST.get('B2')
        B3 = request.POST.get('B3')
        B4 = request.POST.get('B4')
        B5 = request.POST.get('B5')
        B6 = request.POST.get('B6')
        B7 = request.POST.get('B7')
        B8 = request.POST.get('B8')
        B9 = request.POST.get('B9')
        B10 = request.POST.get('B10')
        B11 = request.POST.get('B11')
        B12 = request.POST.get('B12')
        B13 = request.POST.get('B13')
        B14 = request.POST.get('B14')
        B15 = request.POST.get('B15')
        C1 = request.POST.get('C1')
        C2 = request.POST.get('C2')
        C3 = request.POST.get('C3')
        C4 = request.POST.get('C4')
        C5 = request.POST.get('C5')
        C6 = request.POST.get('C6')
        C7 = request.POST.get('C7')
        C8 = request.POST.get('C8')
        C9 = request.POST.get('C9')
        C10 = request.POST.get('C10')
        C11 = request.POST.get('C11')
        C12 = request.POST.get('C12')
        C13 = request.POST.get('C13')
        C14 = request.POST.get('C14')
        C15 = request.POST.get('C15')
        D1 = request.POST.get('D1')
        D2 = request.POST.get('D2')
        D3 = request.POST.get('D3')
        D4 = request.POST.get('D4')
        D5 = request.POST.get('D5')
        D6 = request.POST.get('D6')
        D7 = request.POST.get('D7')
        D8 = request.POST.get('D8')
        D9 = request.POST.get('D9')
        D10 = request.POST.get('D10')
        D11 = request.POST.get('D11')
        D12 = request.POST.get('D12')
        D13 = request.POST.get('D13')
        D14 = request.POST.get('D14')
        D15 = request.POST.get('D15')
        E1 = request.POST.get('E1')
        E2 = request.POST.get('E2')
        E3 = request.POST.get('E3')
        E4 = request.POST.get('E4')
        E5 = request.POST.get('E5')
        E6 = request.POST.get('E6')
        E7 = request.POST.get('E7')
        E8 = request.POST.get('E8')
        E9 = request.POST.get('E9')
        E10 = request.POST.get('E10')
        E11 = request.POST.get('E11')
        E12 = request.POST.get('E12')
        E13 = request.POST.get('E13')
        E14 = request.POST.get('E14')
        E15 = request.POST.get('E15')
        F1 = request.POST.get('F1')
        F2 = request.POST.get('F2')
        F3 = request.POST.get('F3')
        F4 = request.POST.get('F4')
        F5 = request.POST.get('F5')
        F6 = request.POST.get('F6')
        F7 = request.POST.get('F7')
        F8 = request.POST.get('F8')
        F9 = request.POST.get('F9')
        F10 = request.POST.get('F10')
        F11 = request.POST.get('F11')
        F12 = request.POST.get('F12')
        F13 = request.POST.get('F13')
        F14 = request.POST.get('F14')
        F15 = request.POST.get('F15')
        G1 = request.POST.get('G1')
        G2 = request.POST.get('G2')
        G3 = request.POST.get('G3')
        G4 = request.POST.get('G4')
        G5 = request.POST.get('G5')
        G6 = request.POST.get('G6')
        G7 = request.POST.get('G7')
        G8 = request.POST.get('G8')
        G9 = request.POST.get('G9')
        G14 = request.POST.get('G14')
        G15 = request.POST.get('G15')
        H1 = request.POST.get('H1')
        H2 = request.POST.get('H2')
        H3 = request.POST.get('H3')
        H4 = request.POST.get('H4')
        H5 = request.POST.get('H5')
        H6 = request.POST.get('H6')
        H7 = request.POST.get('H7')
        H8 = request.POST.get('H8')
        H9 = request.POST.get('H9')
        H14 = request.POST.get('H14')
        H15 = request.POST.get('H15')
        I1 = request.POST.get('I1')
        I2 = request.POST.get('I2')
        I3 = request.POST.get('I3')
        I4 = request.POST.get('I4')
        I5 = request.POST.get('I5')
        I6 = request.POST.get('I6')
        I7 = request.POST.get('I7')
        I8 = request.POST.get('I8')
        I9 = request.POST.get('I9')
        I14 = request.POST.get('I14')
        I15 = request.POST.get('I15')

    
        name = request.POST.get('name')
        rollNo = request.POST.get('rollNo')
        registerNo = request.POST.get('rollNo')
        std = request.POST.get('std')
        div = request.POST.get('div')
        id = request.POST.get('TheId')
        term = request.POST.get('sem')
        
        #
        ObtainedMarks.objects.filter(rollNo=id).delete()



     
        #
        # firstTerm.objects.filter(rollNo=id).delete()
        

        R = ObtainedMarks(term=term,name=name,rollNo = rollNo,registerNo = registerNo,std = std,div=div,A1=A1,
                            A2=A2,
                            A3=A3,
                            A4=A4,
                            A5=A5,
                            A6=A6,
                            A7=A7,
                            A8=A8,
                            A9=A9,
                            A10=A10,
                            A11=A11,
                            A12=A12,
                            A13=A13,
                            A14=A14,
                            A15=A15,
                            B1=B1,
                            B2=B2,
                            B3=B3,
                            B4=B4,
                            B5=B5,
                            B6=B6,
                            B7=B7,
                            B8=B8,
                            B9=B9,
                            B10=B10,
                            B11=B11,
                            B12=B12,
                            B13=B13,
                            B14=B14,
                            B15=B15,
                            C1=C1,
                            C2=C2,
                            C3=C3,
                            C4=C4,
                            C5=C5,
                            C6=C6,
                            C7=C7,
                            C8=C8,
                            C9=C9,
                            C10=C10,
                            C11=C11,
                            C12=C12,
                            C13=C13,
                            C14=C14,
                            C15=C15,
                            D1=D1,
                            D2=D2,
                            D3=D3,
                            D4=D4,
                            D5=D5,
                            D6=D6,
                            D7=D7,
                            D8=D8,
                            D9=D9,
                            D10=D10,
                            D11=D11,
                            D12=D12,
                            D13=D13,
                            D14=D14,
                            D15=D15,
                            E1=E1,
                            E2=E2,
                            E3=E3,
                            E4=E4,
                            E5=E5,
                            E6=E6,
                            E7=E7,
                            E8=E8,
                            E9=E9,
                            E10=E10,
                            E11=E11,
                            E12=E12,
                            E13=E13,
                            E14=E14,
                            E15=E15,
                            F1=F1,
                            F2=F2,
                            F3=F3,
                            F4=F4,
                            F5=F5,
                            F6=F6,
                            F7=F7,
                            F8=F8,
                            F9=F9,
                            F10=F10,
                            F11=F11,
                            F12=F12,
                            F13=F13,
                            F14=F14,
                            F15=F15,
                            G1=G1,
                            G2=G2,
                            G3=G3,
                            G4=G4,
                            G5=G5,
                            G6=G6,
                            G7=G7,
                            G8=G8,
                            G9=G9,
                            G14=G14,
                            G15=G15,
                            H1=H1,
                            H2=H2,
                            H3=H3,
                            H4=H4,
                            H5=H5,
                            H6=H6,
                            H7=H7,
                            H8=H8,
                            H9=H9,
                            H14=H14,
                            H15=H15,
                            I1=I1,
                            I2=I2,
                            I3=I3,
                            I4=I4,
                            I5=I5,
                            I6=I6,
                            I7=I7,
                            I8=I8,
                            I9=I9,
                            I14=I14,
                            I15=I15)
        R.save()
        context = {
        'v':"--THis is variable--"
        }
    return redirect('/')
    return render(request,'EntrySplitter.html',context)

        

def EntrySplitter(request):
    if request.method == "POST":
        what = request.POST.get('what')
        if(what == 'Details'):
            context = {
                'dests':"author",
            }
            return render(request,'Details.html',context)
        else:
            # dests = ObtainedMarks.objects.all()
            context = {
                'dests':'dests',
            }
            return render(request,'marksheet.html',context)
    context = {
        'v':"--THis is variable--"
    }
    return render(request,'EntrySplitter.html',context)

def saveMarksheet(request):
    if request.method == "POST":
        # A1 = request.POST.get('A1')
        # A2 = request.POST.get('A2')
        # A3 = request.POST.get('A3')
        # A4 = request.POST.get('A4')
        # A5 = request.POST.get('A5')
        # A6 = request.POST.get('A6')
        # A7 = request.POST.get('A7')
        # A8 = request.POST.get('A8')
        # A9 = int(A1)+int(A2)+int(A3)+int(A4)+int(A5)+int(A6)+int(A7)+int(A8)
        # A10 = request.POST.get('A10')
        # A11 = request.POST.get('A11')
        # A12 = request.POST.get('A12')
        # A13 = int(A10)+int(A11)+int(A12)
        # A14 = int(A9)+int(A13)
        # A15 = request.POST.get('A15')

        # B1 = request.POST.get('B1')
        # B2 = request.POST.get('B2')
        # B3 = request.POST.get('B3')
        # B4 = request.POST.get('B4')
        # B5 = request.POST.get('B5')
        # B6 = request.POST.get('B6')
        # B7 = request.POST.get('B7')
        # B8 = request.POST.get('B8')
        # B9 = int(B1)+int(B2)+int(B3)+int(B4)+int(B5)+int(B6)+int(B7)+int(B8)
        # B10 = request.POST.get('B10')
        # B11 = request.POST.get('B11')
        # B12 = request.POST.get('B12')
        # B13 = int(B10)+int(B11)+int(B12)
        # B14 = int(B9)+int(B13)
        # B15 = request.POST.get('B15')

        # C1 = request.POST.get('C1')
        # C2 = request.POST.get('C2')
        # C3 = request.POST.get('C3')
        # C4 = request.POST.get('C4')
        # C5 = request.POST.get('C5')
        # C6 = request.POST.get('C6')
        # C7 = request.POST.get('C7')
        # C8 = request.POST.get('C8')
        # C9 = int(C1)+int(C2)+int(C3)+int(C4)+int(C5)+int(C6)+int(C7)+int(C8)
        # C10 = request.POST.get('C10')
        # C11 = request.POST.get('C11')
        # C12 = request.POST.get('C12')
        # C13 = int(C10)+int(C11)+int(C12)
        # C14 = int(C9)+int(C13)
        # C15 = request.POST.get('C15')

        # D1 = request.POST.get('D1')
        # D2 = request.POST.get('D2')
        # D3 = request.POST.get('D3')
        # D4 = request.POST.get('D4')
        # D5 = request.POST.get('D5')
        # D6 = request.POST.get('D6')
        # D7 = request.POST.get('D7')
        # D8 = request.POST.get('D8')
        # D9 = int(D1)+int(D2)+int(D3)+int(D4)+int(D5)+int(D6)+int(D7)+int(D8)
        # D10 = request.POST.get('D10')
        # D11 = request.POST.get('D11')
        # D12 = request.POST.get('D12')
        # D13 = int(D10)+int(D11)+int(D12)
        # D14 = int(D9)+int(D13)
        # D15 = request.POST.get('D15')

        # E1 = request.POST.get('E1')
        # E2 = request.POST.get('E2')
        # E3 = request.POST.get('E3')
        # E4 = request.POST.get('E4')
        # E5 = request.POST.get('E5')
        # E6 = request.POST.get('E6')
        # E7 = request.POST.get('E7')
        # E8 = request.POST.get('E8')
        # E9 = int(E1)+int(E2)+int(E3)+int(E4)+int(E5)+int(E6)+int(E7)+int(E8)
        # E10 = request.POST.get('E10')
        # E11 = request.POST.get('E11')
        # E12 = request.POST.get('E12')
        # E13 = int(E10)+int(E11)+int(E12)
        # E14 = int(E9)+int(E13)
        # E15 = request.POST.get('E15')

        # F1 = request.POST.get('F1')
        # F2 = request.POST.get('F2')
        # F3 = request.POST.get('F3')
        # F4 = request.POST.get('F4')
        # F5 = request.POST.get('F5')
        # F6 = request.POST.get('F6')
        # F7 = request.POST.get('F7')
        # F8 = request.POST.get('F8')
        # F9 = int(F1)+int(F2)+int(F3)+int(F4)+int(F5)+int(F6)+int(F7)+int(F8)
        # F10 = request.POST.get('F10')
        # F11 = request.POST.get('F11')
        # F12 = request.POST.get('F12')
        # F13 = int(F10)+int(F11)+int(F12)
        # F14 = int(F9)+int(F13)
        # F15 = request.POST.get('F15')

        # G1 = request.POST.get('G1')
        # G2 = request.POST.get('G2')
        # G3 = request.POST.get('G3')
        # G4 = request.POST.get('G4')
        # G5 = request.POST.get('G5')
        # G6 = request.POST.get('G6')
        # G7 = request.POST.get('G7')
        # G8 = request.POST.get('G8')
        # G9 = int(G1)+int(G2)+int(G3)+int(G4)+int(G5)+int(G6)+int(G7)+int(G8)
        # G14 = G9
        # G15 = request.POST.get('G15')

        # H1 = request.POST.get('H1')
        # H2 = request.POST.get('H2')
        # H3 = request.POST.get('H3')
        # H4 = request.POST.get('H4')
        # H5 = request.POST.get('H5')
        # H6 = request.POST.get('H6')
        # H7 = request.POST.get('H7')
        # H8 = request.POST.get('H8')
        # H9 = int(H1)+int(H2)+int(H3)+int(H4)+int(H5)+int(H6)+int(H7)+int(H8)
        # H14 = H9
        # H15 = request.POST.get('H15')
        
        # I1 = request.POST.get('I1')
        # I2 = request.POST.get('I2')
        # I3 = request.POST.get('I3')
        # I4 = request.POST.get('I4')
        # I5 = request.POST.get('I5')
        # I6 = request.POST.get('I6')
        # I7 = request.POST.get('I7')
        # I8 = request.POST.get('I8')
        # I9 = int(I1)+int(I2)+int(I3)+int(I4)+int(I5)+int(I6)+int(I7)+int(I8)
        # I14 = I9
        # I15 = request.POST.get('I15')





        A1 = request.POST.get('A1')
        A2 = request.POST.get('A2')
        A3 = request.POST.get('A3')
        A4 = request.POST.get('A4')
        A5 = request.POST.get('A5')
        A6 = request.POST.get('A6')
        A7 = request.POST.get('A7')
        A8 = request.POST.get('A8')
        A9 = request.POST.get('A9')
        A10 = request.POST.get('A10')
        A11 = request.POST.get('A11')
        A12 = request.POST.get('A12')
        A13 = request.POST.get('A13')
        A14 = request.POST.get('A14')
        A15 = request.POST.get('A15')
        B1 = request.POST.get('B1')
        B2 = request.POST.get('B2')
        B3 = request.POST.get('B3')
        B4 = request.POST.get('B4')
        B5 = request.POST.get('B5')
        B6 = request.POST.get('B6')
        B7 = request.POST.get('B7')
        B8 = request.POST.get('B8')
        B9 = request.POST.get('B9')
        B10 = request.POST.get('B10')
        B11 = request.POST.get('B11')
        B12 = request.POST.get('B12')
        B13 = request.POST.get('B13')
        B14 = request.POST.get('B14')
        B15 = request.POST.get('B15')
        C1 = request.POST.get('C1')
        C2 = request.POST.get('C2')
        C3 = request.POST.get('C3')
        C4 = request.POST.get('C4')
        C5 = request.POST.get('C5')
        C6 = request.POST.get('C6')
        C7 = request.POST.get('C7')
        C8 = request.POST.get('C8')
        C9 = request.POST.get('C9')
        C10 = request.POST.get('C10')
        C11 = request.POST.get('C11')
        C12 = request.POST.get('C12')
        C13 = request.POST.get('C13')
        C14 = request.POST.get('C14')
        C15 = request.POST.get('C15')
        D1 = request.POST.get('D1')
        D2 = request.POST.get('D2')
        D3 = request.POST.get('D3')
        D4 = request.POST.get('D4')
        D5 = request.POST.get('D5')
        D6 = request.POST.get('D6')
        D7 = request.POST.get('D7')
        D8 = request.POST.get('D8')
        D9 = request.POST.get('D9')
        D10 = request.POST.get('D10')
        D11 = request.POST.get('D11')
        D12 = request.POST.get('D12')
        D13 = request.POST.get('D13')
        D14 = request.POST.get('D14')
        D15 = request.POST.get('D15')
        E1 = request.POST.get('E1')
        E2 = request.POST.get('E2')
        E3 = request.POST.get('E3')
        E4 = request.POST.get('E4')
        E5 = request.POST.get('E5')
        E6 = request.POST.get('E6')
        E7 = request.POST.get('E7')
        E8 = request.POST.get('E8')
        E9 = request.POST.get('E9')
        E10 = request.POST.get('E10')
        E11 = request.POST.get('E11')
        E12 = request.POST.get('E12')
        E13 = request.POST.get('E13')
        E14 = request.POST.get('E14')
        E15 = request.POST.get('E15')
        F1 = request.POST.get('F1')
        F2 = request.POST.get('F2')
        F3 = request.POST.get('F3')
        F4 = request.POST.get('F4')
        F5 = request.POST.get('F5')
        F6 = request.POST.get('F6')
        F7 = request.POST.get('F7')
        F8 = request.POST.get('F8')
        F9 = request.POST.get('F9')
        F10 = request.POST.get('F10')
        F11 = request.POST.get('F11')
        F12 = request.POST.get('F12')
        F13 = request.POST.get('F13')
        F14 = request.POST.get('F14')
        F15 = request.POST.get('F15')
        G1 = request.POST.get('G1')
        G2 = request.POST.get('G2')
        G3 = request.POST.get('G3')
        G4 = request.POST.get('G4')
        G5 = request.POST.get('G5')
        G6 = request.POST.get('G6')
        G7 = request.POST.get('G7')
        G8 = request.POST.get('G8')
        G9 = request.POST.get('G9')
        G14 = request.POST.get('G14')
        G15 = request.POST.get('G15')
        H1 = request.POST.get('H1')
        H2 = request.POST.get('H2')
        H3 = request.POST.get('H3')
        H4 = request.POST.get('H4')
        H5 = request.POST.get('H5')
        H6 = request.POST.get('H6')
        H7 = request.POST.get('H7')
        H8 = request.POST.get('H8')
        H9 = request.POST.get('H9')
        H14 = request.POST.get('H14')
        H15 = request.POST.get('H15')
        I1 = request.POST.get('I1')
        I2 = request.POST.get('I2')
        I3 = request.POST.get('I3')
        I4 = request.POST.get('I4')
        I5 = request.POST.get('I5')
        I6 = request.POST.get('I6')
        I7 = request.POST.get('I7')
        I8 = request.POST.get('I8')
        I9 = request.POST.get('I9')
        I14 = request.POST.get('I14')
        I15 = request.POST.get('I15')



        name = request.POST.get('name')
        rollNo = request.POST.get('rollNo')
        registerNo = request.POST.get('rollNo')
        std = request.POST.get('std')
        div = request.POST.get('div')
        term = request.POST.get('sem')



     
        #
        # firstTerm.objects.filter(rollNo=id).delete()
        

        R = ObtainedMarks(term=term,name=name,rollNo = rollNo,registerNo = registerNo,std = std,div=div,A1=A1,A2=A2,A3=A3,A4=A4,A5=A5,A6=A6,A7=A7,A8=A8,A9=A9,A10=A10,A11=A11,A12=A12,A13=A13,A14=A14,A15=A15,B1=B1,B2=B2,B3=B3,B4=B4,B5=B5,B6=B6,B7=B7,B8=B8,B9=B9,B10=B10,B11=B11,B12=B12,B13=B13,B14=B14,B15=B15,C1=C1,C2=C2,C3=C3,C4=C4,C5=C5, C6=C6,C7=C7,C8=C8,C9=C9, C10=C10,C11=C11, C12=C12,C13=C13,C14=C14,C15=C15,D1=D1, D2=D2,D3=D3,D4=D4,D5=D5, D6=D6,D7=D7,D8=D8,D9=D9,D10=D10,D11=D11,D12=D12, D13=D13,D14=D14, D15=D15,E1=E1,E2=E2,E3=E3,E4=E4,E5=E5,E6=E6,E7=E7,E8=E8,E9=E9,E10=E10, E11=E11,E12=E12,E13=E13,E14=E14,E15=E15, F1=F1,F2=F2,F3=F3,F4=F4,F5=F5,F6=F6,F7=F7,F8=F8,F9=F9,F10=F10,F11=F11,F12=F12,F13=F13,F14=F14, F15=F15,G1=G1,G2=G2,G3=G3,G4=G4,G5=G5,G6=G6,G7=G7,G8=G8,G9=G9,G14=G14,G15=G15,H1=H1, H2=H2, H3=H3,H4=H4,H5=H5,H6=H6,H7=H7,H8=H8,H9=H9,H14=H14,H15=H15,I1=I1,I2=I2,I3=I3,I4=I4,I5=I5,I6=I6,I7=I7,I8=I8,I9=I9,I14=I14,I15=I15)
        R.save()
        return redirect('/')
        context = {
            'v':"--THis is variable--"
        }
        return render(request,'index.html',context)





# def LLogin(request):
#     if request.method == "POST":
#         un = request.POST.get('username')
#         pd = request.POST.get('password')
#         user = authenticate(username=un, password=pd)
#         if user is not None:
#             # A backend authenticated the credentials
#             context = {
#                 'v':"--THis is variable--"
#             }
#             return render(request,'index.html',context)
#         else:
#             # No backend authenticated the credentials
#             context = {
#                 'v':"--THis is variable--"
#             }
#             return render(request,'login.html',context)