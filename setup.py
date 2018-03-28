#!/usr/bin/env python

from setuptools import setup


SETUP_REQUIRES = [
    "setuptools>=36",
    "pytest-runner",
]


TESTS_REQUIRE = [
    "pytest>=3.1.0",
    "pytest-cov",
    "colorlog",
    "mock",
    "pytest-remove-stale-bytecode",
]


setup(
    name="tavern_flask",

    setup_requires=SETUP_REQUIRES,

    tests_require=TESTS_REQUIRE,
    extras_require={
        "tests": TESTS_REQUIRE
    }
)
