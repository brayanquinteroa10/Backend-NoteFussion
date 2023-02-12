from django .urls import path  
from .views import Tareavista 



urlpatterns = [
    path('works/post', Tareavista.as_view(), name='post'),
    path('works/get', Tareavista.as_view(), name='get'),
    path('works/put/<int:id>', Tareavista.as_view(), name='put'),
    path('works/delete/<int:id>', Tareavista.as_view(), name='delete')
]