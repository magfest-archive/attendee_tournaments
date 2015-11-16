from attendee_tournaments import *

AutomatedEmail.extra_models[AttendeeTournament] = lambda session: session.query(AttendeeTournament).all()

AutomatedEmail(AttendeeTournament, 'Your Attendee Tournament Application Has Been Received', 'tournament_app_received.txt',
               lambda app: True)
