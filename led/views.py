from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Custom,LedNumber,Picture
# Create your views here.

def index(request):
	'登录界面'
	return render(request,'led/index.html')
	#return HttpResponse("hello")

def choice_page(request,user_id):
	'登录后选择操作界面'
	led_list = Custom.objects.get(pk =user_id)
	context = {
		'led_list' : led_list,
		'user_id':user_id
	}
	return render(request,'led/choice_page.html',context)

def movie_show(request):
	'LED放映界面'
	return HttpResponse("hello")

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

def add_led(request,user_id):
	'点击添加按钮到添加LED界面'
	context={}
	context['user_id'] = user_id
	return render(request,'led/add_led.html',context)
	# return HttpResponseRedirect(reverse('led:add_led',args=(user_id,)))
	# return HttpResponse("hello you clicked")

def add_led_data(request,user_id):
	'处理添加数据成功后跳到选择操作界面'
	if request.method == 'POST':
		c = Custom.objects.get(pk = user_id)
		c.lednumber_set.create(led_text = request.POST.get('led_text'),address_text = request.POST.get('led_address'))
		c.save()
		led_list = Custom.objects.get(pk =user_id)
		context = {
			'led_list' : led_list,
			'user_id':user_id
		}
		# return HttpResponseRedirect(reverse('led:choice',{'user_id':user_id,'led_list':led_list}))
		return render(request,'led/choice_page.html',context)

def led_operation(request,user_id):
	'处理关于LED的操作'
	if request.method == 'POST':
		try:
			led_id = request.POST['led_choice']
			led_op = request.POST['op']
			if not all([led_id,led_op]):
				return HttpResponseRedirect(reverse('led:choice', args = (user_id,)))
			if led_op == "d":
				LedNumber.objects.filter(id=led_id).delete()
				return HttpResponseRedirect(reverse('led:choice', args = (user_id,)))
			elif led_op == "u":
				print('now at op=u')
				context = {
					'led_id' : led_id,
					'user_id':user_id
				}
				return render(request,'led/update_led.html',context)
				# return HttpResponse("hello")
				# return render(request,'led/update_led.html',context)
			elif led_op=="l":
				user = Custom.objects.get(pk = user_id)
				urls = user.picture_set.all()
				# url=Picture.objects.filter(Picture.custom.id = 'user_id')
				context = {
					# 'user_id':user_id,
					'urls':urls,
				}
				print(urls)
				return render(request,'led/show_led.html',context)
		except:
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
		# real_url = request.POST.get('pic_url')
		
		c.picture_set.create(pic_url = request.POST.get('pic_url'))
		c.save()
	context={
		'user_id':user_id,
	}
	return HttpResponseRedirect(reverse('led:choice', args = (user_id,)))
