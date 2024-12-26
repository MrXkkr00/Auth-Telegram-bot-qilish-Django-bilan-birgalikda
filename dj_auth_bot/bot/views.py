from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .management.commands.run_bot import bot
from .models import User
from .serializers import GetAuthOTPcode
from django.core.cache import cache
import jwt


class VerifyUserCodeView(APIView):
    serializer_class = GetAuthOTPcode

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = GetAuthOTPcode(data=data)
            if not serializer.is_valid():
                return Response({'message': 'Invalid data'}, status=400)
            code = data['data']
            user_id = cache.get(code)

            if not user_id:
                return Response({'message': 'Code was expired'}, status=400)

            data = bot.get_chat(user_id)
            print(data)
            new_user = User.objects.get_or_create(telegram_id=user_id, first_name=data['first_name'],
                                                  last_name=['last_name'], username=['username'])
            cache.delete(code)
            encoded_jwt = jwt.encode({"data": new_user}, "secret", algorithm="HS256")

            return Response(
                {'message': 'User verified Succsessfully', 'data': {'token': encoded_jwt, 'user': new_user}},
                status=200)

        except Exception as e:
            return Response({'message': str(e)}, status=400)
