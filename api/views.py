from cgitb import reset
import re
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Note
from api.serializers import NoteSerializer
from django.http import JsonResponse

# Create your views here.
def getRountes(request):
    return JsonResponse('Our Api', safe=False)

class NotesList(APIView):
    """
    List all notes, or create a new notes.
    """
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


class GetNotes(APIView):
    def get(self, request, pk, format=None):
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False)
        return Response(serializer.data)       



class UpdateNoteView(APIView):
    # permission_classes = (IsAuthenticated,)
    # serializer_class = PaymentSerializerView

    def put(self, request, pk):
        data = request.data
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=data)

        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)

class CreateNoteView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        note = Note.objects.create(
            body=data['body']
            )
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)



class DeleteNoteView(APIView):
    # permission_classes = (IsAuthenticated,)
    # serializer_class = PaymentSerializerView

    def delete(self, request, pk):
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('Note Was Deleted')