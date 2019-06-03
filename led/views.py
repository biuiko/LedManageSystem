from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Custom,LedNumber,Picture,Video
import json
# Create your views here.

def index(request):
	'登录界面'
	return render(request,'led/index.html')
	#return HttpResponse("hello")

def choice_page(request,user_id):
	'登录后选择操作界面'
	user = Custom.objects.get(pk =user_id)
	led_list = user.lednumber_set.all()
	context = {
		'led_list' : led_list,
		'user_id':user_id
	}
	# return render(request,'led/choice_page.html',context)
	return render(request,'led/LedMessage.html',context)

def check(request):
	'检验用户登录'
	if not request.method == 'POST':
		return HttpResponse("你的打开方式有一点点奇怪哦")
	user_name = request.POST.get('username')
	user_password = request.POST.get('userpassword')
	if not all([user_name,user_password]):
		return render(request,'led/index.html')
	users = Custom.objects.all()
	for user in users:
		print("find")
		if user.user_name == user_name and user.user_password==user_password:
			return HttpResponseRedirect(reverse('led:choice', args = (user.id,)))
	return HttpResponse("我没有找到你诶")

def add_led_data(request,user_id):
	'处理添加数据成功后跳到选择操作界面'
	if request.method == 'POST':
		c = Custom.objects.get(pk = user_id)
		c.lednumber_set.create(led_text = request.POST.get('led_text'),address_text = request.POST.get('led_address'))
		c.save()
		led_list = c.lednumber_set.all()
		context = {
			'led_list' : led_list,
			'user_id':user_id
		}
		# return HttpResponseRedirect(reverse('led:choice',context))
		return render(request,'led/LedMessage.html',context)

def del_led_data(request,user_id):
	'删除成功后跳回LED管理界面'
	if request.method == 'POST':
		led_id = request.POST['led_choice']
		LedNumber.objects.filter(id=led_id).delete()
		user = Custom.objects.get(pk =user_id)
		led_list = user.lednumber_set.all()
		context = {
			'led_list' : led_list,
			'user_id':user_id
		}
		return render(request,'led/LedMessage.html',context)

def del_pic_data(request,user_id):
	'删除成功后跳回图片管理界面'
	if request.method == 'POST':
		pic_id = request.POST['pic']
		Picture.objects.filter(id=pic_id).delete()
		user = Custom.objects.get(pk = user_id)
		pics = user.picture_set.all()
		leds = user.lednumber_set.all()
		context = {
			'leds':leds,
			'user_id' : user_id,
			'pics' : pics,
		}
	return render(request,'led/manage_pic.html',context)

def del_video_data(request,user_id):
	'删除成功后跳回视频管理界面'
	if request.method == 'POST':
		video_id = request.POST['video']
		Video.objects.filter(id=video_id).delete()
		user = Custom.objects.get(pk = user_id)
		videos = user.video_set.all()
		leds = user.lednumber_set.all()
		context = {
			'leds':leds,
			'user_id' : user_id,
			'videos' : videos,
		}
	return render(request,'led/manage_video.html',context)

def led_operation(request,user_id):
	'处理关于LED的操作'
	if request.method == 'POST':
		try:
			led_id = request.POST['led_choice']
			led_op = request.POST['op']
			if not all([led_id,led_op]):
				return HttpResponseRedirect(reverse('led:choice', args = (user_id,)))
			elif led_op=="p":
				return led_show_picture(request,user_id,led_id)
			elif led_op=="v":
				return led_show_video(request,user_id,led_id)
		except:
			print(led_op)
			print('出错啦')
			return HttpResponseRedirect(reverse('led:choice', args = (user_id,)))

def led_update(request,led_id,user_id):
	'修改LED信息'
	if not request.method == 'POST':
		return HttpResponse("你的打开方式有一点点奇怪哦")
	try:
		new_led_text = request.POST.get('ledname')
		if new_led_text != "":
			LedNumber.objects.filter(id = led_id).update(led_text = new_led_text)
	except:
		pass
	try:
		new_address_text = request.POST.get('ledaddress')
		if new_address_text != "":
			LedNumber.objects.filter(id=led_id).update(address_text = new_address_text)
	except:
		pass

	return HttpResponseRedirect(reverse('led:choice',args = (user_id,)))

def add_picture(request,user_id):
	'添加图片的url'
	if request.method == 'POST':
		c = Custom.objects.get(pk = user_id)
		real_url = request.POST.get('pic_url')
		print(real_url)
		c.picture_set.create(pic_url = request.POST.get('pic_url'))
		c.save()
	user = Custom.objects.get(pk = user_id)
	pics = user.picture_set.all()
	leds = user.lednumber_set.all()
	context = {
		'leds':leds,
		'user_id' : user_id,
		'pics' : pics,
	}
	print("goto pic_manage.html")
	return render(request,'led/manage_pic.html',context)

def add_video(request,user_id):
	'添加视频的url'
	if request.method == 'POST':
		c = Custom.objects.get(pk = user_id)
		real_url = request.POST.get('video_url')
		print(real_url)
		c.video_set.create(video_url = request.POST.get('video_url'))
		c.save()
	user = Custom.objects.get(pk = user_id)
	videos = user.video_set.all()
	leds = user.lednumber_set.all()
	context = {
		'leds':leds,
		'user_id' : user_id,
		'videos' : videos,
	}
	return render(request,'led/manage_video.html',context)
	# return HttpResponseRedirect(reverse('led:video_manage', args = (user_id,)))

def led_show_picture(request,user_id,led_id):
	'显示led的图片内容'
	if request.method == 'POST' or request.method=='GET':
		user = Custom.objects.get(pk = user_id)
		get_urls = user.picture_set.all()
		urls = []
		for i in get_urls:
			urls.append(i.pic_url)
		context = {
			'user_id':user_id,
			'led_id':led_id,
			'urls' : json.dumps(urls),
		}
		print('now at look led')
		return render(request,'led/show_led.html',context)

def led_show_video(request,user_id,led_id):
	'显示led的视频内容'
	if request.method == 'POST' or request.method=='GET':
		user = Custom.objects.get(pk = user_id)
		get_urls = user.video_set.all()
		urls = []
		for i in get_urls:
			urls.append(i.video_url)
		context = {
			'user_id':user_id,
			'led_id':led_id,
			'urls' : json.dumps(urls),
		}
		print('now at look led')
		return render(request,'led/show_video_led.html',context)

def pic_manage(request,user_id):
	if request.method=='POST':
		user = Custom.objects.get(pk = user_id)
		pics = user.picture_set.all()
		leds = user.lednumber_set.all()
		context = {
			'leds':leds,
			'user_id' : user_id,
			'pics' : pics,
		}
		return render(request,'led/manage_pic.html',context)

def video_manage(request,user_id):
	if request.method=='POST':
		user = Custom.objects.get(pk = user_id)
		videos = user.video_set.all()
		leds = user.lednumber_set.all()
		context = {
			'leds':leds,
			'user_id' : user_id,
			'videos' : videos,
		}
		return render(request,'led/manage_video.html',context)