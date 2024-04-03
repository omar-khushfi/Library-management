from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
def index(request):
    if request.method == 'POST':
        add_book=bookforms(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save();
        add_category=categoryform(request.POST);
        if add_category.is_valid():
           add_category.save();

    context={
        'books':book.objects.all(),
        'category':category.objects.all(),  
        'form':bookforms(),
        'formcat':categoryform(),
        'allbooks':book.objects.filter(active=True).count(),
        'booksold':book.objects.filter(state='sold').count(),
        'bookrental':book.objects.filter(state='rental').count(),
        'bookavailble':book.objects.filter(state='availble').count(),
        
    }
    return render(request,'pages/index.html',context)

def books(request):
    title=None;
    search=book.objects.all();
    if 'search_name' in request.GET:
        title=request.GET['search_name'];
        if title:
            search=search.filter(title__icontains=title)

    context={
        'formcat':categoryform(),
        'books':search,
        'category':category.objects.all(),
    }
    return render(request,'pages/books.html',context)


def update(request,id):
    book_id=book.objects.get(id=id);
    if request.method=='POST':
        book_save=bookforms(request.POST,request.FILES,instance=book_id);
        if book_save.is_valid():
            book_save.save();
            return redirect('/')
    else:
        book_save=bookforms(instance=book_id);
    context = {
        'form':book_save,
    }
    return render(request,'pages/update.html',context)

def delete(request,id):
    book_delete=get_object_or_404(book,id=id);
    if request.method == 'POST':
        book_delete.delete();
        return redirect('/');
    return render(request,'pages/delete.html') 
