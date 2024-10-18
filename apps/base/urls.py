from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename="task-api")

urlpatterns = []  
urlpatterns += router.urls