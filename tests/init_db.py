

def main():
  from django.contrib.auth.models import User

  username = "admin"
  try:

    user = User.objects.get(username=username)

  except User.DoesNotExist:
    user = User(username=username)

  user.set_password("12345678")
  user.is_superuser = True
  user.is_staff = True
  user.is_active = True

  user.save()

  username = "testuser1"
  try:

    user = User.objects.get(username=username)

  except User.DoesNotExist:
    user = User(username=username)

  user.set_password("12345678")
  user.is_active = True

  user.save()

