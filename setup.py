import os
import sys

import setuptools
from setuptools.command.install import install

VERSION = "1.0"

def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setuptools.setup(
    name="django-nativeshortuuidfield",
    version=VERSION,
    description="A decoder/encoder Field for uuid",
    long_description=readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/foundertherapy/django-nativeshortuuidfield",
    author="Laith Abu Zainih",
    author_email="systems@foundertherapy.co",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords='shortuuid uuid nativeshortuuid',
    packages=setuptools.find_packages(),
    install_requires=[
        "requests==2.18.4",
        "django>=1.11",
        "django-shortuuidfield"
    ],
    python_requires='>=3',
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)