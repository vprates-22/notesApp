from rest_framework.decorators import api_view
from .utils import *

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        return getNotes(request)
    if request.method == 'POST':
        return createNote(request)

@api_view(['GET', 'PUT', 'DELETE'])
def note(request, pk):

    if request.method == 'GET':
        return getNote(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)
    
    if request.method == 'DELETE':
        return deleteNote(request, pk)