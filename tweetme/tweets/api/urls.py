from .views import TweetListAPIView
from django.conf.urls import url
from django.views.generic.base import RedirectView


urlpatterns = [
	# url(r'^$', RedirectView.as_view(url='/'), name='home'),
	url(r'^$', TweetListAPIView.as_view(), name='list'),
	# url(r'^create/$', TweetCreateView.as_view(), name='create'),
	# url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
	# url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
	# url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete')


]