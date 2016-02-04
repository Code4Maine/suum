from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

version = __import__('suum').__version__

install_requires = [
    'setuptools==18.0.1',
    'Django==1.9.2',
    'django_configurations==1.0',
    'dj-database-url==0.3.0',
    'pylibmc==1.5.0',
    'Pillow==2.0.0',
    'django-cache-url==0.8.0',
    'werkzeug==0.9.4',
    'gunicorn==0.17.4',
    'easy-thumbnails==1.2',
    'django-debug-toolbar==1.4',
    'django-extensions==1.6.1',
    'django-braces==1.4.0',
    'django-localflavor==1.1',
    'django-allauth==0.24.1',
    'django-floppyforms==1.6.1',
    'django-custom-user==0.5',
    'django-nose==1.4.1',
    'raven==5.2.0',
    'factory_boy==2.5.1',
    'boto==2.39.0',
    'django-storages==1.1.8',
    'djangorestframework==3.3.2',
    'django-cors-headers==1.1.0',
    'markdown==2.6.1',
    'django-filter==0.9.2',
    'django-templated-email==0.4.9',
    'psycopg2==2.5'
]

# App specific libraries
install_requires += [
]

dep_links = [
    "https://onec-pypicloud.s3.amazonaws.com/6f45/django_configurations/django-configurations-0.9-sbrandtb.tar.gz?Signature=szSuFV7%2F0uBGsNZo53tOLbQx0j8%3D&Expires=1438552169&AWSAccessKeyId=AKIAIYMHQ75FUPRJ7C4Q#egg=django-configurations-0.9-sbrandtb"
]


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name="suum",
    version=version,
    url='http://github.com/powellc/suum',
    license='BSD',
    platforms=['OS Independent'],
    description="An suum for django applications.",
    author="Colin Powell",
    author_email='colin.powell@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    #dependency_links=dep_links,
    include_package_data=True,
    zip_safe=False,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'suum': 'suum',
        'suum/templates': 'suum/templates',
    },
    entry_points={
        'console_scripts': [
            'suum = suum.manage_suum:main',
        ],
    },
)
