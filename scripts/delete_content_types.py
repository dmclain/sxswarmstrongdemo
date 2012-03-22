#!/usr/bin/env python
from django.contrib.contenttypes.models import ContentType

if __name__ == '__main__':
    ContentType.objects.all().delete()
