from rest_framework import serializers


from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "body", "created_at", "updated_at")
        model = Post

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation["author"] = instance.author.username

        return representation
