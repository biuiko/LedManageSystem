from django.urls import path
from . import views

app_name = 'led'

urlpatterns = [
	path('',views.index,name ='index'),
	path('<int:user_id>/choice/',views.choice_page,name='choice'),
	# path('movie/',views.movie_show,name='movie'),
	path('check/',views.check,name ='check'),
	# path('<int:user_id>/add_led/',views.add_led,name='add_led'),
	path('<int:user_id>/add_led_data/',views.add_led_data,name='add_led_data'),
	path('<int:user_id>/del_led_data',views.del_led_data,name='del_led_data'),
	path('<int:user_id>/del_pic_data',views.del_pic_data,name='del_pic_data'),
	path('<int:user_id>/del_video_data',views.del_video_data,name='del_video_data'),
	path('<int:user_id>/led_operation/',views.led_operation,name='led_operation'),
	path('<int:led_id>/<int:user_id>/led_update/',views.led_update,name='led_update'),
	path('<int:user_id>/add_picture',views.add_picture,name='add_picture'),
	path('<int:user_id>/add_video',views.add_video,name='add_video'),
	path('picture/<int:user_id>/<int:led_id>',views.led_show_picture,name='led_show_picture'),
	path('video/<int:user_id>/<int:led_id>',views.led_show_video,name='led_show_video'),
	path('pic_manage/<int:user_id>',views.pic_manage,name='pic_manage'),
	path('video_manage/<int:user_id>',views.video_manage,name='video_manage'),

]