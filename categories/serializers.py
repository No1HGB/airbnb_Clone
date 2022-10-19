from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)  # 유저가 데이터 작성 시 보내지 않도록
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(
            **validated_data,
        )  # validated_data는 dict. **:dict를 가져와서 name="",kind=""형태로 바꿔줌

    # instance: category
    # update에 대한 로직
    def update(self, instance, validated_data):
        # dictionary.get(key에 해당하는 data 반환, 없을 경우 반환하는 값)
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
