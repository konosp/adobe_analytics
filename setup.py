from setuptools import setup, find_packages

setup(name='python-omniture',
      description='A wrapper for the Adobe Omniture and SiteCatalyst web analytics API.',
      long_description=open('README.md').read(),
      author='Stijn Debrouwere',
      author_email='stijn@stdout.be',
      url='http://stdbrouw.github.com/python-omniture/',
      download_url='http://www.github.com/stdbrouw/python-omniture/tarball/master',
      version='0.1.1',
      license='MIT',
      packages=find_packages(),
      keywords='data analytics api wrapper adobe',
      install_requires=[
            'requests',
      ],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   ],
      )