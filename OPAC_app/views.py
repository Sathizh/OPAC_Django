from django.shortcuts import render,redirect
from . forms import BookForm
from .models import Book,Borrow
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
class AddBook(generic.CreateView):
	model=Book
	form_class=BookForm
	template_name='OPAC_app/AddBook.html'
	success_url=reverse_lazy('OPAC_app:index')
class HomePage(generic.TemplateView):
	template_name='OPAC_app/index.html'
# class BookDetail(generic.DetailView):
# 	model=Book
# 	template_name='OPAC_app/BookDetail.html'
class BorrowList(generic.ListView):
	model=Borrow
	template_name='OPAC_app/myhistory.html'
def DeleteBook(request,pk):
	book=Book.objects.get(pk=pk)
	borrow=Borrow.objects.filter(book=book)
	if borrow:
		return HttpResponse('<h3 class="alert alert-warninig">Same book copy is in circle,collect all the book and try later!</h3>')
	else:
		book.delete()
	return render(request,'OPAC_app/DeleteBook.html',{'book':book})
	
def BookDetail(request,pk):
	book=Book.objects.get(pk=pk)
	borrow=Borrow.objects.filter(book=book,user=request.user)
	if book.Qty > 0:
		empty= False
	else:
		empty= True
	return render(request,'OPAC_app/BookDetail.html',{'book':book,'borrow':borrow,'empty':empty})
def BorrowBook(request,pk):
	book=Book.objects.get(pk=pk)
	if request.method == 'POST':
		if book.Qty > 0:
			exist=Borrow.objects.filter(user=request.user,book=book)
			if exist:
				return HttpResponse('<h3 class="alert alert-warninig">Book not available now...</h3>')
				return redirect('OPAC_app:myhistory')
			else:
				borrow=Borrow()
				borrow.book=book
				borrow.user=request.user
				book.Qty-=1
				book.save()
				borrow.save()
		else:
			# return HttpResponse("<script>alert('book not available now!');</script>")
			return HttpResponse('<h3 class="alert alert-warninig">Book not available now...</h3>')
	return redirect('OPAC_app:myhistory')

def search(request):
	if request.method == 'POST':
		category=request.POST.get('category')
		query=request.POST.get('search')
		if query:
			result =Book.objects.filter(Q(name__icontains=query)|Q(ISBN__icontains=query),category=category)
		else:
			result = Book.objects.filter(category=category)
	else:
		reverse_lazy('OPAC_app:index')
	return render(request,'OPAC_app/search_result.html',{'result':result})

def ReturnBook(request,pk):
	book=Book.objects.get(pk=pk)
	borrow=Borrow.objects.get(book=book,user=request.user)
	if request.method == 'POST':
		book.Qty+=1
		book.save()
		borrow.delete()
	return redirect('OPAC_app:index')