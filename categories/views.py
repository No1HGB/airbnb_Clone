from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])  # GET, POST 둘 다 허용. 기본값=GET
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories,
            many=True,
        )  # QuerySet을 전달할 경우, many=True를 해주어야 함. 기본값=data 1개.
        return Response(serializer.data)  # serializer로 받은 data
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)  # data= 로 데이터 작성
        if serializer.is_valid():  # 유효성 검사
            new_category = (
                serializer.save()
            )  # POST로 받은 데이터를 저장. .save()를 실행하면 자동적으로 serializer안에서 create메소드를 찾음.
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def oneCategory(request, pk):
    # 예외처리
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        getSerializer = CategorySerializer(category)
        return Response(getSerializer.data)
    elif request.method == "PUT":
        putSerializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )  # partial=True: data일부만 전송되어도 유효성 검사에 걸리지 않게끔(업데이트 이기 때문에 일부만 변경 가능하게끔)
        if putSerializer.is_valid():
            updated_category = putSerializer.save()
            # 자동적으로 update 메소드 실행. serializer는 create, update를 자동적으로 구분함.
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(putSerializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(HTTP_204_NO_CONTENT)
