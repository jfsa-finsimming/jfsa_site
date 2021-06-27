from django.contrib import admin
from .models import Team, NationalMember, Position, Member, Tag, NewsPost, Event

admin.site.register(Team)
admin.site.register(NationalMember)
admin.site.register(Position)
admin.site.register(Member)
admin.site.register(Tag)
admin.site.register(NewsPost)
admin.site.register(Event)
