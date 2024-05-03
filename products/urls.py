from django.urls import path
from . import views
from .views import EditReview, DeleteReview

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path("review_edit/<int:pk>/", EditReview.as_view(), name="edit_review"),
    path("delete/<int:pk>", DeleteReview.as_view(),
         name="delete_review"),
    path('/<int:pk>', views.Wishlist.as_view(), name='wishlist'),
]