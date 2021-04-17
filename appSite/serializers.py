from rest_framework import serializers
from appSite.models import Nav


class NavSerializer(serializers.ModelSerializer):
    class Meta():
        model = Nav
        fields = '__all__'
        # fields = ('aaa','bbb')

