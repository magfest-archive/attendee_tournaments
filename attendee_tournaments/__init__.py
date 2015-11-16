from uber.common import *
from attendee_tournaments._version import __version__
from attendee_tournaments.config import *
from attendee_tournaments.models import *
import attendee_tournaments.model_checks
import attendee_tournaments.automated_emails

static_overrides(join(at_config['module_root'], 'static'))
template_overrides(join(at_config['module_root'], 'templates'))
mount_site_sections(at_config['module_root'])
