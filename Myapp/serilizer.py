from rest_framework import serializers, exceptions
from .models import FibonanciMethod
class FibonanciSerializer(serializers.Serializer):

    class Meta:
        model = FibonanciMethod
        fields = ('number','startTime','endTime','totalTime','FiboniciList','Fibonaci_output')

    def validate(self, data):
        number = data.get('number')
        if not number:
            raise exceptions.ValidationError('mobile number is wrong')
        return data
    def create(self, validated_data):

        return FibonanciMethod.objects.create(**validated_data)
