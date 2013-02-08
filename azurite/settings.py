from django.conf import settings

AZURITE = {
    'account_name': None,
    'container': None,
    'static_container': None,
    'account_key': None,
    'cdn_host': None,
    'use_ssl': False,
}

if hasattr(settings, 'AZURITE'):
    AZURITE.update(settings.AZURITE)
