from rest_framework import viewsets
from JsonAPI import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = serializers.UserSerializer(data=request.DATA, context={'request': request})
        if user_serializer.is_valid():
            try:
                user_serializer.object.set_password(user_serializer.data['password'])
                user_serializer.object.save()
            except Exception as e:
                return Response({'Error':'Error saving user data! '})
             
            return Response({'Success':'User {0} is registered successfully.'.format(user_serializer.data['username'])})
        else:
            return Response({'Error':'Error registering user, incorrect data! ', 'data': json.dumps(user_serializer.errors)})
      
    def update(self, request, *args, **kwargs):
        ''' 
        Updates user data. 
        
        If the password provided is different then first hash it by "set_password" and then save the object.
        '''
        # permission_classes = (IsAdminUser,)
        old_user = User.objects.get(id=kwargs['pk'])
        old_password = old_user.password # this field is later being updated and replaced by the serializer
        user_serializer = serializers.UserSerializer(instance=old_user, data=request.DATA, context = {'request': request})
        
        if user_serializer.is_valid():                                                    
            if old_password != user_serializer.data['password']:
                user_serializer.object.set_password(user_serializer.data['password'])            
            try:                
                user_serializer.save()
            except Exception as e:
                return Response({'Error': 'Error updating user, incorrect data!'})
                      
            return Response({'user:': user_serializer.data,  'status':'User {0} was updated successfully.'.format(user_serializer.data['username'])})
        else:
            return Response({'Error': 'Error updating user, incorrect data!'})
       