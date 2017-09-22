from setuptools import setup

setup(
    name='sfmgr',
    version='1.1',
    description='Manage scripts and files in WPM',
    url='https://github.com/sbarbett/sfmgr',
    author='Shane Barbetta',
    author_email='shane@barbetta.me',
    license='GNU General Public License v3 or later (GPLv3+)',
    keywords='sfmgr',
    packages=['sfmgr'],
    package_dir={'sfmgr': 'src'},
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    zip_safe=False
)