from django.contrib import admin

from real_estate_card.models import RealEstateActualUser, RealEstate, RealEstateOwner, RealEstatePhoto


@admin.register(RealEstateOwner)
class RealEstateOwnerAdmin(admin.ModelAdmin):
    list_display = ('passport', 'surname', 'first_name', 'last_name')
    list_display_links = ('passport', 'surname', 'first_name', 'last_name')


@admin.register(RealEstateActualUser)
class RealEstateActualUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'first_name', 'last_name')
    list_display_links = ('id', 'surname', 'first_name', 'last_name')


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'type', 'description', 'state')
    list_display_links = ('id', 'address', 'type', 'state')


@admin.register(RealEstatePhoto)
class RealEstatePhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'real_estate')
    list_display_links = ('id', 'title', 'real_estate')