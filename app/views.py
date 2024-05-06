from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarList,ShowRoomList
from .serializers import CarListSerializer,ShowRoomSerializer
from rest_framework import status
from rest_framework.decorators import APIView

class showroom_view(APIView):
    def get(self, request):
        try:
            showroom = ShowRoomList.objects.all()
            serializer = ShowRoomSerializer(showroom, many=True)
        except:
            return Response({Response.error},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            serializer = ShowRoomSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"Error":"Post request Error"},status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        try:
            showroom = ShowRoomList.objects.get(pk=pk)
            serializer =ShowRoomSerializer(showroom,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
    def delete(self, request, pk):
        try:
            showroom = ShowRoomList.objects.get(pk=pk)
            showroom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        


@api_view(['GET','POST'])
def car_list_view(request):
   if request.method == 'GET':
        try:
            car = CarList.objects.all()
            serializer = CarListSerializer(car, many=True)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
   
   if request.method == 'POST':
        serializer = CarListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            

@api_view(['GET','PUT','DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        car = CarList.objects.get(pk=pk)
        serializer = CarListSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = CarList.objects.get(pk=pk)
        serializer = CarListSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        car = CarList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)