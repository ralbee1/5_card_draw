#Package the pip according to Python documentation https://packaging.python.org/en/latest/specifications/
#Choosing a license https://gist.github.com/nicolasdao/a7adda51f2f185e8d2700e1573d8a633
'''Setup file for building a pip for a module.

INSTRUCTIONS FOR BUILDING A PIP https://pip.pypa.io/en/stable/cli/pip_wheel/

Install Prequisites: py -m pip install --upgrade pip setuptools wheel twine build
Build Pip Distributable: py -m build --wheel from the /PythonTools/ directory with this setup.py in it.

#Developer Install: "py -m pip install -e ." from this folder.
#User Install: Install from the global pip.

To build the pip module, increment the version number in the setup.py file and run the following command, uploading the generated package in dist/ for others to install and use.
'''
import os
from pathlib import Path
import setuptools

requires = [
    'tkinter',
    'pathlib',
]

scripts = [
    str(Path('video_poker','video_poker.py'))
]


setuptools.setup(
    name = '5_card_draw',
    version = os.getenv('PACKAGE_VERSION', '0.0.dev0'),
    description = 'Video Poker application for 5 card draw poker in video poker format.',
    author = 'Richard Albee',
    author_email='ralbee1@iwu.edu',
    packages = setuptools.find_packages(),
    install_requires = requires,
    scripts = scripts,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    python_requires = '>=3.8',
    url = "https://github.com/ralbee1/VideoPoker-5CardRedraw"
)
