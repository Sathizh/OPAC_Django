from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime,timedelta
# Create your models here.

def get_duedate():
	return datetime.today()+timedelta(days=14)

class Book(models.Model):
	name=models.CharField(max_length=80)
	author=models.CharField(max_length=30)
	ISBN=models.BigIntegerField(validators=[MinValueValidator(0),MaxValueValidator(9999999999999)],unique=True)
	Qty=models.IntegerField(validators=[MinValueValidator(0)])
	location=models.CharField(max_length=80)
	poster=models.ImageField(upload_to='poster/',default='default-book.jpg')
	book_choices=(('Book','Book'),('Artical','Artical'),('Digital','Digital'),('Journal','Journal'))
	category=models.CharField(max_length=10,choices=book_choices,blank=False)

	def __str__(self):
		return self.name
class Borrow(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	book=models.ForeignKey('OPAC_app.Book',on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)
	due_date=models.DateTimeField(default=get_duedate)
	class Meta:
		ordering =['due_date']
	def __str__(self):
		return self.user.username+' - '+ self.book.name