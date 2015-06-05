# -*- coding:utf-8 -*-

from distutils.core import setup

setup(
    name='Lausestaja',
    version='0.1',
    description='Jagab teksti lauseteks',
    author='Kristian Kankainen',
    author_email='kristian.kankainen@keeleleek.ee',
    url='http://www.keeleleek.ee/',
    packages=['lausestaja'],
    package_dir={'lausestaja': 'src/lausestaja'},
    package_data={'lausestaja': ['data/*.txt']},
    #scripts=['bin/proov1.py'],
    license='GNU GPL version 3 or any later version',
    long_description=open('README.txt').read(),
    requires=[
        "regex"
        ],
    )

