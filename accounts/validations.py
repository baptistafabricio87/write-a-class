from django.contrib.auth.models import User


def empty_field(field):
    return not field.strip()


def registered_account(username, email):
    return (
            User.objects.filter(email=email).exists()
            or User.objects.filter(username=username).exists()
    )


def different_passwords(password_1, password_2):
    return password_1 != password_2


def password_greater_than_eight(password_1, password_2):
    return (len(password_1) >= 8) and (len(password_2) >= 8)
