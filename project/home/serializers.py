from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = Person
        # exclude = ['age']
        fields = '__all__'
        depth = 1   #to show foreign key details

    def get_country(self, obj):
        return "India"

    def validate(self, data):
        special = "!@#$%^&*()_+=-[]{};:'\"\\|,<.>/?`~"

        # validate only if 'name' is provided
        if 'name' in data and any(char in special for char in data['name']):
            raise serializers.ValidationError("Name should not contain special characters.")

        # validate only if 'age' is provided
        if 'age' in data and data["age"] < 18:
            raise serializers.ValidationError("Age must be at least 18 years.")

        return data