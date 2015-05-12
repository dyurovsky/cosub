from setuptools import setup

setup(name='cosub_lc',
      version='0.1',
      description='A tool for managing external HITs on Mechanical Turk',
      author='Long Ouyang',
      author_email='long.ouyang@gmail.com',
      url='http://www.github.com/dyurovsky/cosub',
      packages=['cosub_lc'],
      install_requires = ['boto >= 2.33.0','pytimeparse >= 1.1.2'],
      entry_points = {
        'console_scripts': [
          'cosub = cosub_lc.runner:go'
        ]
      }
)
