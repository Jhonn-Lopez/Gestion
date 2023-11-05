from django.contrib import admin
from .models import User, ActiveCurse, Alternative, CorrectAnswer, Curse, Module, Question

admin.site.register(User)
admin.site.register(ActiveCurse)
admin.site.register(Alternative)
admin.site.register(CorrectAnswer)
admin.site.register(Curse)
admin.site.register(Module)
admin.site.register(Question)
