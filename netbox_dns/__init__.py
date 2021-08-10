from extras.plugins import PluginConfig

__version__ = "0.0.1"


class DnsConfig(PluginConfig):
    name = "netbox_dns"
    verbose_name = "Netbox Dns"
    description = "Netbox Dns"
    min_version = "2.11.9"
    max_version = None
    version = __version__
    author = "Aurora Research Lab"
    author_email = "info@aurorabilisim.com"
    required_settings = []
    default_settings = {"loud": False}


config = DnsConfig