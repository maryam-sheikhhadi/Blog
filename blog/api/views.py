from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Article
from .permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperuserOrStaffReadOnly
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    def get_queryset(self):
        print(self.request.user)
        print(self.request.auth)
        return User.objects.all()

    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        # 204 no content
        return Response(status=204)
