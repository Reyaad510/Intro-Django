from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # Meta tells what part of model we want access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')


# Used to visualize
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
