import xadmin
from xadmin import views


class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "应心"
    # 修改footer
    site_footer = '应心后台'
    #菜单收缩
    menu_style = "accordion"

from base.models import Dict, User, School, Role, Topic, Activity, Image, Comment, Collect, Like


class DictAdmin(object):
    list_display = ['item_name', 'item_code', 'created_time']
    search_fields = ['item_name']
    list_filter = ['item_name', 'item_code']

class UserAdmin(object):
    list_display = ['open_id', 'mobile', 'is_authenticated', 'role_code', 'gender', 'auth_img', 'created_time']
    search_fields = ['mobile', 'is_authenticated', 'role_code', 'gender']
    list_filter = ['mobile', 'is_authenticated', 'role_code', 'gender']

class SchoolAdmin(object):
    list_display = ['name', 'address', 'created_time']
    search_fields = ['name', 'address']
    list_filter = ['name', 'address']

class RoleAdmin(object):
    list_display = ['name', 'code', 'created_time']
    search_fields = ['name']
    list_filter = ['name', 'code']

class TopicAdmin(object):
    list_display = ['user_id', 'content', 'created_time']
    search_fields = ['user_id', 'content']
    list_filter = ['user_id']

class ActivityAdmin(object):
    list_display = ['user_id', 'title', 'content', 'start_time', 'end_time', 'place', 'contact_wx', 'created_time']
    search_fields = ['user_id', 'title', 'content', 'start_time', 'end_time', 'place', 'contact_wx']
    list_filter = ['user_id', 'title', 'start_time', 'end_time', 'place']

class ImageAdmin(object):
    list_display = ['user_id', 'path', 'item_code', 'created_time']
    search_fields = ['user_id', 'item_code']
    list_filter = ['user_id', 'item_code']

class CollectAdmin(object):
    list_display = ['user_id', 'item_code', 'created_time']
    search_fields = ['user_id']
    list_filter = ['user_id', 'item_code']

class LikeAdmin(object):
    list_display = ['user_id', 'item_code', 'created_time']
    search_fields = ['user_id']
    list_filter = ['user_id', 'item_code']

class CommentAdmin(object):
    list_display = ['user_id', 'content', 'item_code', 'father_id', 'created_time']
    search_fields = ['user_id', 'item_code']
    list_filter = ['user_id', 'item_code']

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Dict, DictAdmin)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(School, SchoolAdmin)
xadmin.site.register(Role, RoleAdmin)
xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Activity, ActivityAdmin)
xadmin.site.register(Image, ImageAdmin)
xadmin.site.register(Collect, CollectAdmin)
xadmin.site.register(Like, LikeAdmin)
xadmin.site.register(Comment, CommentAdmin)


