from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Category, Game, Image 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_slug']
    prepopulated_fields = {'category_slug': ('category_name',)}


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True  # Enable image deletion


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'console_type', 'details', 'category', 'game_slug']
    list_editable = ['category', 'price']
    list_filter = ['category', 'price']
    prepopulated_fields = {'game_slug': ('name',)}
    inlines = [ImageInline]

    def get_formsets(self, request, obj=None):
        """Enable formset for inline images."""
        formsets = super().get_formsets(request, obj)
        if obj:
            for formset in formsets:
                if issubclass(formset.model, Image):
                    formset.queryset = formset.model.objects.filter(game=obj)
        return formsets


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['game_id', 'image']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = ('email',)











