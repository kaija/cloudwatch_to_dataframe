#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudwatch-to-dataframe.
# https://github.com/kaija/cloudwatch_to_dataframe

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2020, kaija <kaija.chang@gmail.com>

from preggy import expect

from cloudwatch_to_dataframe import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
