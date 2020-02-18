import sys
from setuptools import setup, setuptools
__author__ = "Yiming Lin"
__version__= "0.0.1"

if sys.version_info < (3, 4, 1):
    sys.exit('Python < 3.4.1 is not supported!')


setup(name='mtcnn',
      version=__version__,
      description='Multi-task Cascaded Convolutional Neural Networks for Face Detection, based on Pytorch',
      license='MIT',
      packages=setuptools.find_packages(exclude=["tests.*", "tests"]),
      install_requires=[
          "torch>=1.0.0",
          "Pillow>=6.0.0"
      ],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      keywords="mtcnn face detection",
      zip_safe=False)
