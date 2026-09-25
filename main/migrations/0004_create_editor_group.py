from django.db import migrations

def create_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    editor_group, _ = Group.objects.get_or_create(name="Editor")

    permissions = Permission.objects.filter(
        content_type__app_label="main",
        codename__in=["change_skill", "change_experience"],
    )
    editor_group.permissions.set(permissions)

def remove_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Editor").delete()

class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_experience_starred_by_skill_starred_by"),
    ]

    operations = [
        migrations.RunPython(create_editor_group, remove_editor_group),
    ]