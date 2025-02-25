from rest_framework import serializers
from .models import Question , Answer
from .custom_relational import UserEmailNameRelationalField


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    
    
class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    # how to show fields in api view
    user = UserEmailNameRelationalField(read_only=True)
    
    class Meta:
        model = Question
        fields = '__all__'
        
        
    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data
        
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'