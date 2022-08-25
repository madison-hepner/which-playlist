"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from whichplaylistapi.models import PlayListItem


class PlayListView(ViewSet):
    """play lists view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

            Returns:
            Response -- JSON serialized game type
        """
        playlist = PlayListItem.objects.get(pk=pk)
        serializer = PlayListSerializer(playlist)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """

        playlist = PlayListItem.objects.all()
        serializer = PlayListSerializer(playlist, many=True)
        return Response(serializer.data)

    def create(self, request):
        playlist = PlayListItem.objects.create(
            playlist_name=request.data["playlist_name"],
            description=request.data["description"],
            playlist_vibes=request.data["playlist_vibes"],
            length=request.data["length"]
        )
        serializer = PlayListSerializer(playlist)
        return Response(serializer.data)

    def update(self, request, pk):
        playlist = PlayListItem.objects.get(pk=pk)
        playlist.playlist_name = request.data["playlist_name"]
        playlist.description = request.data["description"]
        playlist.playlist_vibes = request.data["playlist_vibes"]
        playlist.length = request.data["length"]

        # game_type = GameType.objects.get(pk=request.data["game_type"])
        # game.game_type = game_type
        playlist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        playlist = PlayListItem.objects.get(pk=pk)
        playlist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayListItem
        fields = ('id', 'playlist_name', 'description',
                  'playlist_vibes', 'length')


class CreatePlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayListItem
        fields = ['id',  'playlist_name', 'description',
                  'playlist_vibes', 'length']
