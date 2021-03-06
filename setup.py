import os
from setuptools import setup, find_packages

def read(descfile):
    return open( os.path.join ( os.path.dirname(__file__), descfile)).read()

setup(
    name='scsqc',

    version='1.0.1',

    author='Venkat Kaushik',

    author_email='higgsmass@gmail.com',

    maintainer='Venkat Kaushik',

    maintainer_email='higgsmass@gmail.com',

    url='https://github.com/higgsmass/scsqc',

    description= ('SC Surgical Quality Collaborative - DataMove/DataMart') ,

    long_description = read('README.md'),

    platforms="platform-independent",

    license='MIT',

    packages= find_packages('src'),

    package_dir = {'':'src'},

    package_data = {
        'response': ['data/*'],
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Health IT :: Datamart',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],

    install_requires = [
        'warnings',
    ],

    setup_requires = [
        'pbr',
    ],

    test_suite='nose.collector',
    tests_require=['nose'],

    entry_points = {
        'console_scripts': ['scsqc-start=scsqc.command_line:main'],
    },

    scripts=[
        'bin/scsqc'
    ],

    pbr=True,
    zip_safe=False,
    include_package_data=True,

)
