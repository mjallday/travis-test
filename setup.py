import re
from setuptools import setup, find_packages


packages = find_packages('.', exclude=('tests', 'tests.*', 'db', 'db.*'))


def find_version():
    return (
        re
        .compile(r".*__version__ = '(.*?)'", re.S)
        .match(open('balanced_service/__init__.py').read())
        .group(1)
    )


version = find_version()

tests_require = [
    'mock >= 0.8, < 0.9',
    'nose >=1.1.0',
]

setup(
    name='balanced_service',
    version=version,
    url='http://github.com/balanced/balanced',
    author='Balanced',
    author_email='dev@balancedpayments.com',
    packages=packages,
    scripts=[
        'bin/balanced',
        'bin/balancedd',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
       # performance & eventloops
        'cython==0.20.1',
        'gevent ==1.0',

        # web
        'gunicorn ==18.0.1bninja0',
        'boto ==2.28.0',

        # utilities
        'blinker>=1.2',
        'iso3166',
        'iso8601',
        'netaddr==0.7.10',
        'python-daemon==1.6',
        'jsonschema==2.3.0',
        'jsonpatch==1.3',
        'simplejson==2.3.2',
        'setproctitle>=1.1',
        'python-dateutil>=1.5,<2.0',

        # monitoring
        'newrelic>=1.13.1.31,<2.0',

        # datastore clients
        'mongoengine==0.7.9',
        'pyes==0.90.1',
        'python-statsd<1.5.8',
        'psycopg2>=2.3',
        'redis ==2.9.1',

        # sqlalchemy & extensions
        'SQLAlchemy==0.8.4',
        'sqlalchemy-migrate==0.8.2',
        'sqlalchemy-citext',

        # balanced
        'sterling[util,web,db,messaging,templating] ==3.2.7',
        'precog==2.42.4',
    ],
    extras_require={
        'tests': tests_require,
    },
    tests_require=tests_require,
)
