from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRountes, name='rountes'),
    path('notes/', views.NotesList.as_view(), name='note_list'),
    path('notes/<str:pk>/', views.GetNotes.as_view(), name='get_notes'),
    path('notes/<str:pk>/update/', views.UpdateNoteView.as_view(), name='update_note'),
    path('notes/<str:pk>/delete/', views.DeleteNoteView.as_view(), name='delete_note'),
]