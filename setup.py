from setuptools import setup, find_packages

import os #import the os module

setup(
    name='django-website-showroom',
    version='0.4.0',
    description='General purpose showroom for presenting a collection of categorized websites',
    author='Holger Drewes',
    author_email='Holger.Drewes@gmail.com',
    url='https://github.com/holgerd77/django-website-showroom/',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    platforms=['OS Independent'],
    install_requires=[
        'Django>=1.11,<2.0',
        'django-haystack>=2.6,<2.7',
        'Whoosh>=2.7,<2.8',
        'Pillow',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
