from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    created = serializers.DateTimeField(read_only=True)
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
