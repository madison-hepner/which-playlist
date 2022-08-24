"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from whichplaylistapi.models import PlayListItem


class PlayListView(ViewSet):
    """play lists view"""

    def retrieve(self, request, pk):
        playlist = PlayListItem.objects.get(pk=pk)
        serializer = PlayListSerializer(playlist)
        return Response(serializer.data)

    def list(self, request):
        playlist = PlayListItem.objects.all()
        serializer = PlayListSerializer(playlist, many=True)
        return Response(serializer.data)


class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayListItem
        fields = ('id', 'playlist_name', 'description',
                  'playlist_vibes', 'length')
