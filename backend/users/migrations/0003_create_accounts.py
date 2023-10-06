from django.db import migrations


def generate_thumbnail_sizes(apps, schema_editor):
    ThumbnailSize = apps.get_model('users', 'ThumbnailSize')
    ThumbnailSize.objects.bulk_create(
        [
            ThumbnailSize(size=200),
            ThumbnailSize(size=400),
        ]
    )


def generate_accounts(apps, schema_editor):
    Account = apps.get_model('users', 'Account')
    ThumbnailSize = apps.get_model('users', 'ThumbnailSize')
    Account.objects.bulk_create(
        [
            Account(name='Basic'),
            Account(name='Premium', has_link=True),
            Account(name='Enterprise', has_link=True, has_expiring_link=True),
        ]
    )

    Account.objects.get(name='Basic').thumbnail_sizes.add(ThumbnailSize.objects.get(size=200))
    Account.objects.get(name='Premium').thumbnail_sizes.add(ThumbnailSize.objects.get(size=200),
                                                           ThumbnailSize.objects.get(size=400))
    Account.objects.get(name='Enterprise').thumbnail_sizes.add(ThumbnailSize.objects.get(size=200),
                                                              ThumbnailSize.objects.get(size=400))


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_thumbnail_sizes),
        migrations.RunPython(generate_accounts)
    ]
