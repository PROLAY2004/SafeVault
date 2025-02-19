from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from manager_app.models import userdata,Verification_otp,logs,credentials
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail
import random

# Index page
def index(request):
    return redirect("Home")


#Home page
def home(request):
    if(request.session.get('id')):
        context = {
            "session" : 1
        }
        return render(request,'home.html',context)
    else:
        context = {
            "session" : 0
        }
        return render(request,'home.html',context)


#about page
def about(request):
    if(request.session.get('id')):
        context = {
            "Copyright" : datetime.now().year,
            "session" : 1
        }
        return render(request,'about.html',context)
    else:
        context = {
            "Copyright" : datetime.now().year,
            "session" : 0
        }
        return render(request,'about.html',context)


#Contact page
def contact(request):
    if(request.session.get("id")):
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        if(name and email and msg):
            body = "From " + name + " ( " + email + " ) " + " Message = " + msg
            send_mail(
                "Contact Us - SafeVault Response",
                body,
                "safevault@prolay.whf.bz",
                ['prolayhalder2004@gmail.com'],
                fail_silently= False,
            )
            return render(request,"contact.html",{"message" : "Email Sent Successfully.","session" : 1})
        else:
            context = {
                "session" : 1,
            }
            return render(request,'contact.html',context)
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        if(name and email and msg):
            body = "From " + name + " ( " + email + " ) " + " Message = " + msg
            send_mail(
                "Contact Us - SafeVault Response",
                body,
                "safevault@prolay.whf.bz",
                ['prolayhalder2004@gmail.com'],
                fail_silently= False,
            )
            return render(request,"contact.html",{"message" : "Email Sent Successfully.","session" : 0})
        else:
            context = {
                "session" : 0
            }
            return render(request,'contact.html',context)


#Register page
def signup(request):
    if(request.session.get('id')):
        return redirect("Home")
    else:
        name = request.POST.get("username")
        mail = request.POST.get("gmail")
        num = request.POST.get("mobile")
        password = request.POST.get("password")
    
        info = request.POST.get("data")
        a = request.POST.get("a")
        b = request.POST.get("b")
        c = request.POST.get("c")
        d = request.POST.get("d")
        if(a and b and c and d):
            lst = info.split('&')
            name = lst[0]
            mail = lst[1]
            num = lst[2]
            password = lst[3]
            abcd = a+b+c+d
            otp_lst = Verification_otp.objects.filter(email = mail)
            if(Verification_otp.objects.filter(otp = abcd , email = mail ).exists()):
                if(abcd == otp_lst[len(otp_lst)-1].otp):
                    hashed_password = make_password(password)
                    userdata.objects.create(name=name,email=mail,mobile=num,password=hashed_password)
                    current_time = datetime.now()
                    logs.objects.create(operation = "Account Created", data = name, time = current_time )
                    return redirect("Authentication")
                else:
                    info = name+"&"+mail+"&"+num+"&"+password
                    context={
                        "bool" : 1,
                        "message" : "OTP Expired <br><br>",
                        "info" : info,
                        "name":name,
                        "mail":mail, 
                        "num":num, 
                        "password":password
                    } 
                    return render(request,'signup.html',context)
            else:
                info = name+"&"+mail+"&"+num+"&"+password
                context={
                    "bool" : 1,
                    "message" : "Invalid OTP <br><br>",
                    "info" : info,
                    "name":name,
                    "mail":mail, 
                    "num":num, 
                    "password":password
                } 
                return render(request,'signup.html',context)
        elif(name and mail and num and password):
            if(userdata.objects.filter(name=name).exists()):
                return render(request,'signup.html',{"message" : "Username already exist.","bool" : 0})
            elif(userdata.objects.filter(email=mail).exists()):
                return render(request,"signup.html",{"message" : "Email already exists.","bool" : 0})
            elif(userdata.objects.filter(mobile=num).exists()):
                return render(request,"signup.html",{"message":"Mobile Number already exists.","bool" : 0})  
            else:
                if(len(num)==10):
                    key = random.randint(1000,9999)
                    Verification_otp.objects.create(otp = key, email = mail)
                    current_time = datetime.now()
                    logs.objects.create(operation = "Signup OTP sent", data = name, time = current_time )
                    send_mail(
                        "OTP for verification",
                        "Your OTP is "+ str(key),
                        "safevault@prolay.whf.bz",
                        [mail],
                        fail_silently=True,
                        )
                    info = name+"&"+mail+"&"+num+"&"+password
                    return render(request,"signup.html",{"bool" : 1,"info" : info, "name":name, "mail":mail, "num":num, "password":password})
                else:
                    return render(request,"signup.html",{"message":"Mobile Number should be 10 digits.","bool" : 0})
        else:
            return render(request,'signup.html',{"bool" : 0})


#Forgot Password Verification
def verify(request):
    if(request.session.get('id')):
        return redirect("Home")
    else:
        mail = request.POST.get("email")
        a = request.POST.get("a")
        b = request.POST.get("b")
        c = request.POST.get("c")
        d = request.POST.get("d")
        if(a and b and c and d):
            abcd = a+b+c+d
            otp_lst = Verification_otp.objects.filter(email = mail)
            if(Verification_otp.objects.filter(otp = abcd , email = mail ).exists()):
                if(abcd == otp_lst[len(otp_lst)-1].otp):
                    url = "Forgot/" + abcd
                    return redirect(url)
                else:
                    context={
                        "bool" : 1,
                        "message" : "OTP Expired <br><br>",
                        "mail" : mail
                    } 
                    return render(request,'forgot.html',context)
            else:
                context={
                    "bool" : 1,
                    "message" : "Invalid OTP <br><br>",
                    "mail" : mail
                } 
                return render(request,'forgot.html',context)
        elif(mail):
            if(userdata.objects.filter(email = mail).exists()):
                key = random.randint(1000,9999)
                Verification_otp.objects.create(otp = key , email = mail)
                current_time = datetime.now()
                name = userdata.objects.get(email = mail).name
                logs.objects.create(operation = "Reset OTP sent", data = name, time = current_time )
                send_mail(
                    "OTP for verification",
                    "Your OTP is "+ str(key),
                    "safevault@prolay.whf.bz",
                    [mail],
                    fail_silently=True,
                )
                context = {
                    "bool" : 1, 
                    "mail" : mail,
                }
                return render(request,'forgot.html',context)
            else:
                return render(request,'forgot.html',{"message" : "Email does not exists.","bool" : 0})
        else:
            return render(request,'forgot.html',{"bool" : 0})


#Forgot Password Update Page
def update(request,value):
    if(request.session.get("id")):
        return redirect("Home")
    else:
        otp = value
        email = Verification_otp.objects.get(otp = value).email
        if(Verification_otp.objects.filter(otp = otp).exists()):
            new = request.POST.get("password")
            if(new):
                user = userdata.objects.get(email = email)
                if(check_password(new,user.password)):
                    return render(request,"update.html",{"message":"Password can't be same as previous."})
                else:
                    hashed_new = make_password(new)
                    user.password = hashed_new
                    user.save()
                    current_time = datetime.now()
                    logs.objects.create(operation = "Password Reset", data = user.name, time = current_time )
                    return redirect("Authentication")
            else:
                return render(request,"update.html")
        else:
            return redirect("Verification")


#Authentication page
def signin(request):
    if(request.session.get('id')):
        return redirect("Home")
    else:
        name = request.POST.get("uname")
        password = request.POST.get("pword")
        if(name and password):
            if(userdata.objects.filter(name = name).exists()): 
                user = userdata.objects.get(name = name)
                if(check_password(password,user.password)):
                    request.session['id'] = user.id
                    request.session['uname'] = user.name
                    current_time = datetime.now()
                    logs.objects.create(operation = "Login", data = name, time = current_time )
                    return redirect("Dashboard")
                else:
                    context={
                        "message" : "Invalid Credentials."
                    }
                    return render(request,"signin.html",context)
            else:
                context={
                    "message" : "Invalid Credentials."
                }
                return render(request,"signin.html",context)
        else:
            return render(request,'signin.html')


#Logout Page
def logout(request):
    if(request.session.get("id")):
        name = request.session.get("uname") 
        current_time = datetime.now()
        logs.objects.create(operation = "Logout", data = name, time = current_time )
        request.session.flush()
        return redirect("Authentication")
    else:
        return redirect("Home")


#Dashboard
def dashboard(request):
    if(request.session.get("id")):
        
        img = request.FILES.get("image")
        name = request.session.get('uname')
        website = request.POST.get("domain")
        username = request.POST.get("username")
        credential_pass = request.POST.get("password")
        user = userdata.objects.get(name = name)
        if(img):
            user.image.delete()
            user.image = img
            user.save()
            current_time = datetime.now()
            logs.objects.create(operation = "Profile image changed", data = name, time = current_time )
            return redirect("Dashboard")

        if(website and username and credential_pass):
            credentials.objects.create(domain = website, domain_username = username, username = name, password = credential_pass)
            string = website + " credential added"
            current_time = datetime.now()
            logs.objects.create(operation = string, data = name, time = current_time )
            return redirect("Dashboard")
        email = user.email
        num = user.mobile
        activity = logs.objects.filter(data = name)
        show = credentials.objects.filter(username = name)
        context = {
            "user" : name,
            "email" : email,
            "mobile" : num,
            "image" : user.image,
            "activity" : activity,
            "credentials" : show
        }
        return render(request,'dashboard.html',context)
    
    else:
        return HttpResponse("Please Login")


#Profile Page
def profile(request,name):
    if(request.session.get("uname")==name):
        image = request.FILES.get("image")
        new_name = request.POST.get("name")
        user = userdata.objects.get(name = name)
        if(image and new_name):
            user.image.delete()
            user.image = image
            user.save()
            current_time = datetime.now()
            logs.objects.create(operation = "Profile info Updated", data = name, time = current_time )
            url = "/Dashboard/"+name
            return redirect(url)

        
        context={
            "user" : name,
            "email" : user.email,
            "mobile" : user.mobile,
            "image" : user.image,
        }
        return render(request,"profile.html",context)
    else:
        return redirect("Dashboard")



def activity(request,name):
    if(request.session.get("uname")==name):
        user = userdata.objects.get(name = name)
        log = logs.objects.filter(data = name)
        context={
            "image" : user.image,
            "history" : log
        }
        return render(request,"activity.html",context)
    else:
        return redirect("Dashboard")
