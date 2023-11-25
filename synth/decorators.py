from django.core.exceptions import PermissionDenied

def check_user_is_member(function):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="members").exists():
            return function(request, *args, **kwargs)
        raise PermissionDenied()

    return wrapper

def check_user_is_staff(function):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="staff").exists():
            return function(request, *args, **kwargs)
        raise PermissionDenied()

    return wrapper