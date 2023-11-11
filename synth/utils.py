

# This files "resides" on the project level and is imported in views.py in the other apps
# It consists of helper-classes that are needed in many places and is used in this manner
# to stick to the DRY principle.

from products.models import product,genre,mediatype
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
    
# only imported in core/views.py to restrict users to main-links
# that is, if there is a class-based view in the profiles app that only
# staff-members should be able to access, import that view in that app

class StaffRequiredMixin(UserPassesTestMixin):
    '''Class used to restrict access to views where user needs to be a staff member '''

    def test_func(self):
        return self.request.user.groups.filter(name="staff").exists()

class AdminRequiredMixin(UserPassesTestMixin):
    '''Class used to restrict access to views where user needs to be admin '''

    def test_func(self):
        return self.request.user.groups.filter(name="admins").exists()

class MemberRequiredMixin(UserPassesTestMixin):
    '''Class used to restrict access to views where user needs to be a member '''
    
    # All registered users are automatically a part of this group. It makes
    # it easier to "lock down" certain views from users not logged in.

    def test_func(self):
        return self.request.user.groups.filter(name="members").exists()

