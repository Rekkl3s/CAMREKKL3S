#!/usr/bin/env python3


from setuptools import setup, find_packages

setup(name='rekkles',
      version='1.0.0',
      description='rekkles is a tool that exploits several vulnerabilities in popular DVR cameras to obtain network camera credentials.',
      url='https://github.com/EntySec/rekkles',
      author='EntySec',
      author_email='alastorkls82@gmail.com',
      license='MIT',
      python_requires='>=3.7.0',
      packages=find_packages(),
      entry_points={
          "console_scripts": [
                "rekkles = rekkles.cli:main"
          ]
      },
      install_requires=[
          'shodan',
      ],
      zip_safe=False
)
