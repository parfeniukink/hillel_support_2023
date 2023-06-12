import json
from typing import Callable

from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserRegistrationSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        return super().post(request)

# def base_error_handler(func: Callable):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except SerializerError as error:
#             message = {"errors": error._serializer.errors}
#             status_code = 400
#         except Exception as error:
#             message = {"error": str(error)}
#             status_code = 500

#         return HttpResponse(
#             content_type="application/json",
#             content=json.dumps(message),
#             status=status_code,
#         )

#     return inner


# def create_user(request):
#     user_create_serializer = UserCreateSerializer(data=json.loads(request.body))
#     is_valid = user_create_serializer.is_valid()
#     if not is_valid:
#         raise SerializerError(user_create_serializer)

#     user = User.objects.create_user(**user_create_serializer.validated_data)
#     user_public_serializer = UserPublicSerializer(user)

#     return JsonResponse(user_public_serializer.data)


# def retrieve_user(request):
#     user = User.objects.get()
#     user_public_serializer = UserPublicSerializer(user)

#     return JsonResponse(user_public_serializer.data)


# @base_error_handler
# def users_router(request):
#     if request.method == "POST":
#         return create_user(request)
#     elif request.method == "GET":
#         return retrieve_user(request)
