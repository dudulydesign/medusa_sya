


def init_takeleave():
  from takeleave.models import Category
  takeleave_categories = {
    1: {"name": u"病假"},
    2: {"name": u"公假"},
    3: {"name": u"事假"},
    4: {"name": u"其它"},
      }

  for id, item in takeleave_categories.items():
    try:
      cat = Category.objects.get(id=id)
    except Category.DoesNotExist:
      cat = Category(id=id, ordering=0)

    cat.name = item["name"]
    cat.save()
    print "save takeleave category=%s name=%s" % (cat.id, cat.name)


def init_test_users():
  from django.contrib.auth.models import User


  for i in range(10):
    username="testuser%s" % str(i).zfill(2)

    try:
      u = User.objects.get(username=username)
    except User.DoesNotExist:
      u = User(
          username=username,
          is_active=True
          )

    u.set_password("12345678")
    u.save()
    print "new user=%s" % username

def main():
  import random
  import uuid
  import time
  from datetime import datetime, timedelta
  from django.utils import timezone

  init_test_users()
  init_takeleave()
