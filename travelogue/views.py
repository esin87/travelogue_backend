from rest_framework import generics, permissions
from .serializers import EntrySerializer
from .models import Entry
# from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @login_required
class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
