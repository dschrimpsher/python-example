from setuptools import setup

setup(
    name='python-example',
    version='0.1a',
    packages=['python_example'],
    url='http://github.com/dschrimpsher/python-example',
    license='Apache 2.0',
    author='Dan Schrimpsher',
    author_email='d.schrimpsher@cablelabs.com',
    description='Example Python Project',
    install_requires=['request', 'requests-html'],
)
