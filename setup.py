from setuptools import setup

# python3 setup.py sdist bdist_wheel

setup(
    name='credible_intervals',
    version='1.0',
    packages=['credible_intervals'],
    url='',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'typing',
    ],
    author='FabianKP',
    author_email='',
    description='A program for computing simultaneous credible intervals from samples'
)
