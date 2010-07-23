from nose.plugins import Plugin
from django.db.transaction import enter_transaction_management, managed, rollback, leave_transaction_management

savepoint  = None

class DjangoRollbackPlugin(Plugin):
    """Rollback transaction after each test"""

    name = 'django-rollback'
    enabled = True
    env_opt = 'DJANGO_NOSE_WITHOUT_ROLLBACK'
    score = 2000

    def __init__(self):
        Plugin.__init__(self)

    def options(self, parser, env):
        parser.add_option('--without-django-rollback',
                          action='store_false',
                          default=not env.get(self.env_opt),
                          dest='rollback',
                          help=('Do not rollback after each test.'),
                         )

    def configure(self, options, conf):
        self.conf = conf
        if not options.rollback:
            self.enabled = False

    def beforeTest(self, test):
        enter_transaction_management()
        managed(True)
        
    def afterTest(self, test):
        rollback()
        leave_transaction_management()
