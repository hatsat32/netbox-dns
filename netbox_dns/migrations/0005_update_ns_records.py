# Generated by Django 3.2.9 on 2021-11-26 07:01

from django.db import migrations
from netbox_dns.models import Zone, Record


def create_initial_ns_records(apps, schema_editor):
    Zone = apps.get_model("netbox_dns", "Zone")

    for zone in Zone.objects.all():
        nameservers = zone.nameservers.all()
        nameserver_names = [f'{ns.name.rstrip(".")}.' for ns in nameservers]

        ns_name = "@"
        ns_ttl = zone.default_ttl

        delete_ns = zone.record_set.filter(type=Record.NS, managed=True).exclude(
            value__in=nameserver_names
        )
        for record in delete_ns:
            record.delete()

        for ns in nameserver_names:
            Record.objects.update_or_create(
                zone_id=zone.pk,
                type=Record.NS,
                name=ns_name,
                ttl=ns_ttl,
                value=ns,
                managed=True,
            )


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_dns", "0004_create_ptr_for_a_aaaa_records"),
    ]

    operations = [
        migrations.RunPython(create_initial_ns_records),
    ]
