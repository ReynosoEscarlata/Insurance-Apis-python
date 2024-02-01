from django.contrib.auth.mixins import UserPassesTestMixin

class ManagerRequired(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="manager").exists()

