from rest_framework import serializers
from configapp.models import *

# class NewsSerializer(serializers.Serializer):
#   title = serializers.CharField(max_length=50)
#   context = serializers.CharField(allow_blank=True, required=False)
#   created_ed = serializers.DateTimeField(read_only=True)
#   updated_ed = serializers.DateTimeField(read_only=True)
#   category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#   photo = serializers.ImageField(allow_null=True, required=False)
#   is_bool = serializers.BooleanField(default=True)
#   views = serializers.IntegerField(default=0)
#
#   def create(self, validated_data):
#     return News.objects.create(**validated_data)
#
#
# class CategorySerializer(serializers.Serializer):
#   title = serializers.CharField(max_length=50)
#
#   def create(self, validated_data):
#     return Category.objects.create(**validated_data)

from rest_framework import serializers
from .models import *

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model =Actor
        fields = '__all__'

class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitMovie
        fields = ['id','movie','title','author']
        read_only_fields = ["id",'author']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()  # email maydoni
    text = serializers.CharField()
# class UserSerializer(serializers.ModelSerializer):

