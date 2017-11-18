from django.utils import timezone 
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext, loader
from polls.models import Choice,Question
from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

def library(request):
 return render(request,'polls/library.html')

def call_login(request):
 return render(request,'polls/login.html')
 
def call_signup(request):
 return render(request,'polls/signup.html')
@login_required
def profilepage(request):
 return render(request,'polls/profilepage.html')

@login_required 
def editprofile(request):
 loggedinuser = request.user
 firstname = request.POST['firstname']
 lastname = request.POST['lastname']
 email = request.POST['email']
 
 if firstname and lastname and email:
  loggedinuser.first_name = firstname
  loggedinuser.last_name = lastname
  loggedinuser.email = email
  loggedinuser.save()
  return HttpResponseRedirect(reverse('polls:profilepage'))
 else:
  return render(request,"polls/profilepage.html", { 'message' : "All fields are necessary."} )
  

def afterlogin(request):
 username = request.POST['username']
 password = request.POST['password']
 user = authenticate(username = username , password = password)
 if user is not None:
  if user.is_active:
   login(request,user)
   return HttpResponseRedirect(reverse('polls:index2')) 
  else: 
   return render(request,"polls/login.html", { 'message' : "The password is valid, but the account has been disabled!" })
  
 else:
  return render(request,"polls/login.html", { 'message' : "Invalid Details." })

@login_required
def logout_view(request):
 logout(request)
 return HttpResponseRedirect(reverse('polls:index'))
 
@login_required
def changepasswordpage(request):
 return render(request,'polls/changepwdpage.html')

@login_required
def changepassword(request):
 loggedinuser = request.user
 oldpassword = request.POST['oldpassword']
 password1 = request.POST['password1']
 password2 = request.POST['password2']  
 user = authenticate(username = loggedinuser.username , password = oldpassword)
 if user is not None:
  if user.is_active:
   if password1 == password2 and password1 and password2:
    
    user.set_password(password1)
    user.save()
    login(request,user)
    return render(request,"polls/changepwdpage.html", { 'message' : "Password Successfully Changed." })
   else:
    return render(request,"polls/changepwdpage.html", { 'message' : "Password Didnot match."})
  else:
   logout(request,user)
   return render(request,"polls/changepwdpage.html", { 'message' : "The password is valid, but the account has been disabled!" })
 else:
  return render(request,"polls/changepwdpage.html", { 'message' : "Password Entered is Incorrect." })

 
 

 
def creatinguser(request):

 email = request.POST['email']
 firstname = request.POST['firstname']
 lastname = request.POST['lastname']
 username = request.POST['username']
 password1 = request.POST['password1']
 password2 = request.POST['password2']
 if password1 and password2 and firstname and username and lastname and email:
  if password1 == password2:
   user = User.objects.create_user(username,email,password1)
   user.first_name = firstname
   user.last_name = lastname
   user.save()
   return HttpResponseRedirect(reverse('polls:index'))
  else :
   return render(request,"polls/signup.html", { 'message' : "Passwords didn't match." })
 else:
   return render(request,"polls/signup.html", { 'message' : "All fields are necessary." })
 


class IndexView(generic.ListView):
 template_name = 'polls/index.html'
 context_object_name = 'latest_question_list'
 
 def get_queryset(self):
  """Return the last five punlished questions"""
  return Question.objects.filter(
   pub_date__lte = timezone.now()
   ).order_by('pub_date')[:6]



class IndexView2(generic.ListView):
 template_name = 'polls/index2.html'
 context_object_name = 'latest_question_list'
 
 def get_queryset(self):
  """Return the last five punlished questions"""
  return Question.objects.filter(
   pub_date__lte = timezone.now()
   ).order_by('pub_date')[:6]


class DetailView(generic.DetailView):
 model = Question
 template_name  = 'polls/detail.html'
 def get_queryset(self):
  return Question.objects.filter(pub_date__lte = timezone.now())

class ResultsView(generic.DetailView):
 model = Question
 template_name = 'polls/results.html'

 


#def index(request):
# latest_question_list = Question.objects.order_by('-pub_date')[:5]
# template = loader.get_template('polls/index.html')
# context = RequestContext(request , {
#  'latest_question_list' : latest_question_list,
# })
# return HttpResponse(template.render(context))
 
  # def index(request):
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  context = {'latest_question_list': latest_question_list}
  #  return render(request, 'polls/index.html', context)

#def results(request,question_id):
#  response = "You're looking at the results of question %s."
#  return HttpResponse(response  %question_id)
@login_required
def vote(request, question_id):
 p = get_object_or_404(Question, pk = question_id)
 try:
  selected_choice = p.choice_set.get(pk = request.POST['choice'])
 except (KeyError ,Choice.DoesNotExist):
  #redisplaying the voting form
  return render(request , 'polls/detail.html' , {
   'question':p,
   'error_message': "You didn't select a choice. ",
  })
 else:
  selected_choice.votes += 1
  selected_choice.save()
  # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
       # user hits the Back button.  
 return HttpResponseRedirect(reverse('polls:results', args= (p.id,)))
 
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', {'question': question}) 
 
#raising an error 
#def detail(request, question_id):
 #   try: 
  #      question = Question.objects.get(pk=question_id)
   # except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'ques': question})
 
 
#alternate shortcut better option
 
#def detail(request,question_id):
# question = get_object_or_404(Question , pk = question_id)
# return render(request , 'polls/detail.html' , {'question' : question} )
