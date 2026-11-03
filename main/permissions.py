from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change portfolio items."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


ACTION_BY_METHOD = {
    "POST": "add",
    "PUT": "change",
    "PATCH": "change",
    "DELETE": "delete",
}


def has_model_permission(model):
    """Baca publik; tulis butuh izin Django model (add/change/delete_<model>).

    Superuser otomatis lolos. Group "Editor" (change_skill / change_experience)
    bisa update, tetapi tidak bisa delete kecuali diberi izin delete.
    """

    class HasModelPermission(BasePermission):
        message = "You do not have permission to perform this action."

        def has_permission(self, request, view):
            if request.method in SAFE_METHODS:
                return True
            action = ACTION_BY_METHOD.get(request.method)
            if action is None:
                return False
            opts = model._meta
            perm = f"{opts.app_label}.{action}_{opts.model_name}"
            return request.user.has_perm(perm)

    return HasModelPermission