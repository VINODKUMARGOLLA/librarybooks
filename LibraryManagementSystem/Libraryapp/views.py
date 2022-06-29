from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
from Libraryapp.models import books


def home(request):
    return render(request,'index.html')

def log_read(request):
    user_name = request.POST["txtname"]
    user_pswd = request.POST["txtpswd"]
    user = authenticate(username=user_name, password=user_pswd)
    return render(request,'admin_home.html')


def Books(request):
    data = books.objects.all()

    return render(request,"Allbooks.html",{'data':data})


def ahome(request):
    return render(request,'admin_home.html')


def New(request):
    return render(request,"Newbook.html")


def add_book(request):
    l1=books()
    l1.book_name=request.POST['bname']
    l1.book_auther_name=request.POST['aname']
    l1.book_price=request.POST['price']
    l1.book_description=request.POST['bookd']
    l1.save()

    return redirect('books')


def delete_book(request,id):
    l1= books.objects.get(id=id)
    l1.delete()
    return redirect('books')


def update_book(request,id):
    l2= books.objects.get(id=id)

    if request.method == 'POST':
        l2.book_name = request.POST['bname']
        l2.book_auther_name = request.POST['aname']
        l2.book_price = request.POST['price']
        l2.book_description = request.POST['bookd']
        l2.save()

        return redirect('books')

    return render(request,'updatebook.html',{'data':l2})