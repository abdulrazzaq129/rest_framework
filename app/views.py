from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import CarList, ShowRoomList,Review
from .serializers import CarListSerializer, ShowRoomSerializer,ReviewSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissions
from rest_framework import mixins
from rest_framework import generics

class ReviewRetrieve(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShowroomList(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            showrooms = ShowRoomList.objects.all()
            serializer = ShowRoomSerializer(showrooms, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": f"Failed to retrieve showrooms. {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = ShowRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowroomDetail(APIView):
    
    def get(self, request, pk):
        try:
            showroom = ShowRoomList.objects.get(pk=pk)
            serializer = ShowRoomSerializer(showroom)
            return Response(serializer.data)
        except ShowRoomList.DoesNotExist:
            return Response({"error": "Showroom not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            showroom = ShowRoomList.objects.get(pk=pk)
            serializer = ShowRoomSerializer(showroom, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ShowRoomList.DoesNotExist:
            return Response({"error": "Showroom not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            showroom = ShowRoomList.objects.get(pk=pk)
            showroom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ShowRoomList.DoesNotExist:
            return Response({"error": "Showroom not found."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        cars = CarList.objects.all()
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    try:
        car = CarList.objects.get(pk=pk)
    except CarList.DoesNotExist:
        return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarListSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarListSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
