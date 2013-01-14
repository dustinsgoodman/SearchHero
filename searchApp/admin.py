from searchApp.models import User,Game_History,Path,Question
from django.contrib import admin

#BR:ToDo make fields modifiable in admin view 
admin.site.register(User)
admin.site.register(Game_History)
admin.site.register(Path)
admin.site.register(Question)
