from django.contrib.auth.models import Group
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from allauth.account.models import EmailAddress

from authentication.models import UserInfo


@api_view(['POST'])
def user_check(request):
    # print(request.user)
    # print(request.auth)
    print(request.user in Group.objects.get(name='abcd').user_set.all())
    print(Group.objects.get(name='abcd'))
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def group_create(request):
    print(request.data)
    serializer = GroupSerializer(data=request.data)
    print(request.user)
    if serializer.is_valid():
        new_group = Group.objects.create(name=request.data['groupName'])
        new_group.user_set.add(request.user)
        print(type(new_group))
        return Response("success")


@api_view(['GET'])
def get_userinfo(request):
    userdata = {'username': request.user.username,
                'name': request.user.name,
                'id': request.user.id,
                'email': request.user.email}
    return Response(userdata)



