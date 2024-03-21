from django.contrib import admin
from django.utils.html import format_html
from myapp.models import About,Service,Project,Testimonial,Team,Contact,Blog,User
from django.utils.safestring import mark_safe


# Define AboutAdmin class here
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content1', 'content2', 'display_image1', 'display_image2']

    def display_image1(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.image1.url))

    def display_image2(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.image2.url))

    display_image1.short_description = 'Image 1'
    display_image2.short_description = 'Image 2'






# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display = ['full_name', 'designation', 'display_image']
#     readonly_fields = ['display_image']

#     def display_image(self, obj):
#         return obj.image.url if obj.image else None
#     display_image.short_description = 'Image'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'display_image']

    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return 'No Image'

    display_image.short_description = 'Image Preview'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('text1', 'text2', 'display_image')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'





class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession', 'display_image', 'stars', 'comment')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url)) if obj.image else None
    display_image.short_description = 'Image'

    def stars(self, obj):
        return obj.stars  # This returns the value of the 'stars' field
    stars.short_description = 'Stars'

   
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'designation', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date_published', 'image_display')
    search_fields = ('title', 'category', 'author')
    list_filter = ('category', 'author', 'date_published')
    readonly_fields = ('date_published', 'image_display')
    
    def image_display(self, obj):
        return '<a href="{0}" target="_blank"><img src="{0}" style="max-height: 100px; max-width: 100px;" /></a>'.format(obj.image.url)
    image_display.allow_tags = True
    image_display.short_description = 'Image'
    

    def author_image_display(self, obj):
        return '<a href="{0}" target="_blank"><img src="{0}" style="max-height: 100px; max-width: 100px;" /></a>'.format(obj.author_image.url)
    author_image_display.allow_tags = True
    author_image_display.short_description = 'Author Image'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'number', 'message', 'added_on', 'is_approve']

# Register AboutAdmin with the Django admin site
admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin) 
admin.site.register(Testimonial, TestimonialAdmin)   
admin.site.register(Team, TeamAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(User)








# Optionally, customize the Django admin site header
admin.site.site_header = "Clicker|Admin"
