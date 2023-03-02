from rest_framework import serializers
from .models import Music, Album, Member, Band


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Music
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Album
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Member
        fields = '__all__'

    
class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Band
        fields = '__all__'