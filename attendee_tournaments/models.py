from attendee_tournaments import *


class AttendeeTournament(MagModel):
    first_name   = Column(UnicodeText)
    last_name    = Column(UnicodeText)
    email        = Column(UnicodeText)
    cellphone    = Column(UnicodeText)
    game         = Column(UnicodeText)
    availability = Column(MultiChoice(c.TOURNAMENT_AVAILABILITY_OPTS))
    format       = Column(UnicodeText)
    experience   = Column(UnicodeText)
    needs        = Column(UnicodeText)
    why          = Column(UnicodeText)
    volunteering = Column(Boolean, default=False)

    status = Column(Choice(c.TOURNAMENT_STATUS_OPTS), default=c.NEW, admin_only=True)

    email_model_name = 'app'
