from rest_framework.permissions import BasePermission


class ReaderPermission(BasePermission):
    """ Проверка, что пользователь активен. """

    def has_permission(self, request, view):
        return request.user.is_staff
