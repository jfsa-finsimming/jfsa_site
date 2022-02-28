from django.contrib import admin
from .models import Team, NationalMember, Position, Member, Tag, NewsPost, Event, Race, JFSACupResult, JFSACupRecord,  JFSACupMedia
from .forms import JFSACupForm
from cloudinary.forms import cl_init_js_callbacks

@admin.register(JFSACupMedia)
class JFSACupMediaAdmin(admin.ModelAdmin):
    add_form_template = 'admin/post_form.html'
    change_form_template = 'admin/check_form.html'

    def get_form(self, request, obj=None, **kwargs):
        try:
            instance = kwargs['instance']
            return JFSACupForm(instance=instance)
        except KeyError:
            return JFSACupForm

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context = dict( backend_form = JFSACupForm())
        extra_context['form'] = self.get_form(request.POST,request.FILES)
        return super(JFSACupMediaAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        post = JFSACupMedia.objects.get(id=object_id)
        extra_context["form"] = post.instance
        return super(JFSACupMediaAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)
#
    def save_model(self, request, obj, form, change):
        obj.save()
        images = request.FILES.getlist('images')
        for image in images:
            JFSACupMedia.objects.create(images=image)
        return super().save_model(request, obj, form, change)


admin.site.register(Team)
admin.site.register(NationalMember)
admin.site.register(Position)
admin.site.register(Member)
admin.site.register(Tag)
admin.site.register(NewsPost)
admin.site.register(Event)
admin.site.register(Race)
admin.site.register(JFSACupResult)
admin.site.register(JFSACupRecord)
