from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from docman.models import DocumentType
from docman.serializers import DocumentTypeSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def documenttype_list(request):
    """
    List all access types, or create a new access type.
    """
    if request.method == 'GET':
        documenttype = DocumentType.objects.all()
        serializer = DocumentTypeSerializer(documenttype, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocumentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def documenttype_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        documenttype = DocumentType.objects.get(pk=pk)
    except DocumentType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocumentTypeSerializer(documenttype)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocumentTypeSerializer(documenttype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        documenttype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
