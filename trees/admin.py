from django.contrib import admin

from .models import Square, Specie, Tree, Family

@admin.register(Square)
class SquereAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_display", 
        "description", 
        "address", 
        "image1",
        "altimg1", 
        "image2",
        "altimg2", 
        "image3",
        "altimg3", 
        "slug", 
        "created", 
        "modified",
        ]
    list_editable = [
        "description",
        "is_display",
        "address",
        "altimg1",
        "altimg2",
        "altimg3",
        ]


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created", "modified"]

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created", "modified"]




@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "specie",
        "family",
        "square",
        "slug",
        "is_display",
        "created",
        "modified",
        "image1",
        "altimg1",
        "image2",
        "altimg2",
        "image3",
        "altimg3",
        "source",
        "quantidade",
    ]
    list_filter = ["is_display", "created", "modified"]
    list_editable = [
        "is_display",
        "source",
        "quantidade", 
        "altimg1",
        "altimg2",
        "altimg3",
        ]