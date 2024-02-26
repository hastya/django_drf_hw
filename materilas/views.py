from rest_framework import viewsets, generics
from materilas.models import Course, Lesson
from materilas.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated
from materilas.permissions import IsOwner, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner | IsModerator]

    def create(self, request, *args, **kwargs):
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if is_moderator:
            return self.permission_denied(request)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        is_moderator = request.user.groups.filter(name='Moderators').exists()
        if is_moderator:
            return self.permission_denied(request)
        return super().destroy(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
