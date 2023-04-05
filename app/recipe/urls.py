from django.urls import path, include
from recipe import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
app_name = 'recipe'

router.register('recipes', views.RecipeViewSet, basename='recipe')
router.register('tags', views.TagsViewSet, basename="tag")
router.register('ingredients', views.IngredientViewSet, basename="ingredient")

urlpatterns = [
     path('', include(router.urls)),
]
