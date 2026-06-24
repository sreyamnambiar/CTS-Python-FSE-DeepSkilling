from django.contrib import admin

from .models import Course, Department, Enrollment, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'credits', 'department')
	search_fields = ('name', 'code', 'department__name')
	list_filter = ('department', 'credits')


admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)
