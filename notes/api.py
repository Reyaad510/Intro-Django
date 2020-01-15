from rest_framework import serializers, viewsets
from .models import PersonalNote, Note


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    # Meta tells what part of model we want access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()  # start debugger here
        # pass
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note


# Used to visualize
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = Note.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
