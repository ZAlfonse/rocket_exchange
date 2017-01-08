from django.db.models.signals import pre_save
from django.dispatch import receiver

from datetime import datetime

from social_django.models import UserSocialAuth


@receiver(pre_save, sender=UserSocialAuth, dispatch_uid="steam_pre_save_user_sync")
def udpate_steam_data(sender, instance, **kwargs):
    if 'player' in instance.extra_data:
        user = instance.user
        user.steam_id = instance.extra_data['player']['steamid']
        user.steam_persona = instance.extra_data['player']['personaname']
        user.steam_profile = instance.extra_data['player']['profileurl']
        user.steam_avatar = instance.extra_data['player']['avatar']
        user.steam_created = datetime.fromtimestamp(int(instance.extra_data['player']['timecreated']))
        user.save()
