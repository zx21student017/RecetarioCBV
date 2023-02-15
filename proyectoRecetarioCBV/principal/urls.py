from django.urls import path

from .views import RecetaListView, RecetaCreateView, RecetaDetailView, RecetaUpdateView, RecetaDeleteView

urlpatterns = [
    path('',RecetaListView.as_view(),name='receta'),
    path('crearReceta',RecetaCreateView.as_view(),name='crear'),
    path('detalleReceta/<int:pk>',RecetaDetailView.as_view(),name='detalleReceta'),
    path('modificarReceta/<int:pk>',RecetaUpdateView.as_view(),name='modificarReceta'),
    path('borrarReceta/<int:pk>',RecetaDeleteView.as_view(),name='borrarReceta')
]