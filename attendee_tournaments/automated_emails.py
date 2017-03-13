from attendee_tournaments import *

AutomatedEmail.queries[AttendeeTournament] = lambda session: session.query(AttendeeTournament).all()

AutomatedEmail(AttendeeTournament, 'Your tournament application has been received', 'tournament_app_received.txt',
               lambda app: app.status == c.NEW,
               ident='tournament_app_received')

AutomatedEmail(AttendeeTournament, 'Your tournament application has been approved', 'tournament_app_accepted.txt',
               lambda app: app.status == c.ACCEPTED,
               ident='tournament_app_accepted')

AutomatedEmail(AttendeeTournament, 'Your tournament application has been declined', 'tournament_app_declined.txt',
               lambda app: app.status == c.DECLINED,
               ident='tournament_app_declined')
