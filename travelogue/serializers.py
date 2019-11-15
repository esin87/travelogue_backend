from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    entry_url = serializers.ModelSerializer.serializer_url_field(
        view_name='entry_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Entry
        fields = ('title', 'photo_url', 'place_name',
                  'notes', 'entry_url', 'owner', 'date',)
