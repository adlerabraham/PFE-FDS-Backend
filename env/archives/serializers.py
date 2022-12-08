from rest_framework.serializers import ModelSerializer

from archives.models import Archives

class ArchivesSerializers(ModelSerializer):
    class Meta:
        model =Archives
        fields ='__all__'
