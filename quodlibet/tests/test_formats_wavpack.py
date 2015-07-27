# -*- coding: utf-8 -*-
# Copyright 2015 Christoph Reiter
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

import os

from tests import TestCase, DATA_DIR
from quodlibet.formats.wavpack import WavpackFile


class TWavpackFile(TestCase):

    def setUp(self):
        self.song = WavpackFile(os.path.join(DATA_DIR, 'silence-44-s.wv'))

    def test_length(self):
        self.assertAlmostEqual(self.song("~#length"), 3.68471, 3)

    def test_bitrate(self):
        self.failUnlessEqual(self.song("~#bitrate"), 76)