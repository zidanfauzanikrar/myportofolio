from django.contrib.auth.management import create_permissions
from django.db import migrations

EDITOR_CODENAMES = ["change_skill", "change_experience"]


def ensure_editor_permissions(apps, schema_editor):
    # Baris Permission biasanya baru dibuat oleh sinyal post_migrate, yaitu SETELAH
    # semua migrasi selesai. Pada database baru, migrasi 0004 melihat tabel izin
    # kosong sehingga Group "Editor" dibuat tanpa izin. Buat izinnya sekarang.
    main_config = apps.get_app_config("main")
    main_config.models_module = True  # create_permissions berhenti jika None
    try:
        create_permissions(
            main_config,
            apps=apps,
            verbosity=0,
            using=schema_editor.connection.alias,
        )
    finally:
        main_config.models_module = None

    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    editor_group, _ = Group.objects.get_or_create(name="Editor")
    permissions = Permission.objects.filter(
        content_type__app_label="main",
        codename__in=EDITOR_CODENAMES,
    )
    # add(), bukan set(): izin tambahan yang diberikan lewat admin tidak terhapus.
    editor_group.permissions.add(*permissions)


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_create_editor_group"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        # Rollback tidak melakukan apa pun: Group dihapus oleh rollback 0004.
        migrations.RunPython(ensure_editor_permissions, migrations.RunPython.noop),
    ]