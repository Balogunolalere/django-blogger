from django.urls import path
from .views import HomeView,CreateView,PostView,DeleteView,UpdateView,AboutView,ContactView


urlpatterns = [

	path('',HomeView.as_view(),name='index'),
	path('post/<int:pk>/', PostView.as_view(),name='post'),
	path('post/create/', CreateView.as_view(), name='create'),
	path('post/<int:pk>/delete', DeleteView.as_view(), name='delete'),
	path('post/<int:pk>/edit', UpdateView.as_view(), name='edit'),
	path('about/', AboutView.as_view(), name='about'),
	path('contact/', ContactView.as_view(), name='contact'),

]