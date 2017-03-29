from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView, ListView










class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()


	def get_object(self):
		return Tweet.objects.get(id=1)

class TweetListView(ListView):
	queryset = Tweet.objects.all()


	def get_context_data(self, **kwargs):
		context = super(TweetListView, self).get_context_data(**kwargs)
		return context









# #retrieve
# def tweet_detail_view(request, id=1):
# 	obj = Tweet.objects.get(id=id)
# 	context = {
# 		'object': obj
# 	}
# 	return render(request, 'tweets/tweet_list.html', context)
#
# #list
# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	for obj in queryset:
#
# 		context = {
# 		'object_list': queryset
# 	}
# 	return render(request, 'tweets/tweet_list.html', context)