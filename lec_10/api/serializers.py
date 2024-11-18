from rest_framework import serializers
from . models import Student

class StudentSerializers(serializers.ModelSerializer):

    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be startwith r')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['name','roll',"city"]

    # Field level Validation(single Field)
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return  value

    # Object level Validation (Multiple Fields)
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'veeru' and ct.lower() != 'pune':
            raise serializers.ValidationError('city must be pune')
        return data




