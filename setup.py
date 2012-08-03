# -*- coding:utf-8 -*-

from distutils.core import setup

setup(
    name='Lausestaja',
    version='0.1dev',
    description='Jagab teksti lauseteks',
    author='Kristian Kankainen',
    author_email='kristian.kankainen@kuu.la',
    url='http://www.kuu.la/viki/keeleressursse',
    packages=['lausestaja'],
    package_dir={'lausestaja': 'src/lausestaja'},
    licensce='GNU GPL version 3 or any later version',
    long_description=open('README.txt').read(),
    )

