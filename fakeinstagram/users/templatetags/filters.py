from django import template
register = template.Library()

@register.filter(name='following')
def following(user,request_user):
    if request_user.following.filter(id = user.id):
        print("holaaaaaaaa")
        return True
    print("uenooooooo")
    return False
