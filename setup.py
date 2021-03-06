from setuptools import setup

# import `__version__` from code base
exec(open('edward/version.py').read())

setup(
    name='edward',
    version=__version__,
    description='A library for probabilistic modeling, inference, and '
                'criticism',
    author='Dustin Tran',
    author_email="dustin@cs.columbia.edu",
    packages=['edward', 'edward.stats', 'edward.models'],
    install_requires=['tensorflow>=0.9.0',
                      'numpy>=1.7',
                      'scipy>=0.16',
                      'six>=1.10.0'],
    extras_require={'stan': ['pystan>=2.0.1.3'],
                    'pymc3': ['pymc3>=3.0'],
                    'neural networks': ['keras>=1.0.0', 'prettytensor>=0.5.3'],
                    'visualization': ['progressbar>=2.0']},
    url='https://github.com/blei-lab/edward',
    license='Apache License 2.0',
    classifiers=['License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4'],
)
