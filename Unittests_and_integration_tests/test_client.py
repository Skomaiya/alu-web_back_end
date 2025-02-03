#!/usr/bin/env python3
""" Unittest Test client
"""
import unittest
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    ''' self descriptive '''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
