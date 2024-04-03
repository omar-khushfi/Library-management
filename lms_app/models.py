from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50);
    def __str__(self):
        return self.name;
class book(models.Model):
   

    state_book=[
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold')
    ]
    category=models.ForeignKey(category,on_delete=models.PROTECT,null=True,blank=True);
    title=models.CharField(max_length=200);
    author=models.CharField(max_length=200,null=True,blank=True);
    photo_book=models.ImageField(upload_to='photo',null=True,blank=True);
    photo_author=models.ImageField(upload_to='photo',null=True,blank=True);
    pages=models.IntegerField(null=True,blank=True);
    price=models.DecimalField(max_digits=10,decimal_places=2);
    retal_price_day=models.DecimalField(max_digits=10,decimal_places=2);
    retal_period=models.IntegerField(null=True,blank=True);
    active=models.BooleanField(default=True);
    state=models.CharField(max_length=50,choices=state_book,null=True,blank=True);
    total_rental=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True);
    
    def __str__(self):
        return self.title;