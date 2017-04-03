from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from django.db.models import Q
from .forms import TweetModelForm
from django.urls import reverse_lazy
from django.views.generic import (DetailView, ListView,
                                  CreateView, UpdateView,
                                  DeleteView)




class TweetCreateView(LoginRequiredMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/tweet_create.html'
	# success_url = reverse_lazy('tweet:detail')
	login_url = '/admin/'


class TweetUpdateView(LoginRequiredMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/tweet_update.html'
	success_url = '/tweet/'
	login_url = '/admin/'


class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()


class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	success_url = reverse_lazy('tweet:list')
	template_name = 'tweets/tweet_confirm_delete.html'


class TweetListView(ListView):


	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		query = self.request.GET.get('q', None)
		if query is not None:
			qs = qs.filter(Q(content__icontains=query) | Q(user__username__icontains=query))
		return qs



	def get_context_data(self, **kwargs):
		context = super(TweetListView, self).get_context_data(**kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy('tweet:create')
		return context

