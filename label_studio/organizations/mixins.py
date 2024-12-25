class OrganizationMixin:
    @property
    def active_members(self):
        return self.members


class OrganizationMemberMixin:
    def has_permission(self, user):
        if user.is_superuser is True or self.members.filter(id=user.id).exists():
            return True
        return False
