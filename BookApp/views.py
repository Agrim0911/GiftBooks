from django.shortcuts import render,redirect
from .models import Register,Books
from django.contrib import messages
import datetime
import pdb



def register(request):
    details = Register.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name',)
        phone_no = request.POST.get('phone_no',)
        email = request.POST.get('email',)
        password = request.POST.get('password',)
        address = request.POST.get('address',)
        pincode = request.POST.get('pincode',)
        city = request.POST.get('city',)
        state = request.POST.get('state',)
        country = request.POST.get('country',)
        detail = Register(name=name,phone_no=phone_no,email=email,password=password,address=address,pincode=pincode,city=city,state=state,country=country)
        detail.save()
        return redirect('/login')
    return render(request,'BookApp/register.html',{'details':details})

def login(request):
    try:
        if request.method == 'POST':
            global email
            email = request.POST.get('email',)
            password = request.POST.get('password',)            
            
            details = Register.objects.filter(email=email,password=password).get()      
            if len(details.email) > 0:
                return redirect("/loggedin") 
    except Register.DoesNotExist:
        messages.error(request,'Invalid Credentials')
    return render(request,'BookApp/login.html')

def index(request):
    details = Register.objects.all()
    return render(request,'BookApp/out_index.html',{'details':details})

def log_index(request):
    try:
        book2 = Books.objects.all()
        details = Register.objects.filter(email=email).get()
        return render(request,'BookApp/log_index.html',{'book2':book2,'details':details})
    except NameError:
        messages.error(request,'You need to log in in order to continue')
        return render(request,('BookApp/emailerror.html'))


def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        book_class = request.POST.get('book_class',)
        publisher = request.POST.get('publisher',)
        edition_year = request.POST.get('edition_year',)
        price = request.POST.get('price',)
        condition = request.POST.get('condition',)
        status = request.POST.get('status',)
        insert_date = request.POST.get('insert_date',)
        if insert_date == "":
            insert_date = datetime.date.today()
        cover_pic = request.POST.get('cover_pic',)
        detail = Books(name=name,cover_pic=cover_pic,book_class=book_class,publisher=publisher,edition_year=edition_year,price=price,condition=condition,status=status,insert_date=insert_date)
        detail.save()
        return redirect('/loggedin')
    book1 = Books.objects.all()
    details = Register.objects.filter(email=email).get()
    return render(request,'BookApp/add_book.html',{'book1':book1,'details':details})

def detail(request,id):
    book = Books.objects.get(id=id)
    details = Register.objects.filter(email=email).get()
    return render(request,'BookApp/detail.html',{'book':book,'details':details})

