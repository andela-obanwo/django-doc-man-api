from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from docman.models import AccessType
from docman.serializers import AccessTypeSerializer

# Create your views here.

class AccessTypeList(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    @csrf_exempt
    """
    List all access types, or create a new access type.
    """
    queryset = AccessType.objects.all()
    serializer_class = AccessTypeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AccessTypeDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = AccessType.objects.all()
    serializer_class = AccessTypeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)