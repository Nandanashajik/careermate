from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def Login_get(request):
    return render(request,"loginindex.html")

def Login_post(request):
    Username=request.POST['textfield']
    Password=request.POST['textfield2']
    lg=Login.objects.filter(username=Username,password=Password)
    if lg.exists():
        lg1=Login.objects.get(username=Username,password=Password)
        request.session['lid']=lg1.id

        if lg1.type=="admin":
            return HttpResponse(
                '''<script>alert('admin login success');window.location='/myapp/adminhome_get/'</script>''')


        elif lg1.type=="guide":
            return HttpResponse(
                '''<script>alert('mentor login success');window.location='/myapp/guidehome_get/'</script>''')


        elif lg1.type=="company":
            return HttpResponse(
                '''<script>alert('company login success');window.location='/myapp/companyhome_get/'</script>''')


        elif lg1.type=="user":
            return HttpResponse(
                '''<script>alert('Job Aspirant login success');window.location='/myapp/userhomeindex_get/#a'</script>''')



        else:
            return HttpResponse('''<script>alert('admin not found');window.location='/myapp/Login_get/'</script>''')
    else:
        return HttpResponse('''<script>alert('user not found');window.location='/myapp/Login_get/'</script>''')


def Changepassword_get(request):
    if request.session['lid']=='':
        return redirect('/myapp/Login_get/')

    return render(request, "admin/changepassword.html")
def Changepassword_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:

        current_password=request.POST['textfield']
        new_password=request.POST['textfield2']
        confirm_password=request.POST['textfield3']
        check=Login.objects.filter(password=current_password,id=request.session['lid'])
        if check.exists():
            if new_password==confirm_password:
                Login.objects.filter(password=current_password,id=request.session['lid']).update(password=confirm_password)
                return HttpResponse('''<script>alert('password updated succesfully');window.location='/myapp/Login_get/'</script>''')

            else:
                return HttpResponse('''<script>alert('password and confirm password not match');window.location='/myapp/Changepassword_get/'</script>''')
        else:
            return HttpResponse('''<script>alert('incorrect password');window.location='/myapp/Changepassword_get/'</script>''')




def companyview_get(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        data=Company.objects.filter(status="pending")
        return render(request, "admin/company view.html",{"data":data})

def companyview_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        search=request.POST['textfield']
        data = Company.objects.filter(status="pending",companyname__icontains=search)
        return render(request, "admin/company view.html", {"data": data})

def approvecompany(request,id):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        Company.objects.filter(LOGIN=id).update(status="approved")
        Login.objects.filter(id=id).update(type='company')
        return HttpResponse('''<script>alert('company approved successfully');window.location='/myapp/companyview_get/'</script>''')

def rejectcompany(request,id):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        Company.objects.filter(LOGIN=id).update(status="rejected")
        Login.objects.filter(id=id).update(type='rejected')

        return HttpResponse('''<script>alert('company rejected');window.location='/myapp/companyview_get/'</script>''')


def guideview_get(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        data=Guide.objects.filter(status="pending")
        return render(request,"admin/guide view.html",{"data":data})

def guideview_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        search=request.POST['textfield']
        data = Guide.objects.filter(name__icontains=search)
        return render(request, "admin/guide view.html", {"data": data})

def approveguide(request,id):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        Guide.objects.filter(LOGIN=id).update(status="approved")
        Login.objects.filter(id=id).update(type='guide')
        return HttpResponse('''<script>alert('Mentor approved successfully');window.location='/myapp/guideview_get/'</script>''')

def rejectguide(request,id):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        Guide.objects.filter(LOGIN=id).update(status="rejected")
        Login.objects.filter(id=id).update(type='rejected')
        return HttpResponse('''<script>alert('Mentor rejected');window.location='/myapp/guideview_get/'</script>''')



def viewApprovedCompany_get(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:

        data=Company.objects.filter(status="approved")
        return render(request,"admin/view approved company.html",{"data":data})
def viewApprovedCompany_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        search=request.POST['textfield']
        data = Company.objects.filter(status="approved",companyname__icontains=search)
        return render(request, "admin/view approved company.html", {"data": data})


def viewApprovedGuide_get(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        data = Guide.objects.filter(status="approved")
        return render(request,"admin/view approved guide.html",{"data":data})
def viewApprovedGuide_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        search=request.POST['textfield']
        data = Guide.objects.filter(status="approved",name__icontains=search)
        return render(request, "admin/view approved guide.html", {"data": data})


def viewRegisteredUsers_get(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        data=User.objects.all()
        return render(request,"admin/view registered users.html",{"data":data})
def viewRegisteredUsers_post(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:
        search=request.POST['textfield']
        data = User.objects.filter(name__icontains=search)
        return render(request, "admin/view registered users.html", {"data": data})

def motivationalVideo_get(request):
    return render(request, "admin/motivationalvideos.html")
def motivationalVideo_post(request):
    video=request.FILES['video']
    # date=request.POST['date']
    title=request.POST['title']
    description=request.POST['description']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.mp4'
    fs.save(date, video)
    path = fs.url(date)


    var=Videos()
    var.video=path
    var.date=datetime.now().today()
    var.title=title
    var.description=description
    var.save()



    return HttpResponse('''<script>alert('video uploaded');window.location='/myapp/adminhome_get/'</script>''')

def adminlogout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('logout success');window.location='/myapp/Login_get/'</script>''')

def adminhome_get(request):
    if request.session['lid'] == '':
        return redirect('/myapp/Login_get/')
    else:

        return render(request,"admin/adminindex.html")



# guide


def register_get(request):
    return render(request,"guide/register.html")
def register_post(request):

    name=request.POST['name']
    photo=request.FILES['photo']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    district=request.POST['district']
    workplace=request.POST['workplace']
    qualification=request.POST['qualification']
    certificate=request.FILES['certificate']
    password=request.POST['password']
    confirmpassword=request.POST['confirm_password']

    fs=FileSystemStorage()
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    fs.save(date,photo)
    path=fs.url(date)

    cer=FileSystemStorage()
    date2=datetime.now().strftime('%Y%m%d-%H%M%S')+'.pdf'
    cer.save(date2,certificate)
    pathh=cer.url(date2)



    if Login.objects.filter(username=email).exists():
        return HttpResponse(
            '''<script>alert('Email already Existed');window.location='/myapp/register_get/'</script>''')

    if password==confirmpassword:


        l=Login()
        l.username=email
        l.password= password
        l.type='pending'
        l.save()


        gu=Guide()
        gu.name=name
        gu.email=email
        gu.phoneno=phone
        gu.photo=path
        gu.place=place
        gu.pin=pin
        gu.post=post
        gu.district=district
        gu.workplace=workplace
        gu.qualification=qualification
        gu.certificate=pathh
        gu.status='pending'
        gu.LOGIN=l
        gu.save()
        return HttpResponse('''<script>alert('guide registerd succesfully');window.location='/myapp/Login_get/'</script>''')
    else:
        return HttpResponse('''<script>alert('password doesn't match');window.location='/myapp/register_get/'</script>''')




def changepassword_get(request):
    return render(request,"guide/gchangepassword.html")
def changepassword_post(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    check = Login.objects.filter(password=current_password, id=request.session['lid'])
    if check.exists():
        if new_password == confirm_password:
            Login.objects.filter(password=current_password, id=request.session['lid']).update(password=confirm_password)
            return HttpResponse(
                '''<script>alert('password updated succesfully');window.location='/myapp/Login_get/'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('password and confirm password not match');window.location='/myapp/Changepassword_get/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('incorrect password');window.location='/myapp/Changepassword_get/'</script>''')


def viewprofile_get(request):
    data=Guide.objects.get(LOGIN=request.session['lid'])
    return render(request,"guide/view profile.html",{'data':data})

def edit_get(request,id):
    data=Guide.objects.get(id=id)
    return render(request,"guide/edit.html",{'data':data})
def edit_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield10']
    pin = request.POST['textfield5']
    post = request.POST['textfield6']
    district = request.POST['textfield7']
    workplace = request.POST['textfield8']
    qualification = request.POST['textfield9']
    id = request.POST['id']
    gu = Guide.objects.get(id=id)

    if 'textfield2' in request.FILES:
        photo = request.FILES['textfield2']
        if photo !='':
            fs = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
            fs.save(date, photo)
            path = fs.url(date)
            gu.photo = path
            gu.save()

    if 'textfield10' in request.FILES:
        certificate = request.FILES['textfield10']
        if certificate != '':
            cer = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.pdf'
            cer.save(date, certificate)
            pathh = cer.url(date)
            gu.certificate = pathh
            gu.save()

    gu.name = name
    gu.email = email
    gu.phoneno = phone
    gu.place = place
    gu.pin = pin
    gu.post = post
    gu.district = district
    gu.workplace=workplace
    gu.qualification=qualification
    gu.save()
    return HttpResponse('''<script>alert('edited succesfully');window.location='/myapp/viewprofile_get/'</script>''')


def viewrequestfromuser_get(request):
    data=Request.objects.filter(status='pending',GUIDE__LOGIN=request.session['lid'])
    return render(request,"guide/view request from user.html",{"data":data})
def viewrequestfromuser_post(request):
    return render(request,"guide/view request from user.html")


def viewapprovedrequest_get(request):
    data= Request.objects.filter(status="approved",GUIDE__LOGIN=request.session['lid'])
    return render(request,"guide/virew approved request.html",{"data":data})
def viewapprovedrequest_post(request):
    search=request.POST['textfield']
    data= Request.objects.filter(status="approved",USER__name__icontains=search,GUIDE__LOGIN=request.session['lid'])
    return render(request,"guide/virew approved request.html",{"data":data})

def acceptrequest_get(request,id):
    data = Request.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert('Approved');window.location='/myapp/viewrequestfromuser_get/'</script>''')

def rejectrequest_get(request,id):
    data = Request.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert('Rejected');window.location='/myapp/viewrequestfromuser_get/'</script>''')

def guide_viewRegisteredUsers_get(request):
    data=User.objects.all()
    return render(request,"guide/view registered users.html",{"data":data})

def guide_viewRegisteredUsers_post(request):
    search=request.POST['textfield']
    data = User.objects.filter(name__icontains=search)
    return render(request, "guide/view registered users.html", {"data": data})


def guidehome_get(request):
    return render(request,"guide/guideindex.html")


#company

def c_register_get(request):
    return render(request,"company/register.html")
def c_register_post(request):
    companyname=request.POST['company_name']
    liscenceno=request.POST['license_no']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    district=request.POST['district']
    state=request.POST['state']
    phoneno=request.POST['phone']
    email=request.POST['email']
    photo=request.FILES['photo']
    password=request.POST['password']
    confirmpassword=request.POST['confirm_password']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs.save(date,photo)
    path = fs.url(date)

    if Login.objects.filter(username=email).exists():
        return HttpResponse(
            '''<script>alert('Email already Existed');window.location='/myapp/register_get/'</script>''')


    if password == confirmpassword:

        l = Login()
        l.username = email
        l.password = password
        l.type = 'pending'
        l.save()

        co =Company()
        co.companyname = companyname
        co.liscenceno = liscenceno
        co.email = email
        co.phoneno = phoneno
        co.photo = path
        co.place = place
        co.pin = pin
        co.post = post
        co.district = district
        co.state=state
        co.status = 'pending'
        co.LOGIN = l
        co.save()
        return HttpResponse(
            '''<script>alert('company registerd succesfully');window.location='/myapp/Login_get/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('password doesn't match');window.location='/myapp/c_register_get/'</script>''')


def c_changepassword_get(request):
    return render(request, "company/cochangepassword.html")
def c_changepassword_post(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    check = Login.objects.filter(password=current_password, id=request.session['lid'])
    if check.exists():
        if new_password == confirm_password:
            Login.objects.filter(password=current_password, id=request.session['lid']).update(password=confirm_password)
            return HttpResponse(
                '''<script>alert('password updated succesfully');window.location='/myapp/Login_get/'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('password and confirm password not match');window.location='/myapp/Changepassword_get/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('incorrect password');window.location='/myapp/Changepassword_get/'</script>''')

def c_viewprofile_get(request):
    data=Company.objects.get(LOGIN=request.session['lid'])
    return render(request,"Company/view profile.html",{'data':data})

def c_edit_get(request):
    data=Company.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"company/edit.html",{'data':data})
def c_edit_post(request):
    companyname= request.POST['textfield']
    liscenceno= request.POST['textfield2']
    email = request.POST['textfield9']
    phoneno = request.POST['textfield10']
    place = request.POST['textfield3']
    pin = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    state=request.POST['textfield7']

    co = Company.objects.get(LOGIN_id=request.session['lid'])

    if 'textfield8' in request.FILES:
        photo = request.FILES['textfield8']
        if photo !='':
            fs = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
            fs.save(date, photo)
            path = fs.url(date)
            co.photo = path
            co.save()

    co.companyname = companyname
    co.liscenceno = liscenceno
    co.email = email
    co.phoneno = phoneno
    co.place = place
    co.pin = pin
    co.post = post
    co.district = district
    co.state=state
    co.save()
    return HttpResponse('''<script>alert('edited succesfully');window.location='/myapp/c_viewprofile_get/'</script>''')

def addvacancy_get(request):
    return render(request,"Company/add vacancy.html")


def addvacancy_post(request):
    description=request.POST['description']
    job=request.POST['job']
    # companydetails=request.POST['companydetails']
    eligibility=request.POST['eligibility']


    a=Vacancy()
    a.description=description
    # a.companydetails=companydetails
    a.eligibility=eligibility
    a.JOB=job
    a.COMPANY=Company.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('Vacancy Added Succesfully');window.location='/myapp/companyhome_get/'</script>''')




def editvacancy_get(request,id):
    data=Company.objects.get(id=id)
    return render(request,"Company/edit vacancy.html",{'data':data})

def editvacancy_post(request):
    description = request.POST['textfield9']
    jid = request.POST['jid']

    a = Vacancy()
    a.description = description
    a.JOB_id = jid
    a.USER = User.objects.get(LOGIN_id=request.section['lid'])
    a.save()
    return HttpResponse('''<script>alert('edited succesfully');window.location='/myapp/viewvacancy_get/'</script>''')


def viewvacancy_get(request):
    data=Vacancy.objects.all()
    return render(request,"Company/view vacancy.html",{'data':data})

def viewvacancy_post(request):
    data = Vacancy.objects.all()
    return render(request, "Company/view vacancy.html", {'data': data})


def viewrequest_qualification_get(request):
    data=Application.objects.filter(status='pending')
    return render(request,"Company/view request and qualification.html",{'data':data})
def viewrequest_qualification_post(request):
    fdate=request.POST['textfield']
    tdate=request.POST['textfield2']
    data=Application.objects.filter(date__range=[fdate,tdate],status='pending')
    return render(request,"Company/view request and qualification.html",{'data':data})

def c_acceptrequest_get(request,id):
    data = Application.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert('Approved');window.location='/myapp/viewrequest_qualification_get/'</script>''')

def c_rejectrequest_get(request,id):
    data = Application.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert('Rejected');window.location='/myapp/viewrequest_qualification_get/'</script>''')


def companyhome_get(request):
    return render(request,"Company/companyindex.html")


#user

def userregister_get(request):
    return render(request,"user/register.html")
def userregister_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    photo = request.FILES['photo']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['post']
    district = request.POST['district']
    state = request.POST['state']
    password = request.POST['password']
    confirmpassword = request.POST['confirm_password']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs.save(date, photo)
    path = fs.url(date)

    if Login.objects.filter(username=email).exists():
        return HttpResponse(
            '''<script>alert('Email already Existed');window.location='/myapp/register_get/'</script>''')

    if password == confirmpassword:

        l = Login()
        l.username = email
        l.password = password
        l.type = 'user'
        l.save()

        us = User()
        us.name = name
        us.email = email
        us.phone = phone
        us.photo = path
        us.place = place
        us.pin = pin
        us.post = post
        us.district = district
        us.state=state
        us.LOGIN = l
        us.save()
        return HttpResponse(
            '''<script>alert('User registerd succesfully');window.location='/myapp/Login_get/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('password doesn't match');window.location='/myapp/register_get/'</script>''')


def u_changepassword_get(request):
    return render(request,"user/uchangepassword.html")
def u_changepassword_post(request):
    current_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    check = Login.objects.filter(password=current_password, id=request.session['lid'])
    if check.exists():
        if new_password == confirm_password:
            Login.objects.filter(password=current_password, id=request.session['lid']).update(password=confirm_password)
            return HttpResponse(
                '''<script>alert('password updated succesfully');window.location='/myapp/Login_get/'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('password and confirm password not match');window.location='/myapp/Changepassword_get/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('incorrect password');window.location='/myapp/Changepassword_get/'</script>''')

def u_viewprofile_get(request):
    data=User.objects.get(LOGIN=request.session['lid'])
    return render(request,"User/view profile.html",{'data':data})

def u_edit_get(request):
    data=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/edit.html",{'data':data})
def u_edit_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield10']
    pin = request.POST['textfield5']
    post = request.POST['textfield6']
    district = request.POST['textfield7']
    us = User.objects.get(LOGIN_id=request.session['lid'])

    if 'textfield2' in request.FILES:
        photo = request.FILES['textfield2']
        if photo !='':
            fs = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
            fs.save(date, photo)
            path = fs.url(date)
            us.photo = path
            us.save()

    us.name = name
    us.email = email
    us.phone = phone
    us.place = place
    us.pin = pin
    us.post = post
    us.district = district
    us.save()
    return HttpResponse('''<script>alert('edited succesfully');window.location='/myapp/u_viewprofile_get/'</script>''')

def user_viewvacancy_get(request):
    a=Vacancy.objects.all()
    return render(request,"User/view vacancy.html",{'data':a})

def user_viewvacancy_post(request):
    a = Vacancy.objects.all()
    return render(request,"User/view vacancy.html", {'data':a})

def applyvacancy_get(request,id):
    request.session['vid']=id
    return render(request,"user/apply vacancy.html")

def applyvacancy_post(request):

    cv=request.FILES['filefield']

    fs = FileSystemStorage()
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.pdf'
    fs.save(date, cv)
    path = fs.url(date)
    if Application.objects.filter(VACANCY_id=request.session['vid'],USER=User.objects.get(LOGIN_id=request.session['lid'])).exists():
        return HttpResponse(
            '''<script>alert('Already Exists');window.location='/myapp/user_viewvacancy_get/'</script>''')

    c=Application()
    c.date=datetime.today()
    c.VACANCY_id=request.session['vid']
    c.CV=path
    c.USER=User.objects.get(LOGIN_id=request.session['lid'])
    c.status='pending'
    c.save()
    return HttpResponse('''<script>alert('Application send successfully');window.location='/myapp/user_viewvacancy_get/'</script>''')



# def qualificationmngt_get(request):
#     return render(request,"User/qualification management.html")
# def qualificationmngt_post(request):
#     date=request.POST['textfield3']
#     title=request.POST['textfield4']
#     description=request.POST['textfield5']
#     qualification=request.POST['textfield6']
#
#     a=Job()
#     a.title=title
#     a.qualification=qualification
#     a.description=description
#     a.date=date
#     a.USER=User.objects.get(LOGIN_id=request.session['lid'])
#     a.save()
#     return HttpResponse('''<script>alert('qualification added successfully');window.location='/myapp//'</script>''')

def viewstatus_get(request):
    a=Application.objects.filter(status='approved')
    return render(request,"User/view status.html",{'data':a})

def sendrequest_get(request):
    d=Guide.objects.filter(status='approved')
    return render(request,"User/send request.html",{'data':d})

def sendrequest_post(request,id):
    if Request.objects.filter(USER__LOGIN_id=request.session['lid'],status__in=['pending','approved']).exists():
    # if Request.objects.filter(GUIDE_id=id,USER__LOGIN_id=request.session['lid']).exists():
        return HttpResponse(
            '''<script>alert('request already existed');window.location='/myapp/u_viewApprovedGuide_get/'</script>''')



    c=Request()
    c.date=datetime.now().today()
    c.GUIDE_id=id
    c.USER=User.objects.get(LOGIN_id=request.session['lid'])
    c.status='pending'
    c.save()
    return HttpResponse('''<script>alert('request send successfully');window.location='/myapp/u_viewApprovedGuide_get/'</script>''')

def u_viewApprovedCompany_get(request):
    data = Company.objects.filter(status="approved")
    return render(request, "user/user view approved company.html", {"data": data})

def u_viewApprovedCompany_post(request):
    search = request.POST['textfield']
    data = Company.objects.filter(status="approved", companyname__icontains=search)
    return render(request, "user/user view approved company.html", {"data": data})

def u_viewApprovedGuide_get(request):
    data = Request.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request, "user/user view approved guide.html", {"data": data})

def u_viewApprovedGuide_post(request):
    search = request.POST['textfield']
    data = Guide.objects.filter(status="approved", name__icontains=search)
    return render(request, "user/user view approved guide.html", {"data": data})


def userhome_get(request):
    # data=Videos.objects.all()

    return render(request,"user/userindex.html",)

def userhomeindex_get(request):
    data=Videos.objects.all()

    return render(request,"user/userindexhome.html",{"data":data})



#####################################################quide chat with user

def chat1(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "guide/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})

def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_id, "date": i.date, "from": i.FROM_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})



##############################################3user chat with quide




def chat2(request,id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Guide.objects.get(LOGIN=cid)

    return render(request, "user/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})

def chat_view2(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Guide.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROM_id=fromid, TO_id=toid) | Q(FROM_id=toid, TO_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_id, "date": i.date, "from": i.FROM_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send2(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_id = toid
    chatobt.FROM_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})