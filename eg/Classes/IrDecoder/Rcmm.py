# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2020 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

# Local imports
from eg.Classes.IrDecoder import DecodeError, IrProtocolBase

MODES = {
    1: "Mouse",
    2: "Keyboard",
    3: "Gamepad",
}

class Rcmm(IrProtocolBase):
    def Decode(self, data):
        raise DecodeError("not implemented")

    def GetBits(self):
        if 66 > self.data[self.pos] > 266:
            raise DecodeError("wrong pulse")
        pause = self.data[self.pos + 1]
        self.pos += 2
        if pause < 366:
            return 0  # binary 00
        elif pause < 528:
            return 1  # binary 01
        elif pause < 694:
            return 2  # binary 10
        elif pause < 861:
            return 3  # binary 11
        else:
            raise DecodeError("pause too long")

    def ShiftInBits(self, numBits):
        data = 0
        for _ in xrange(numBits):
            data <<= 2
            data |= self.GetBits()
        return data
