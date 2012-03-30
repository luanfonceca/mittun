from django.contrib import admin

from mittun.sponsors.models import Sponsor, Category, Contact, Job, Requirement, Responsibility, Bonus


class ContactInline(admin.TabularInline):
    model = Contact


class ContactAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):

    inlines = [
        ContactInline,
    ]

    def queryset(self, request):
        qs = super(SponsorAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def change_view(self, request, object_id, extra_context=None):
        sponsor = Sponsor.objects.get(id=object_id)
        if request.user == sponsor.user:
            self.exclude = ('user',)
        else:
            self.exclude = ()
        return super(SponsorAdmin, self).change_view(request, object_id, extra_context)


if Contact not in admin.site._registry:
    admin.site.register(Contact, ContactAdmin)

if Sponsor not in admin.site._registry:
    admin.site.register(Sponsor, SponsorAdmin)

if Category not in admin.site._registry:
    admin.site.register(Category)

if Job not in admin.site._registry:
    admin.site.register(Job)

if Responsibility not in admin.site._registry:
    admin.site.register(Responsibility)

if Requirement not in admin.site._registry:
    admin.site.register(Requirement)

if Bonus not in admin.site._registry:
    admin.site.register(Bonus)

