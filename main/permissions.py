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


def IsPortfolioOwnerOrEditorOrReadOnly(model):
    """Membuat kelas permission untuk satu model (dipakai di @permission_classes).

    Pemakaian: @permission_classes([IsPortfolioOwnerOrEditorOrReadOnly(Skill)])

    - Baca (GET/HEAD/OPTIONS): terbuka untuk semua orang.
    - PUT/PATCH: butuh izin change_<model>, dimiliki pemilik (superuser) dan Editor.
    - POST: butuh izin add_<model>; DELETE: butuh izin delete_<model>.
      Editor hanya diberi change_*, jadi ditolak untuk create dan delete.

    Izin dicek dengan has_perm (Django Permission), bukan nama Group, sehingga
    mencabut izin di admin langsung mencabut akses.

    Catatan: ini izin berbasis peran untuk SATU portofolio. Pemeriksaan ini
    berlaku di level view/model dan tidak menyaring objek milik pengguna lain.
    Kalau aplikasi kelak punya banyak pemilik dan data privat, pemeriksaan
    objek (has_object_permission) dan pembatasan queryset perlu didesain
    tersendiri.
    """

    class _IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
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

    _IsPortfolioOwnerOrEditorOrReadOnly.__name__ = f"IsPortfolioOwnerOrEditorOrReadOnly_{model.__name__}"
    return _IsPortfolioOwnerOrEditorOrReadOnly