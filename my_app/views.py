from django.shortcuts import render
from django.http import HttpResponse

import pyrebase
# import pyqrcode
# import png
# from pyqrcode import QRCode
import qrcode
config={
    "apiKey": "AIzaSyDdheLeY7Yw-Mam3w2IKnbvgd1Hh7LUFdk",
    "authDomain": "niyukthi-be5f6.firebaseapp.com",
    "projectId": "niyukthi-be5f6",
    "databaseURL": "https://niyukthi-be5f6-default-rtdb.firebaseio.com/",
    'storageBucket': "niyukthi-be5f6.appspot.com",
    'messagingSenderId': "700335121802",
    "appId": "1:700335121802:web:5971b337078f7060139473",
    'measurementId': "G-LS4WN48MDJ"
}
firebase = pyrebase.initialize_app(config)
storage =firebase.storage()
authe = firebase.auth()
db = firebase.database()

def index(request):

    return render(request,'index.html')

def newIndex(request):
    return render(request,'new.html')

def login(request):
    return render(request,'login.html')


def register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    dob = request.POST.get('dob')
    print(name,email,password,phone,address,dob)
    context = {}
    context["Name"]=name
    context["Email"]=email
    context["Phone"]=phone
    context["Address"]=address
    context["DOB"]=dob
    try:
        # user=authe.create_user_with_email_and_password(email,password)
      
        db.child("User").child(phone).child("Name").push(name)
        db.child("User").child(phone).child("Email").push(email)
        db.child("User").child(phone).child("Password").push(password)
        db.child("User").child(phone).child("address").push(address)
        db.child("User").child(phone).child("dob").push(dob)
        # user=authe.create_user_with_email_and_password(email,password)
        # uid = user['localId']
        # idtoken = request.session['uid']
        # db.child("new").child(idtoken).push(d)
        # print("User Id : ",uid)
    except:
        
        return render(request,'login.html')
    # session_id=phone
    # request.session['phone']=str(session_id)
    data1 ={"name":name,"phone":phone,"email":email}
    img =qrcode.make(data1)
    img.save('static/qrcode/qrcode.png')
    path_img = "static/qrcode/qrcode.png" 
    print(path_img)
    path_on_cloud = phone + "/"+phone+".png"
    storage.child(path_on_cloud).put(path_img) 
    storage.child(path_on_cloud).download("static/qrcode/qr.png") 
    return render(request,'new.html',context)

def signin(request):
    e = request.POST.get('phone')
    p = request.POST.get('password_1')
    users = db.child("User").get().each()
    name=db.child("User").child(e).child("Name").get().each()
    email=db.child("User").child(e).child("Email").get().each()
    address=db.child("User").child(e).child("address").get().each()
    dob=db.child("User").child(e).child("dob").get().each()
    for i in name:
        n = i.val()
    for i in email:
        em = i.val()
    for i in address:
        a = i.val()
    for i in dob:
        d = i.val()
    context = {}
    context["Name"]=n
    context["Email"]=em
    context["Phone"] = e
    context["Address"]=a
    context["DOB"]=d
   

    passw=""
    users = db.child("User").get().each()
    password = db.child("User").child(e).child("Password").get().each()
    for i in password:
        passw = i.val()
    phone =[]
    for i in users:
        phone.append(i.key())
    try:
        if e in phone and (p == passw) :
            print("Success")
        else:
            raise Exception()
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,'login.html',{"message":message})
    data1 ={"name":n,"phone":e,"email":em}
    img =qrcode.make(data1)
    img.save('static/qrcode/qrcode.png')
    # path_img = "static/qrcode/qrcode.png" 
    # print(path_img)
    path_on_cloud = e + "/"+e +".png"
    # storage.child(path_on_cloud).put(path_img) 
    storage.child(path_on_cloud).download("static/qrcode/qr.png") 
    return render(request,'new.html',context)

def feedback(request):
    username = request.POST.get('user')
    email_id = request.POST.get('email_id')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    data = {"email":email_id,"subject":subject,"message": message}
    db.child("feedback").child(username).set(data)
    return render(request,'index.html')

def subscribe(request):
    email = request.POST.get('email')
    db.child("subscribes").push(email)
    return render(request,'index.html')

def appointment(request,phone):
    print(phone)
    Dermatology =[]
    ENT =[]
    General_Medicine =[]
    General_Surgery = []
    Ophthalmology =[]
    Orthopedics =[]
    Paediatrics =[]
    Psychiatry = []

    derm = db.child("Doctors").child("Dermatology").get().each()
    en  = db.child("Doctors").child("ENT").get().each()
    gm = db.child("Doctors").child("General Medicine").get().each()
    gs = db.child("Doctors").child("General Surgery").get().each()
    op = db.child("Doctors").child("Ophthalmology").get().each()
    ortho = db.child("Doctors").child("Orthopedics").get().each()
    paed = db.child("Doctors").child("Paediatrics").get().each()
    psych = db.child("Doctors").child("Psychiatry").get().each()
    for i in derm:
        Dermatology.append(i.key())
    for i in en:
        ENT.append(i.key())
    for i in gm:
        General_Medicine.append(i.key())
    for i in gs:
        General_Surgery.append(i.key())
    for i in op:
        Ophthalmology.append(i.key())
    for i in ortho:
        Orthopedics.append(i.key())
    for i in paed:
        Paediatrics.append(i.key())
    for i in psych:
        Psychiatry.append(i.key())
    return render(request,'appointment.html',{"Phone":phone,"Dermatology":Dermatology,"ENT":ENT,"General_Medicine":General_Medicine,"General_Surgery":General_Surgery,"Ophthalmology":Ophthalmology,"Orthopedics":Orthopedics,"Paediatrics":Paediatrics,"Psychiatry":Psychiatry})

def reset(request):
    return render(request, "forgot.html")

def postReset(request):
    phone = request.POST.get('phone')
    from twilio.rest import Client

    import random as r
    # function for otp generation
    def otpgen():
        otp=""
        for i in range(4):
            otp+=str(r.randint(1,9))
        return otp
    otp = otpgen()
    print(otp)
    account_sid = 'AC32005626822915566ac01677f6bb5587'
    auth_token = '9957901f911924f46fe23a3ce0a7f2a5'
    client = Client(account_sid, auth_token)
    names= db.child("User/"+phone+"/Name").get().each()
    name=[]
    for i in names:
        name.append(i.val())
    phone="+91"+phone
    message = client.messages.create(
             body='Hi '+str(name)+ ',Your Resetting Password OTP is '+ otp ,
             from_='+13343841912',
             to=phone
         )
    return render(request, "otp.html", {"phone":phone})

def sendOTP(request,phone):
    otpRcvd = request.POST.get('otp')
    return render(request, "reset.html",{"phone":phone})

def PasswordRest(request,phone):
    phone = phone[3:13]
    password = request.POST.get('password')

    db.child("User/"+phone+"/Password").remove()
    db.child("User/"+phone+"/Password").push(password)
    return render(request, "login.html")


# def sendAppointmentSMS(request,phone):
#     print("inside sendAppointmentSMS")
#     return render(request,"appointment.html",{"phone":phone})



def signup(request):
    return render(request,"signup.html")

# def qr(request,name,email,address,dob,phone):
#     # print("Data :",name,email,address,dob)
#     data1 ={"name":name,"email":email,"address":address,"dob":dob,"phone":phone}
#     img =qrcode.make(data1)
#     img.save('static/qrcode/qrcode.png')
#     # qr = qrcode.QRCode(
#     #     version=1,
#     #     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     #     box_size=10,
#     #     border=4,
#     # )
#     # qrcode.add_data(data1)

#     # # qrcode.add_data(data1)
#     # qrcode.make(data1)

#     # img = qrcode.make_image()

#     # img.save('123.png')
#     return render(request,'new.html',{"img":img,"data":data1})



def logout(request):
    # try:
    #     del request.session['id']
    # except KeyError:
    #     pass
    return render(request,'index.html')


def appointPatient(request):
    date = request.POST.get('date')
    print(date)
    return render(request,'appointment.html')  

def backToHome(request,Phone):
    print(Phone)
    name=db.child("User").child(Phone).child("Name").get().each()
    email=db.child("User").child(Phone).child("Email").get().each()
    for i in name:
        n = i.val()
    for i in email:
        em = i.val()
    data1 ={"name":n,"phone":Phone,"email":em}
    img =qrcode.make(data1)
    img.save('static/qrcode/qrcode.png')
    context = {}
    context["Name"]=n
    context["Email"]=em
    context["Phone"] = Phone
    return render(request,'new.html',context)
def myAppointment(request, phone):
    print(phone)
    return render(request, 'myAppointment.html', {"phone": phone})