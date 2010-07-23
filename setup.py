try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='django-nose-rollback',
    description='Nose plugin for use with django-nose to rollback after each test.',
    py_modules=['rollback'],
    version='0.1',
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'django-rollback = rollback:DjangoRollbackPlugin'
        ]
    }
)