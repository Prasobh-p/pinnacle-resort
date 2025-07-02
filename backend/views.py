from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from backend.models import Accomdb,Roomdb,Fooddb,Fooditeamsdb



# Create your views here.


def indexpage(req):
    return render(req, "index.html")


def add_accommodationpage(req):
    return render(req, "add_accommodation.html")


def save_accommodationpage(req):
    if req.method == "POST":
        Anam = req.POST.get("Ana")
        Aimg = req.FILES.get("Aimage")
        Adesc = req.POST.get("Adescription")
        obj = Accomdb(NAME=Anam, IMAGE=Aimg, DESCRIPTION=Adesc)
        obj.save()
    return redirect('add_accommodationpage')


def displaypage(req):
    data=Accomdb.objects.all()
    return render(req, "display_accommodation.html", {'data': data})

def editdata(req,accid):
    data = Accomdb.objects.get(id=accid)
    return render(req,"editpage.html",{'data':data})



def updatedata(req,accid):
    if req.method =="POST":
        Anam = req.POST.get("Ana")
        Adesc =req.POST.get("Adescription")

        try:
            Aimg=req.FILES['Aimage']
            fs=FileSystemStorage()
            file=fs.save(Aimg.name,Aimg)
        except:
            file=Accomdb.objects.get(id=accid).IMAGE
    Accomdb.objects.filter(id=accid).update(IMAGE=file, NAME=Anam, DESCRIPTION=Adesc)
    return redirect(displaypage)


def deletedata(req,accid):
    data=Accomdb.objects.filter(id=accid)
    data.delete()
    return redirect(displaypage)


def add_roomspage(req):
    data=Accomdb.objects.all()
    return render(req,'add_rooms.html',{'data':data})

def save_roompage(req):
    if req.method == "POST":
        Rtyp = req.POST.get("Roomtype")
        Rnam = req.POST.get("Roomname")
        Rpri = req.POST.get("Rprice")
        Rimg = req.FILES.get("Rimage")
        Rbe = req.POST.get("Rbed")
        Ram = req.POST.get("Rame")
        Rvie = req.POST.get("Rview")
        Rpoo = req.POST.get("Rpool")
        obj1 = Roomdb(ROOMTYPE=Rtyp,NAME=Rnam,PRICE=Rpri,IMAGE=Rimg,BEDDING=Rbe,AMENITIES=Ram,VIEWS=Rvie,POOL=Rpoo)
        obj1.save()
    return redirect("add_roomspage")

def displayroompage(req):
    iteam = Roomdb.objects.all()
    return render(req,"display_room.html",{'iteam':iteam})

def edit_roompage(req, Rid):
    iteam = Roomdb.objects.get(id=Rid)
    data = Accomdb.objects.all()
    return render(req,'Edit_roompage.html',{'iteam':iteam,'data':data})


def update_roompage(req,Rid):
    if req.method =="POST":
        Rtyp = req.POST.get("Roomtype")
        Rnam = req.POST.get("Roomname")
        Rpri = req.POST.get("Rprice")
        Rbe = req.POST.get("Rbed")
        Ram = req.POST.get("Rame")
        Rvie  = req.POST.get("Rview")
        Rpoo = req.POST.get("Rpool")

        try:
            Rimg = req.FILES['Rimage']
            fs = FileSystemStorage()
            file = fs.save(Rimg.name,Rimg)
        except:
            file = Roomdb.objects.get(id=Rid).IMAGE
    Roomdb.objects.filter(id=Rid).update(IMAGE=file,ROOMTYPE=Rtyp,NAME=Rnam,PRICE= Rpri,BEDDING=Rbe,VIEWS=Rvie,POOL=Rpoo,AMENITIES=Ram)
    return redirect('displayroompage')



def delete_roompage(req,Rid):
    iteam = Roomdb.objects.filter(id=Rid)
    iteam.delete()
    return redirect('displayroompage')


def loginpage(req):
    return render(req,"loginpage.html")


def adminlogin(req):
    if req.method == "POST":
        un=req.POST.get("username")
        pas=req.POST.get("pass")
        if User.objects.filter(username__contains=un).exists():
            x= authenticate(username=un,password=pas)
            if x is not None :
                login(req,x)
                req.session['username']=un
                req.session['password']=pas
                return redirect(indexpage)
            else:
                return redirect(loginpage)

        else:
            return redirect(loginpage)

def adminlogout(req):
    del req.session ['username']
    del req.session ['password']
    return redirect(loginpage)


def add_foodtype(req):
    return render(req,'add_food.html')


def save_food(req):
    if req.method == "POST":
        Fnam = req.POST.get("Fna")
        Fimg = req.FILES.get("Fimage")
        Fdesc = req.POST.get("Fdescription")
        Fobj = Fooddb(FNAME=Fnam, FIMAGE=Fimg, FDESCRIPTION=Fdesc)
        Fobj.save()
    return redirect('add_foodtype')


def displayfoodpage(req):
    Fdata = Fooddb.objects.all()
    return render(req, "display_food.html", {'Fdata': Fdata})


def editfooddata(req,fooid):
    Fdata = Fooddb.objects.get(id=fooid)
    return render(req,"editfood.html",{'Fdata': Fdata})

def updatefooddata(req,fooid):
    if req.method =="POST":
        Fnam = req.POST.get("Fna")
        Fdesc =req.POST.get("Fdescription")

        try:
            Fimg=req.FILES['Fimage']
            fs=FileSystemStorage()
            file=fs.save(Fimg.name,Fimg)
        except:
            file=Fooddb.objects.get(id=fooid).IMAGE
    Fooddb.objects.filter(id=fooid).update(FIMAGE=file, FNAME=Fnam, FDESCRIPTION=Fdesc)
    return redirect(displayfoodpage)

def deletefooddata(req,fooid):
    Fdata=Fooddb.objects.filter(id=fooid)
    Fdata.delete()
    return redirect(displayfoodpage)


def addfooditeams(req):
    Fdata=Fooddb.objects.all()
    return render(req,'add_foodtype.html',{'Fdata':Fdata})

def save_fooditeams(req):
    if req.method == "POST":
        ftyp = req.POST.get("foodtype")
        fnam = req.POST.get("foodname")
        fpri = req.POST.get("foodprice")
        fimg = req.FILES.get("foodimage")
        fdesc = req.POST.get("fdescription")
        obj2 = Fooditeamsdb(FOODTYPE=ftyp,FONAME=fnam,FOPRICE=fpri,FOIMAGE=fimg,FODESCRIPTION=fdesc,)
        obj2.save()
    return redirect("addfooditeams")


def displayfooditeams(req):
    foods = Fooditeamsdb.objects.all()
    return render(req, "displayfooditeams.html", {'foods': foods})



def edit_foodpage(req, Bid):
    foiteam = Fooditeamsdb.objects.get(id=Bid)
    Fdata = Fooddb.objects.all()
    return render(req,'Edit_fooditeampage.html',{'foiteam':foiteam,'Fdata':Fdata})


def update_foodpage(req,Bid):
    if req.method =="POST":
        ftyp = req.POST.get("foodtype")
        fnam = req.POST.get("foodname")
        fpri = req.POST.get("fprice")
        fdesc = req.POST.get("fdescription")

        try:
            fimg = req.FILES['fimage']
            fs = FileSystemStorage()
            file = fs.save(fimg.name,fimg)
        except:
            file = Fooditeamsdb.objects.get(id=Bid).FOGIMAGE
    Fooditeamsdb.objects.filter(id=Bid).update(FOIMAGE=file,FOODTYPE=ftyp,FONAME=fnam,FOPRICE= fpri,FODESCRIPTION=fdesc)
    return redirect('displayfooditeams')


def delete_foodpage(req,Bid):
    foiteam = Fooditeamsdb.objects.filter(id=Bid)
    foiteam.delete()
    return redirect('displayfooditeams')












