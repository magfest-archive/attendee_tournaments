from attendee_tournaments import *

AttendeeTournament.required = [
    ('first_name', 'First Name'),
    ('last_name', 'Last Name'),
    ('email', 'Email Address'),
    ('game', 'Game Title'),
    ('availability', 'Your Availability'),
    ('format', 'Tournament Format'),
    ('experience', 'Past Experience'),
    ('needs', 'Your Needs'),
    ('why', '"Why?"'),
]


@validation.AttendeeTournament
def email(app):
    if not re.match(c.EMAIL_RE, app.email):
        return 'You did not enter a valid email address'


@validation.AttendeeTournament
def cellphone(app):
    from uber.model_checks import _invalid_phone_number
    if app.cellphone and _invalid_phone_number(app.cellphone):
        return 'You did not enter a valid cellphone number'
