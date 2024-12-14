from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_product, name='list_product'),
    path('product/<int:id>', views.product_dateil, name='product_dateil'),
    path('categorys/', views.list_category, name='list_category'),
    path('category/<int:id>', views.category_dateil, name='category_dateil'),
    path('tags/', views.list_tags, name='list_tags'),
    path('tag/<int:id>', views.tags_detail, name='tags_detail'),
]
