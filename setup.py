from setuptools import setup

setup(
    name='codepen',
    version='1.0.0',
    license='MIT',
    author='Connor Kendrick',
    author_email='connorkendrickmusic@gmail.com',
    description='A Python wrapper for the unofficial CodePen API',
    keywords='codepen api wrapper python python-codepen',
    url='https://github.com/connorkendrick/python-codepen',
    packages=['codepen'],
    install_requires=['requests'],
    tests_require=['pytest', 'vcrpy'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        ],
)
