from ast import Pass
import os

import django
from django.forms.models import model_to_dict

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print(model_to_dict(Passcard.objects.get(id=1)))
    print(Passcard.objects.filter(is_active=True).count())
