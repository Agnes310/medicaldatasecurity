from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from blockchainconn import *
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import random
import time
from abeencrypt import *
# Create your views here.
import dropbox
import hashlib
import binascii
import random
import os
import base64
from Crypto.Cipher import AES
import random
import sys
def sha256(string_to_hash):
    a = hashlib.sha256(string_to_hash).hexdigest() 
    t=hex_to_binary(a)
    return t
def perms(l):
     k=[]
     
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
     #print len(k)
     a=k
     for i in range(len(k)):
         for j in range(len(k)):
             k[i],k[j]=k[j],k[i]
     up=""
     for i in k:
         up+="".join(i)
     s=""

     for i in range(len(l)):
         s+="*"
     s=list(s)
     res=""
     for i in range(0,len(s),2):
         s[i:i+2]=up[i:i+2]
         print ("".join(s))
     res+="".join(s)
     return res
def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(b) for b in binascii.unhexlify(h))  
def permrev(l):
     k=[]
     
     for i in range(0,len(l),4):
         k.append(l[i:i+4])
     a=k
     for i in range(len(k)-1,-1,-1):
         for j in range(len(k)-1,-1,-1):
             k[i],k[j]=k[j],k[i]
     up=""
     for i in k:
         up+="".join(i)
     s=""

     for i in range(len(l)):
         s+="*"
     s=list(s)
     res=""
     for i in range(len(s)):
         s[i]=up[i]
     res+="".join(s)
     return res


class Cipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs).encode("ascii")

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def __datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
al=[]
policy=[]
andl=[]
booly,zz1,yy1=0,0,0
orl=[]
abcd=0
tasks=[]
file_content=""
def home(request):
    return render(request,'login/login.html',{})

from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True)
def log(request):
    request.session.flush()
    return render(request,'login/login.html',{})
def signup(request):
    return render(request,'signup.html',{})
def ind(request):
    return render(request,'users/user_home.html',{})

def duind(request):
    return render(request,'datausers/user_home.html',{})

def dq1(request):
    pk, msk = setup()
    ob1=keyvals(pkv=pk,msk=msk)
    ob1.save()
    return render(request,'dq.html',{})
def dq2(request):
    return render(request,'kgf.html',{})

def accesspolicy(request):
    global tasks
    tasks = request.GET.getlist('d1[]')
    return HttpResponse('Success')

def newadmin(request):
    return render(request,'newadminhome.html',{})

def vb(request):
    global abcd
    global andl
    global orl
    andl=[]
    orl=[]
    abcd=0
    return render(request,'dataown.html',{})

def logval(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    role=request.POST.get("utype")
    mob=request.POST.get("mob")
    username=request.POST.get("username")
    password=request.POST.get("password")
    try:
        ob=users.objects.get(username=username,email=email)
        return HttpResponse("<script>alert('Duplicate entries found');window.location.href='/log/'</script>")
    except:
        t=sha256(password.encode("utf8"))
        print ("sha256")
        print (t)
        re=perms(t)
        print ("permutation")
        print (re)
        key=t[:32]
##        encrypted = encrypt(re, t)
        cipher = Cipher(key.encode("utf8"))

        encrypted = cipher.encrypt(re.encode("utf8"))
        print ("Encrypted")
        print (encrypted)
    try:
        if role=="Patients":
            ob=users(name=name,email=email,mob=mob,role=role,username=username,password=encrypted,status=0)
            ob.save()
        else:
            ob=users(name=name,email=email,mob=mob,role=role,username=username,password=encrypted,status=1)
            ob.save()
        return HttpResponse("<script>alert('Successfully Registered');window.location.href='/log/'</script>")
    except Exception as ex:
        print("Exception: ",ex)
        return HttpResponse("<script>alert('Already Registered');window.location.href='/log/'</script>")

def data(request):
    print("Data")
    return render(request,'data1.html',{"data":ob,"data1":ob1})

def dataownlog(request):
    return render(request,'users/user_home.html',{})

def otherslog(request):
    return render(request,'otherslog.html',{})

def selected(request):
    x=request.GET.get("d1")
    ob=role.objects.raw("select * from App_role where department='"+x+"'")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    return JsonResponse(data,safe=False)

def sig(request):
    return render(request,'users/user_home.html',{})

def valu(request):
    ob= files.objects.all()
    return render(request,'users/user_apps.html',{"files":ob})

def duvalu(request):
    ob= files.objects.all()
    return render(request,'datausers/user_apps.html',{"files":ob})


def sen(request):
    ob= users.objects.filter(role="User")
    
    return render(request,'users/user_upload.html',{"users":ob})

def newsen(request):
    ob=filedates.objects.raw("select * from App_filedates where approve=0 order by id desc limit 3;")
    
    return render(request,'send.html',{})

def cloudpage(request):
    print (request.session["user"])
    ab=""
    if request.session["user"]=="Admin":
        ab="Admin"
    else:
        ab=request.session["user"]
    return render(request,'cloudpagelog.html',{"zx":ab})

def saving(request):
    try:
        global tasks
        s = request.FILES["files2"]
        print (s)
        if request.FILES["files2"]:
            uu = request.POST.get("user")
            fs = FileSystemStorage("App/static/files/")
            fs.save(s.name, s)
            filename ="App/static/files/"+s.name
            f=open(filename,"r")
            msg=f.read()
            f.close()
            print("username",request.session["user"])
            des=request.POST.get("desc")
            key=uu
            if len(key)>32:
                key=key[:32]
            elif len(key)<32 and len(key)>16:
                key=key[:16]
            elif(len(key)<16):
                key = key.ljust(16)
            cipher = Cipher(key.encode("utf8"))

            val = cipher.encrypt(msg.encode("utf8"))
            f=open("App/static/filesenc/"+s.name,"w")
            f.write(val)
            f.close()
            try:
                access_token = 'ttVqa5_XPaAAAAAAAAAAylEHHmcckHbfcG041udS0MqkXhFnA06ME-RbmjjmO_ul'
                transferData = TransferData(access_token)

                file_from = s.name
                file_to = '/test_dropbox/'+s.name  # The full path to upload the file to, including the file name

                # API v2
                transferData.upload_file(file_from, file_to)
            except Exception as ex:
                print("Exception: ",ex)
            
##            os.remove(s.name)
            deploying(s.name)
            createKey(key)
            oo = files(name=s.name,path="App/static/filesenc/"+s.name,desc=des,username=request.session["user"]).save()
            print("File Removed!")
        return HttpResponse("<script>alert('Uploaded Successfully');window.location.href='/sen/'</script>")
    except Exception as ex:
        print("Exception: ",ex)
        return HttpResponse("<script>alert('Failed to upload');window.location.href='/sen/'</script>")
    
def deprole(request):
    x=request.GET.get("d1")
    ob=role.objects.raw("select * from App_role where department='"+x+"'")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)

def inbpage(request):
    print (request.session["user"])
    return render(request,'inboxpage.html',{"zx":request.session["user"]})

def loginval(request):
    usernamelog=request.POST.get("username")
    passwordlog=request.POST.get("password")
    print(usernamelog, passwordlog)
    try:
        if usernamelog=="admin" and passwordlog=="admin":
            request.session["user"]="Admin"
            return render(request,'newadminhomelog.html',{})
        else:
            try:
                obj=users.objects.get(username=usernamelog)
                password=obj.password
                print(password)
                t=sha256(usernamelog.encode("utf8"))
                print (t)
                key= t[:32]
                cipher = Cipher(key.encode("utf8"))
                print("--")
                decrypted = cipher.decrypt(password)
                print ("Decrypted")
                print (decrypted)
                rek=permrev(decrypted)
                print(t==rek)
                if t==rek:
                    if obj.role=="Patients":
                        request.session["user"]=usernamelog
                        return HttpResponse("<script>alert('Success');window.location.href='/dataownlog/'</script>")
                    elif obj.role=="User":
                        request.session["user"]=usernamelog
                        return HttpResponse("<script>alert('Success');window.location.href='/duind/'</script>")
                    else:
                        return HttpResponse("<script>alert('Not a User Yet. Please Register');window.location.href='/log/'</script>")
                else:
                    return HttpResponse("<script>alert('Not a User Yet. Please Register');window.location.href='/log/'</script>")
            except Exception as ex:
                print("Ex: ",ex)
                return HttpResponse("<script>alert('Not a User Yet. Please Register');window.location.href='/log/'</script>")
    except Exception as ex:
        print("Exception: ",ex)
        return HttpResponse("<script>alert('Something Unusual happened. Try Again Later');window.location.href='/log/'</script>")
    
def approved(request):
    x=request.GET.get("d1")
    obj=stafc.objects.get(id=x)
    obj.approve=1
    obj.save()
    ob=stafc.objects.raw("select * from App_stafc where approve=0;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)

def verify(request):
    ob=stafc.objects.raw("select * from App_stafc where approve=0;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print (data)
    return JsonResponse(data,safe=False)


def reqfile(request):
    ob=askey.objects.raw("select * from App_askey order by id desc limit 5")
    return render(request,'keyreq.html',{"data":ob})

def download(request):
    fn=request.POST.get("path")
    name=request.POST.get("name")
    desc=request.POST.get("desc")
    username=request.POST.get("username")
    
    try:
        access_token = 'ttVqa5_XPaAAAAAAAAAAylEHHmcckHbfcG041udS0MqkXhFnA06ME-RbmjjmO_ul'
        dbx = dropbox.Dropbox(access_token)
        metadata, f = dbx.files_download('/test_dropbox/'+fn)
        con=f.content
        print(con)
    except Exception as ex:
        print("Exception",ex)
    deploying(name)
    getKey(0)
    out = open(fn, 'r')
    cc = out.read()
    print("--",cc,fn)
    out.close()
    key=username
    if len(key)>32:
        key=key[:32]
    elif len(key)<32 and len(key)>16:
        key=key[:16]
    elif(len(key)<16):
        key = key.ljust(16)
    cipher = Cipher(key.encode("utf8"))
    decrypted = cipher.decrypt(cc)
    print("Encrypted Content: ",cc)
    print("Decrypted Content: ",decrypted)
    filename = name
    response = HttpResponse(decrypted, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response
