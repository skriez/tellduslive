#!/usr/bin/python

from setuptools import setup

setup(name="tellduslocalapi",
      version='0.0.1',
      description="Communicate with Telldus Local API",
      url="https://github.com/skriez/tellduslocalapi",
      license="",
      author="Emil",
      author_email="emil+github@nylind.se",
      install_requires=['requests',
                        'requests_oauthlib'],
      py_modules=["tellduslocalapi"],
      provides=["tellduslocalapi"],)
