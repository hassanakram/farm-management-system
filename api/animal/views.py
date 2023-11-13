from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal
from .serializers import AnimalSerializer


class AnimalList(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimalDetail(APIView):
    def delete(self, request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
