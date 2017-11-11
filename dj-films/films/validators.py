from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


GENRE = ['Action', 'Drama', 'Comedy', 'Horror', 'Westerns', 'War', 'Thriller', 'Other']

def validate_genre(value):
    g = value.capitalize()
    if not value in GENRE and not g in GENRE:
        raise ValidationError(f"{value} not a valid genre")