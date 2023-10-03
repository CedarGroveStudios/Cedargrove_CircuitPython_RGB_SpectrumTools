# SPDX-FileCopyrightText: Copyright (c) 2023 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`cedargrove_rgb_spectrumtools.two_color_blender`
================================================================================

An Two-Color Spectrum Index to RGB Converter Class
with an Exposed Reference Spectrum List Property

* Author(s): JG

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_RGB_SpectrumTools.git"


def map_range(x, in_min, in_max, out_min, out_max):
    # pylint: disable = duplicate-code
    """Maps and constrains an input value from one range of values to another.
    (from adafruit_simpleio)

    :param float x: The value to be mapped. No default.
    :param float in_min: The beginning of the input range. No default.
    :param float in_max: The end of the input range. No default.
    :param float out_min: The beginning of the output range. No default.
    :param float out_max: The end of the output range. No default.

    :return: Returns value mapped to new range
    :rtype: float
    """
    in_range = in_max - in_min
    in_delta = x - in_min
    if in_range != 0:
        mapped = in_delta / in_range
    elif in_delta != 0:
        mapped = in_delta
    else:
        mapped = 0.5
    mapped *= out_max - out_min
    mapped += out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)


class Blender:
    """Converts a spectrum index value consisting of a positive numeric value
    (0.0 to 1.0, modulus of 1.0) to an RGB color value that representing the
    index position on a blended two-color spectrum.

    The spectrum is defined by a list of colors that fall at the start and end
    of the spectrum. The starting and/or ending color values are allowed to
    change after the class is instantiated.

    A `gamma` value in the range of 0.0 to 3.0 will help to smooth the visual
    transition between colors. A value of 0.55 works well with TFT displays.

    :param int start_color: A 24-bit color values representing the first
        color of the spectrum. Defaults to black (0x000000).
    :param int end_color: A 24-bit color values representing the last color
        of the spectrum. Defaults to white (0xFFFFFF).
    :param float gamma: A positive float value to adjust color intensity for
        human eye perception. Accepts a range of values between 0.0 and 3.0.
        Defaults to 1.0 (no gamma adjustment).
    """

    def __init__(self, start_color=0x000000, end_color=0xFFFFFF, gamma=1):
        self._start_color = start_color
        self._end_color = end_color
        self._gamma = min(max(gamma, 0), 3.0)
        self._index_granularity = (2**16) - 1  # maximum index granularity
        self._index = 0  # set to default startup value

    @property
    def start_color(self):
        """The starting color of the spectrum."""
        return self._start_color

    @start_color.setter
    def start_color(self, new_start_color=0x000000):
        """The starting color of the spectrum.
        :param int new_start_color: A 24-bit color values representing the first
        color of the spectrum. Defaults to black (0x000000)."""
        self._start_color = new_start_color

    @property
    def end_color(self):
        """The last color of the spectrum."""
        return self._end_color

    @end_color.setter
    def end_color(self, new_end_color=0xFFFFFF):
        """The last color of the spectrum.
        :param int new_end_color: A 24-bit color values representing the last color
        of the spectrum. Defaults to white (0xFFFFFF)."""
        self._end_color = new_end_color

    @property
    def gamma(self):
        """Color intensity factor for human eye perception. Accepts a range of
        values between 0.0 and 3.0."""
        return self._gamma

    @gamma.setter
    def gamma(self, new_gamma=1.0):
        """Color intensity factor for human eye perception.
        :param float new_gamma: A positive float value to adjust color intensity for
        human eye perception. Accepts a range of values between 0.0 and 3.0.
        Defaults to 1.0 (no gamma adjustment)."""
        self._gamma = min(max(new_gamma, 0), 3.0)

    def color(self, index=0):
        """Converts a spectrum index value to an RGB color value.
        :param float index: The spectrum index. Ranges between 0.0 (starting
        color) and 1.0 (ending color).
        :return: Returns a 24-bit RGB integer value representing the color
        in the spectrum at the index.
        :rtype: integer
        """

        self._index = (
            (abs(index) * self._index_granularity) % self._index_granularity
        ) / self._index_granularity

        start_red = ((self._start_color >> 16) & 0xFF) / 0xFF
        start_grn = ((self._start_color >> 8) & 0xFF) / 0xFF
        start_blu = ((self._start_color >> 0) & 0xFF) / 0xFF

        end_red = ((self._end_color >> 16) & 0xFF) / 0xFF
        end_grn = ((self._end_color >> 8) & 0xFF) / 0xFF
        end_blu = ((self._end_color >> 0) & 0xFF) / 0xFF

        red = map_range(self._index, 0, 1.0, start_red, end_red)
        grn = map_range(self._index, 0, 1.0, start_grn, end_grn)
        blu = map_range(self._index, 0, 1.0, start_blu, end_blu)

        red = int(round((red**self._gamma) * 0xFF, 0))
        grn = int(round((grn**self._gamma) * 0xFF, 0))
        blu = int(round((blu**self._gamma) * 0xFF, 0))

        return (int(red) << 16) + (int(grn) << 8) + int(blu)
