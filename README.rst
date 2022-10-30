Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_RGB_SpectrumTools/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_RGB_SpectrumTools/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A collection of methods and classes for converting a normalized index to RGB
color values. Included in the collection are spectral conversion methods for
grayscale, iron temperature color, stoplight (green-yellow-red), and visible
light as well as classes for n-color blended light.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_rgb_spectrumtools

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

``grayscale(index, gamma)``

Translates the normalized index value into a 24-bit RGB integer with gamma
adjustment. The spectral index is a floating point value in the range of 0.0 to
1.0 (inclusive); default is 0.0. The gamma value can be from 0.0 to 1.0
(inclusive); default is 0.8, tuned for TFT displays. If the index or gamma
value is outside of the specified range, the 24-bit RGB output will be limited
to the minimum (0x0) or maximum (0xFFFFFF) value.

.. code-block:: python

    >>> from cedargrove_rgb_spectrumtools.grayscale import index_to_rgb
    >>> hex(index_to_rgb(0.5, 1.0))
    '0x8c8c8c'

``iron(index, gamma)``

Translates the normalized index value into a 24-bit RGB integer with gamma
adjustment. The spectral index is a floating point value in the range of 0.0 to
1.0 (inclusive); default is 0.0. The gamma value can be from 0.0 to 1.0
(inclusive); default is 0.5, tuned for TFT displays. If the index or gamma
value is outside of the specified range, the 24-bit RGB output will be limited
to the minimum (0x0) or maximum (0xFFFFFF) value.

.. code-block:: python

    >>> from cedargrove_rgb_spectrumtools.iron import index_to_rgb
    >>> hex(index_to_rgb(0.5, 1.0))
    '0xff0000'

``stoplight(index, gamma)``

Translates the normalized index value into a 24-bit RGB integer with gamma
adjustment. The spectral index is a floating point value in the range of 0.0 to
1.0 (inclusive); default is 0.0. The gamma value can be from 0.0 to 1.0
(inclusive); default is 0.5, tuned for TFT displays. If the index or gamma
value is outside of the specified range, the 24-bit RGB output will be limited
to the minimum (0x0) or maximum (0xFFFFFF) value.

.. code-block:: python

    >>> from cedargrove_rgb_spectrumtools.stoplight import index_to_rgb
    >>> hex(index_to_rgb(0.5, 1.0))
    ‘'0xffff00'

``visible(index, gamma)``

Translates the normalized index value into a 24-bit RGB integer with gamma
adjustment. The spectral index is a floating point value in the range of 0.0 to
1.0 (inclusive); default is 0.0. The gamma value can be from 0.0 to 1.0
(inclusive); default is 0.5, tuned for TFT displays. If the index or gamma
value is outside of the specified range, the 24-bit RGB output will be limited
to the minimum (0x0) or maximum (0xFFFFFF) value.

.. code-block:: python

    >>> from cedargrove_rgb_spectrumtools.visible import index_to_rgb
    >>> hex(index_to_rgb(0.5, 1.0))
    '0x6dff00'

``n_color(index, gamma)``

A class that translates the normalized index value into a 24-bit RGB integer
with gamma adjustment. The spectral index is a floating point value in the
range of 0.0 to 1.0 (inclusive); default is 0.0. The gamma value can be from
0.0 to 3.0 (inclusive); default is 0.55, tuned for TFT displays. If the index
or gamma value is outside of the specified range, the 24-bit RGB output will be
limited to the minimum (0x0) or maximum (0xFFFFFF) value.

The class converts a spectrum index value consisting of a positive numeric
value (0.0 to 1.0, modulus of 1.0) to an RGB color value that representing the
index position on a graduated and blended multicolor spectrum. The spectrum is
defined by a list of colors that are proportionally distributed across the spectrum.
Two spectrum modes are currently supported:

* "light" mode produces a blended color spectrum that mimics a typical wavelength-of-light representation. The spectrum does not wrap; the first and last colors are not blended with each other.

* "continuous" mode blends the color list's first color and last color at the start and end, creating a continuously blended spectrum. This is the default mode.

This class calculates resultant color values on-the-fly to reduce memory
consumption with a slight speed performance sacrifice. Use the
``n-color_table.Spectrum`` class to improve performance.

.. code-block:: python

    >>> from cedargrove_rgb_spectrumtools.n_color import Spectrum
    >>> # Create Red/Yellow/Green light-style spectrum
    >>> spectrum = Spectrum([0xFF0000, 0xFFFF00, 0x00FF00], mode="light", gamma=0.6)
    >>> print(hex(spectrum.color(index=0.36)))
    0xff9c00

``n_color(index, gamma)``

This class functions the same as the ``n_color.Spectrum`` class, calculating
resultant color values from a pre-compiled internal color list to improve speed
performance but with increased memory usage. Use the
``n-color_spectrum.Spectrum`` class to reduce memory usage.

.. code-block:: python

    >>> from cedargrove_rgb_spectrumtools.n_color_table import Spectrum
    >>> # Create Red/Yellow/Green light-style spectrum
    >>> spectrum = Spectrum([0xFF0000, 0xFFFF00, 0x00FF00], mode="light", gamma=0.6)
    >>> print(hex(spectrum.color(index=0.36)))
        0xff9c00

Documentation
=============
API documentation for this library can be found `here <https://github.com/CedarGroveStudios/CircuitPython_RGB_SpectrumTools/blob/main/media/pseudo_rtd_cedargrove_rgb_spectrumtools.pdf>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/CircuitPython_RGB_SpectrumTools/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
