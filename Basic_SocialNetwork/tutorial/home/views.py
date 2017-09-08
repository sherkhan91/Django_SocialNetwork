from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from home.models import Post, Friend


class HomeView(TemplateView):
	template_name = 'home/home.html'


	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created')
		users = User.objects.exclude(id=request.user.id)
		try:
			friend = Friend.objects.get(current_user=request.user)
		except:
			friend = None
		try:
			friends  = friend.users.all()
		except:
			friends = None	
		
		args = {'form': form, 'posts': posts, 'users': users, 'friends': friends}
		return render(request, self.template_name, args)


	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()

			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home:home')



		args = {'form': form, 'text': text}		
		return render(request, self.template_name, args)


def change_friends(request, operation, pk):
	friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend.make_friend(request.user, friend)
	elif operation == 'remove':
		Friend.lose_friend(request.user, friend)	
	return redirect('home:home')
	