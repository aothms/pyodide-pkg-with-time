from setuptools import setup

setup(name='mytime',
      version='0.1.0',
      description='',
      author='Thomas Krijnen',
      author_email='thomas@aecgeeks.com',
      packages=['mytime'],
      package_dir={'mytime': 'build'},
      package_data={'': ['*.so']},
)
