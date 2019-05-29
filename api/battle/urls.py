from django.urls import path

from api.battle.views.datav import IndividualView, GroupView
from api.battle.views.chatbot import IndividualBattleBroadcastView

urlpatterns = [
    path('individual/', IndividualView.as_view()),
    path('group/', GroupView.as_view()),
    path('battle_broadcast/', IndividualBattleBroadcastView.as_view()),
]