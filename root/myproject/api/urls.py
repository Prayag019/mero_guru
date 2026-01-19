from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'vacancies', VacancyViewSet, basename='vacancy')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = router.urls
