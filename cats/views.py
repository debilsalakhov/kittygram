from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer
#
#
# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# class APICat (APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)