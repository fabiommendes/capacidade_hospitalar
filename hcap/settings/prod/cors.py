"""
django:
    https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
"""

from hcap.settings.env import env

ALLOWED_HOSTS = env("HCAP__ALLOWED_HOSTS", default=[])
