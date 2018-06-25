from app.models import Memo
from rest_framework import serializers

class MemoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Memo.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    class Meta:
        model = Memo
        fields = ('id', 'title', 'content', 'created')
