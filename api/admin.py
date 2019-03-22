from django.contrib import admin
from django.utils.translation import gettext_lazy as _
 
from api.chatbot.models import KeywordedResponse, IgnoreNumber

admin.site.register(KeywordedResponse)
admin.site.register(IgnoreNumber)

admin.site.index_title = _('所有管理项目')
admin.site.site_header = _('谢蕾蕾应援会管理页面')
admin.site.site_title = _('谢蕾蕾应援会管理页面')
