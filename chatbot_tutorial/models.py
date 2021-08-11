from django.db import models

# Create your models here.
class CallInfo(models.Model):
	id = models.BigAutoField(primary_key=True)
	user_id = models.CharField(max_length=25, verbose_name="User Id") 
	Button_name = models.CharField(max_length=100, verbose_name="Button name")
	No_Calls = models.IntegerField(default=0, verbose_name="No of Calls")  
