from attendee_tournaments import *


@all_renderable(c.STUFF)
class Root:
    def index(self, session, message=''):
        return {
            'message': message,
            'applications': session.query(AttendeeTournament).order_by('first_name', 'last_name').all()
        }

    def app(self, session, message='', **params):
        app = session.attendee_tournament(params)
        if cherrypy.request.method == 'POST':
            if app.status == c.NEW:
                message = 'You did not indicate whether to accept or decline this application'
            else:
                raise HTTPRedirect('index?message={}{}{}', app.game, ' was marked as ', app.status_label)

        return {
            'app': app,
            'message': message
        }

    @csv_file
    def everything(self, out, session):
        out.writerow([
            'Status', 'Applicant Name', 'Applicant Email', 'Applicant Cellphone', 'Game', 'Availability',
            'Format', 'Experience', 'Needs', 'Why?', 'Volunteers to Run Other Tournaments'
        ])
        for app in session.query(AttendeeTournament).order_by('status', 'game').all():
            out.writerow([
                app.status_label, app.full_name, app.email, app.cellphone, app.game, '\n'.join(app.availability_labels),
                app.format, app.experience, app.needs, app.why, 'yes' if app.volunteering else 'no'
            ])
