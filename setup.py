from setuptools import setup
import io

from setuptools.extension import Extension

try:
    import Cython
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'
extensions = [
    Extension('jsonobject', ["jsonobject/*.pyx"],),
    Extension('jsonobject.api', ["jsonobject/api.pyx"],),
    Extension('jsonobject.base', ["jsonobject/base.pyx"],),
    Extension('jsonobject.base_properties', ["jsonobject/base_properties.pyx"],),
    Extension('jsonobject.containers', ["jsonobject/containers.pyx"],),
    Extension('jsonobject.exceptions', ["jsonobject/exceptions.pyx"],),
    Extension('jsonobject.properties', ["jsonobject/properties.pyx"],),
    Extension('jsonobject.utils', ["jsonobject/utils.pyx"],),
]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)


with io.open('README.md', 'rt', encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='jsonobject',
    version='0.8.0',
    author='Danny Roberts',
    author_email='droberts@dimagi.com',
    description='A library for dealing with JSON as python objects',
    long_description=long_description,
    url='https://github.com/dannyroberts/jsonobject',
    packages=['jsonobject'],
    install_requires=[
        'six',
        'cython'
    ],
    tests_require=['unittest2'],
    ext_modules=extensions,
    test_suite='test',
)
