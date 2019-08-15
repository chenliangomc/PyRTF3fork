classifiers = """\
Development Status :: 4 - Beta
Topic :: Text Editors :: Text Processing
Topic :: Software Development :: Libraries :: Python Modules
Intended Audience :: Developers
Programming Language :: Python
License :: OSI Approved :: GNU General Public License (GPL)
"""

import sys
import os

from setuptools import setup, find_packages

setup(
    name='PyRTF3',
    author='Mars Galactic',
    author_email='xoviat@noreply.users.github.com',
    url='https://github.com/xoviat/pyrtf',
    license='http://www.gnu.org/licenses/gpl.html',
    platforms=['Any'],
    install_requires=['PyParsing'],
    setup_requires=[
        'setuptools-markdown',
        'setuptools_scm',
    ],
    use_scm_version=True,
    description='PyRTF - Rich Text Format Document Generation',
    classifiers=[_f for _f in classifiers.split('\n') if _f],
    keywords=('RTF', 'Rich Text', 'Rich Text Format', 'documentation',
              'reports'),
    long_description_markdown_filename='README.md',
    packages=find_packages())
