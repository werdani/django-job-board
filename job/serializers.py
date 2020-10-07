from rest_framework import serializers
from .models import job 






class Jobserializers(serializers.ModelSerializer):
    class Meta:
        model = job
        fields='__all__'

