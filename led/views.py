from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Custom,LedNumber
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
		return HttpResponse("what")
	user_name = request.POST.get('username')
	user_password = request.POST.get('userpassword')
	if not all([user_name,user_password]):
		return render(request,'led/index.html')
	users = Custom.objects.all()
	for user in users:
		if user.user_name == user_name and user.user_password==user_password:
			return HttpResponseRedirect(reverse('led:choice', args = (user.id,)))
	return HttpResponse("hello")

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