from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated


class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({"detail": "У вас нет прав для удаления этого кота."}, status=403)
        self.perform_destroy(instance)
        return Response(status=204)



class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


def index(request):
    # if request.method == "POST":
    #     name = request.POST.get("name", None)
    #     if name:
    #         room = Room.objects.create(name=name, host=request.user)
    #         print(room.pk)
    #         return HttpResponseRedirect(reverse("room", kwargs={"pk": room.pk}))
    return render(request, 'chat/index.html')
