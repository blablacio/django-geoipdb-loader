from __future__ import absolute_import

import io
import os
import re
from glob import glob

from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='django-geoipdb-loader',
    version='0.1.0',
    description="Helps download and keep updated maxmind's geoip db required for django GeoIP",
    long_description='%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
    ),
    author='Konstantin Alekseev',
    author_email='kv.alekseev@gmail.com',
    url='https://github.com/kalekseev/django-geoipdb-loader',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    keywords=['django', 'geoip'],
)
