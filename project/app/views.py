from app.models import Memo
from app.serializers import MemoSerializer
from rest_framework import mixins, generics

class MemoList(generics.ListCreateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

# class MemoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class MemoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Memo.objects.all()
#     serializer_class = MemoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# from app.models import Memo
# from app.serializers import MemoSerializer
# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# class MemoList(APIView):
#     def get(self, request, format=None):
#         memo = Memo.objects.all()
#         serializer = MemoSerializer(memo, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = MemoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#
# class MemoDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Memo.objects.get(pk=pk)
#         except Memo.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         memo = self.get_object(pk)
#         serializer = MemoSerializer(memo)
#         return Response(serializer)
#
#     def put(self, request, pk, format=None):
#         memo = self.get_object(pk)
#         serializer = MemoSerializer(memo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         memo = self.get_object(pk)
#         memo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from django.http import HttpResponse, JsonResponse
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from app.models import Memo
# from app.serializers import MemoSerializer
#
# @api_view(['GET', 'POST'])
# def memo_list(request):
#     if request.method == 'GET':
#         memo = Memo.objects.all()
#         serializer = MemoSerializer(memo, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MemoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def memo_detail(request, pk):
#     try:
#         memo = Memo.objects.get(pk=pk)
#     except Memo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MemoSerializer(memo)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MemoSerializer(memo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         memo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
