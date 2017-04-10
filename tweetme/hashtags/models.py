from django.db import models
from tweets.models import Tweet
from django.urls import reverse_lazy



class HashTag(models.Model):
	tag = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.tag

	def get_tweets(self):
		return Tweet.objects.filter(content__icontains='#' + self.tag)


	def get_absolute_url(self):
		return reverse_lazy('hashtag', kwarg={'hashtag': self.tag})