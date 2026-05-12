from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    participant_count = serializers.SerializerMethodField()
    is_full = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content','item_name','price','photo','max_participants', 'location', 'participants', 'participant_count', 'is_full')
    
    def get_participant_count(self, obj):
      return obj.participant_count()

    def get_is_full(self, obj):
      return obj.is_full()