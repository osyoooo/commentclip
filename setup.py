#!/usr/bin/env python3

from setuptools import setup

setup(
    name='commentclip',
    version='1.0.0',
    description='A tool to extract comments from source code files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='commentclip',
    py_modules=['commentclip'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'commentclip=commentclip:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
)