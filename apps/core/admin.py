from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from environ import Env
from apps.core.models import Message, Room, Topic


env = Env()

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)


admin.site.site_title = _(
    env("APP_TITLE", cast=str, default="Event Ticketing"))
admin.site.site_header = _(
    env("APP_TITLE", cast=str, default="Event Ticketing"))
admin.site.index_title = _(
    env("INDEX_TITLE", cast=str, default="Event Ticketing"))
