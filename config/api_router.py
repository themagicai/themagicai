from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path

from themagicai.app.views import SkillAPIView
from themagicai.chatGPT.views import LetterAPIView, PostCVAPIView, LetterDetailAPIView, PostCVDetailAPIView
from themagicai.users.api.views import UserViewSet
from themagicai.users.views import RegisterAPIView, LogoutView, PasswordChangeView, ResetPasswordView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("make-letters", LetterAPIView)
router.register("letter-detail", LetterDetailAPIView)
router.register("make-cv", PostCVAPIView)
router.register("cv-detail", PostCVDetailAPIView)
router.register("skills", SkillAPIView)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
