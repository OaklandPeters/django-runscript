from setuptools import setup

setup(
    name='django-runscript',
    version=open('VERSION').read().strip(),
    author='Oakland John Peters',
    author_email='oakland.peters@gmail.com',

    description="Runs Python script from the command-line, while providing the Django environment.",
    long_description=open('README.rst').read(),
    url='https://github.com/OaklandPeters/django-runscript',
    license='MIT',

    packages=['django-runscript'],

    include_package_data=True,

    classifiers=[
        #Select one 'Development Status'
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ]
)
