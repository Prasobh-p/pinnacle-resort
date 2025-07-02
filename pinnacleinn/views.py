import random

from django.shortcuts import render,redirect
from pinnacleinn.models import Condb
from backend.models import Accomdb,Roomdb,Fooddb,Fooditeamsdb
from pinnacleinn.models import Registerdb
from django.contrib import messages
from django.http import HttpResponse
from pinnacleinn.models import Hostdb,Paymentdb
from django.shortcuts import get_object_or_404
import razorpay





# Create your views here.


def Homepage(req):
    Adata = Accomdb.objects.all()
    return render(req,"HOME.html",{'Adata':Adata})

def Aboutpage(req):
    return render(req,"About.html")

def Roompage(req):
    Adata = Accomdb.objects.all()
    rdata = Roomdb.objects.all()
    return render(req,"Rooms.html",{'Adata':Adata,'rdata':rdata})

def Filteredroom(req, Adata):
    rdata=Roomdb.objects.filter(ROOMTYPE=Adata)
    Adata=Accomdb.objects.all()
    return render(req,"Filtered_room.html",{'Adata':Adata, 'rdata':rdata})


def Diningpage(req):
    food = Fooddb.objects.all()
    return render(req,"Dining.html",{'food':food})



def contactpage(req):
    return render(req,"Contact.html")

def Singleroompage(req,r_id):
    rdata = Roomdb.objects.get(id=r_id)
    Adata = Accomdb.objects.all()
    return render(req,"Singleroom.html",{'rdata':rdata,'Adata':Adata})
def Bookingpage(req):
    return render(req,"Booking.html")

def Registerpage(req):
    return render(req,"Register.html")


def userlogin(request):
    if request.method == "POST":
        Pname = request.POST.get('username')
        Eemail = request.POST.get('EMAIL')
        Pass = request.POST.get('password')
        Cpass = request.POST.get("confirmpassword")


        if Registerdb.objects.filter(Name=Pname).exists():
            messages.warning(request, "User already exists.")
            return redirect("Registerpage")

        if Registerdb.objects.filter(Email=Eemail).exists():
            messages.warning(request, "Email already exists.")
            return redirect("Registerpage")

        Registerdb.objects.create(Name=Pname, Email=Eemail, Password=Pass, ConfirmPassword=Cpass)
        messages.success(request, "Registered successfully.")
        return redirect("loginpage")


def loginpage(request):
    return render(request,"Userlogin.html")



def loginn(request):
    if request.method == "POST":
        unam = request.POST.get('unam')
        pas = request.POST.get('pas')
        if Registerdb.objects.filter(Name=unam, ConfirmPassword=pas).exists():
            request.session["Name"] = unam
            request.session["ConfirmPassword"] = pas
            return redirect('Homepage')
        else:
            return redirect('loginpage')
    else:
        return redirect('loginpage')


def logout(request):
    del request.session["Name"]
    del request.session["ConfirmPassword"]
    return redirect(Homepage)




def Bookingdate(request, id):
    rdata = get_object_or_404(Roomdb, pk=id)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        customers = request.POST.get('customers')


        if checkin and checkout and customers:
            booking = Hostdb(
                roomname=rdata.NAME,
                checkin_date=checkin,
                checkout_date=checkout,
                customers=customers,
                total_price=rdata.PRICE
            )
            booking.save()
            request.session['PRICE'] = str(rdata.PRICE)
            messages.success(request, "Booking successful!")
            return redirect("paymentpage")

    return render(request, 'paymentpage', {'rdata': rdata})


def paymentpage(request):
    payname = None
    pemail = None
    price = request.session.get('PRICE')

    user = Registerdb.objects.filter(Name=request.session.get('Name')).first()
    if user:
        payname = user.Name
        pemail = user.Email





    return render(request, "paymentpage.html", {
        "payname": payname,
        "pemail": pemail,
        "price": price
    })

def orderingfinal(request):
    customer = Paymentdb.objects.order_by('-id').first()
    charge = float(customer.Originaltotal_price)  # Removed try block
    amount = int(charge * 100)
    cash = str(amount)

    payment = None  # Define in outer scope

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_ejwy1yBgEPDZ2A', 'NKOMC4fph178a9Cf0Mr2aFrn'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})

    return render(request, "orderingfinal.html", {
        'customer': customer,
        'cash': cash,
        'charge': charge,
        'payment': payment
    })


def orderdetils(request):
    if request.method == "POST":
        hostname = request.session['Name']
        mobnum = request.POST.get("MObile")
        paymail = request.POST.get("paymail")
        proof = request.FILES.get("PRoof")
        address = request.POST.get("ADresses")
        requerments = request.POST.get("REquerments")
        total_price = request.session.get('PRICE')

        Payment = Paymentdb(Hostname=hostname, Mobnum=mobnum,Paymail=paymail, Proof=proof,Address=address, Requerments=requerments,Originaltotal_price=total_price)
        Payment.save()
        return redirect(orderingfinal)



