from .views import UserDetailView, UserFollowView
from django.conf.urls import url, include
from django.views.generic.base import RedirectView


urlpatterns = [
	# url(r'^$', RedirectView.as_view(url='/'), name='home'),
	# url(r'^$', TweetListAPIView.as_view(), name='list'),
	# url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
	url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
	# url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
	# url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete')


]