from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from polls import views
 
urlpatterns = patterns('',
	
	url(r'^feedback',login_required(views.IndexView2.as_view()) , name = 'index2'),
	
	url(r'^$',views.IndexView.as_view() , name = 'index'),
		# ex: /polls/5/
	url(r'^(?P<pk>\d+)/$',login_required (views.DetailView.as_view()), name='detail'),
    # ex: /polls/5/results/
	url(r'^(?P<pk>\d+)/results/$', login_required(views.ResultsView.as_view()), name='results'),
    # ex: /polls/5/vote/
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
	
	url(r'^login/$' , views.call_login , name = 'loginpage'),
	
	url(r'^auth/$' , views.afterlogin , name = 'afterloginpage'),
	
	url(r'^creatinguser/$' , views.creatinguser , name = 'creatinguser'),
	
	url(r'^signup/$' , views.call_signup , name = 'signup'),
	
	url(r'^logout/$' , views.logout_view , name = 'logout'),
	
	url(r'^profilepage/$' , views.profilepage , name = 'profilepage'),
	url(r'^editprofile/$' , views.editprofile , name = 'editprofile'),
	
	url(r'^changepwd/$' , views.changepassword , name = 'changepwd'),
	
	url(r'^changepwdpage/$' , views.changepasswordpage , name = 'changepwdpage'),
	url(r'^library/$' , views.library , name = 'library'),
	
	)
	
	
	

