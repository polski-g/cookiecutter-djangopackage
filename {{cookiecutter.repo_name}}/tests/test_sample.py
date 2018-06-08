#!/usr/bin/env python

from django.test import TestCase

from {{ cookiecutter.app_name }} import models


class Test{{ cookiecutter.app_name|capitalize }}(TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass
