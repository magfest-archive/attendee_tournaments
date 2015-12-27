from attendee_tournaments import *


@Session.model_mixin
class Attendee:
    @property
    def paid_for_badge(self):
        return bool(self.paid == c.HAS_PAID or self.group_id and self.group and self.group.amount_paid)


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

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def matching_attendee(self):
        return self.session.query(Attendee).filter(
            Attendee.first_name == self.first_name.title(),
            Attendee.last_name == self.last_name.title(),
            func.lower(Attendee.email) == self.email.lower()
        ).first()

