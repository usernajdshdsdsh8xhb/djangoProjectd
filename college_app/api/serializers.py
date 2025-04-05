
from rest_framework import serializers

from college_app.api.models import Post, Subject
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["name"]
        
    def to_representation(self, instance):
        return instance.name
        
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    posterName = serializers.CharField()
    original = serializers.IntegerField()
    wish = serializers.IntegerField()
    subjects = SubjectSerializer(many=True, )
    date = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        print("name")

        tmp_dic = validated_data.pop("subjects")
        tmp = Post.objects.create(**validated_data)
        
        tmpRes = []

        for name in tmp_dic:

            obj = Subject.objects.get(name=name["name"])

            tmpRes.append(obj.pk)
        tmp.subjects.set(tmpRes)
        
        return tmp


class CustomTwoPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    posterName = serializers.CharField()
    original = serializers.IntegerField()
    wish = serializers.IntegerField()
    subjects = SubjectSerializer(many=True, )
    date = serializers.DateTimeField(read_only=True)
    posterTelegram = serializers.CharField(write_only=True,allow_blank=True) 
    acceptorTelegram = serializers.CharField(allow_blank=True, write_only=True) 


    def create(self, validated_data):
        print("name")

        tmp_dic = validated_data.pop("subjects")
        tmp = Post.objects.create(**validated_data)
        
        tmpRes = []

        for name in tmp_dic:

            obj = Subject.objects.get(name=name["name"])

            tmpRes.append(obj.pk)
        tmp.subjects.set(tmpRes)
        
        return tmp

        
        
    
class CustomPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    posterName = serializers.CharField()
    posterTelegram = serializers.CharField(read_only=True)
    original = serializers.IntegerField()
    wish = serializers.IntegerField()
    subjects = SubjectSerializer(many=True, )
    date = serializers.DateTimeField(read_only=True)
    acceptorName = serializers.CharField(read_only=True)
    acceptorTelegram = serializers.CharField(read_only=True)