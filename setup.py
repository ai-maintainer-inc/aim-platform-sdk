# coding: utf-8

"""
    Marketplace API

    An API for the AI Maintainer Marketplace  # noqa: E501

    The version of the aim_platform_sdk document: 0.1.6
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "aim_platform_sdk"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions >= 4.3.0",
    "urllib3 >= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="Agent Marketplace API Client",
    author="AI Maintainer Inc",
    author_email="douglas@ai-maintainer.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Marketplace API"],
    python_requires=">=3.8",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    An API client for the AI Maintainer Marketplace  # noqa: E501
    """,
)
