# Generated by Django 2.1.2 on 2019-04-08 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0015_auto_20190408_1321'),
    ]

    def forwards_func(apps, schema_editor):
        Setting = apps.get_model("openshift_api", "Setting")
        db_alias = schema_editor.connection.alias
        Setting.objects.using(db_alias).bulk_create([
            Setting(name="仓库地址", key="registry_hostname", order=3, value=None,
                    helper="eg:192.168.1.1"),
        ])

    def reverse_func(apps, schema_editor):
        Setting = apps.get_model("openshift_api", "Setting")
        db_alias = schema_editor.connection.alias
        Setting.objects.using(db_alias).filter(key='registry_hostname').delete()

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]