from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('details/<int:id>/variable-sets', views.variable_sets, name='variable-sets'),
    path('details/<int:id>/variable-sets/create', views.variable_set_create, name='variable-set-create'),
    path('details/<int:id>/variable-sets/<int:variable_set_id>', views.variable_set_details, name='variable-set-details'),
    path('details/<int:id>', views.details, name='details'),
    path('details/<int:id>/database-builder', views.database_builder, name='database-builder'),
    path('details/<int:id>/variable-extractions', views.variable_extractions, name='variable-extractions'),
    path('details/<int:id>/variable-extractions/create', views.variable_extraction_create, name='variable-extraction-create'),
    path('details/<int:id>/variable-extractions/<int:variable_extraction_id>', views.variable_extraction_details, name='variable-extraction-details'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]