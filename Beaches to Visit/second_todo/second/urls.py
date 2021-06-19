from django.urls import path
from second_todo.second.views import home_page, list_view, detail_view, add_place, remove_place, create_from_form, \
    delete_from_form

urlpatterns = [
    path('', home_page),
    path('list_view/', list_view),
    path('detail_view/<int:pk>', detail_view, name='detail_view'),
    path('add_place/', add_place),
    path('remove_place/', remove_place),
    path('create/', create_from_form),
    path('delete/', delete_from_form, name='delete_place'),
]
