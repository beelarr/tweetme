from rest_framework import serializers

from ..models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tweet
		fields =[
			'user',
			'content'
		]


