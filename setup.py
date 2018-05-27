from setuptools import setup, find_packages

setup(name='dpp_calendar_lib',
      version='0.3',
      author='Jan Pajdak',
      author_email='pajdakjan@gmail.com',
      url='https://github.com/janjpk/S6-DPP-10B',
      packages=find_packages(exclude=['tests*', 'dist*', 'setup*']),
      )
