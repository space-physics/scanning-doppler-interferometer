#!/usr/bin/env python
install_requires = ['python-dateutil','pandas']
tests_require = ['pytest','nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='ScanningDopplerInterferometer',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      version='0.5.0',
      url='https://github.com/scivision/scanning-doppler-interferometer',
      long_description=open('README.rst').read(),
      description="easily download and plot Mark Conde's Scanning Doppler Interferometer data",
      classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Science/Research',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      ],
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require,
                      'plots':['matplotlib'],},
      python_requires='>=3.6',
      scripts=['PlotWinds.py']
	  )

