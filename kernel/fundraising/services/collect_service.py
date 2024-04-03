# -*- coding: utf-8 -*-


from typing import Optional
from datetime import datetime

from django.db.transaction import atomic
from users.models import UserProfile

from fundraising.models import Collect
