from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from user_app.api.serializers import RegisterSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['POST',])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'Success':'Token Successfully Deleted'},status=status.HTTP_200_OK)
