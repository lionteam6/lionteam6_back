from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'nickname',
            'university',
            'password'
        )
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            university=validated_data['university']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if not user.check_password(password): 
                raise serializers.ValidationError()

            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)
                #토큰까지 반환
                return {
                    'id' : user.id,
                    'nickname' : user.nickname,
                    'university' : user.university,
                    'access' : access,      
                    'refresh' : refresh
                }