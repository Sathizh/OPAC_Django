from django.urls import path
from . import views
app_name='OPAC_app'

urlpatterns=[
			path('',views.HomePage.as_view(),name='index'),
			path('addbook/',views.AddBook.as_view(),name='AddBook'),
			path('search_result/',views.search,name='search_result'),
			# path('BookDetail/<int:pk>/',views.BookDetail.as_view(),name='BookDetail'),
			path('BookDetail/<int:pk>',views.BookDetail,name="BookDetail"),
			path('Borrow/<int:pk>/',views.BorrowBook,name='Borrow'),
			path('myhistory/',views.BorrowList.as_view(),name='myhistory'),
			path('return/<int:pk>/',views.ReturnBook,name="return"),
			path('DeleteBook/<int:pk>/',views.DeleteBook,name="DeleteBook"),
]