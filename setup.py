# -*- coding: utf-8 -*-

from setuptools import setup


requires = [ "paramiko" ]


setup(name='pyoecli',
      version='0.1',
      description='Open-E JovianDSS CLI Python bindings',
      url='http://github.com/raveenpl/pyoecli',
      author='Piotr Kandziora',
      author_email='raveenpl@gmail.com',
      install_requires = requires,
      data_files = [ ('/etc/oecli', ['data/ssh.conf']) ],
      packages=['pyoecli'],
      zip_safe=False)

