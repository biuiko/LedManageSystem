from django.db import models

# Create your models here.
class Custom(models.Model):
	user_name = models.CharField(max_length = 100)
	user_password = models.CharField(max_length = 100)
	def __str__(self):
		return self.user_name

class LedNumber(models.Model):
	custom = models.ForeignKey(Custom,on_delete=models.CASCADE)
	led_text = models.CharField(max_length= 100)	#LED内容
	address_text = models.CharField(max_length = 200,null = True,blank = True) #LED位置信息
	def __str__(self):
		return self.led_text

class Picture(models.Model):
	pic_url = models.CharField(max_length=500)
	custom = models.ForeignKey(Custom,on_delete=models.CASCADE)
	def __str__(self):
		return self.pic_url

class Video(models.Model):
	video_url = models.CharField(max_length=500)
	custom = models.ForeignKey(Custom,on_delete=models.CASCADE)
	def __str__(self):
		return self.video_url