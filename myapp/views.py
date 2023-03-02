from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .models import Music, Album, Member, Band
from .serializers import MusicSerializer, AlbumSerializer, MemberSerializer, BandSerializer

### ListCreateAPIView            --> Auto implements GET(List) and POST(Create) functions
### RetrieveUpdateDestroyAPIView --> Used for read-write-delete endpoints to represent a single model instance.
##                                   Provides `get`, `put`, `patch` and `delete` method handlers.

'''Music''' 
class MusicList(generics.ListCreateAPIView):
    queryset         = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


'''Album'''
class AlbumList(generics.ListCreateAPIView):
    queryset         = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


'''Member'''
class MemberList(generics.ListCreateAPIView):
    queryset         = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


'''Band'''
class BandList(generics.ListCreateAPIView):
    queryset         = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )