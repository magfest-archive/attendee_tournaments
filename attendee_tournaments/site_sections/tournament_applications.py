from attendee_tournaments import *


@all_renderable()
class Root:
    def index(self, session, message='', **params):
        params.pop('id', None)  # don't allow editing of existing apps
        app = session.attendee_tournament(params)
        if cherrypy.request.method == 'POST':
            message = check(app)
            if not message:
                session.add(app)
                raise HTTPRedirect('index?message={}', 'Your application has been received')

        return {
            'app': app,
            'message': message
        }
