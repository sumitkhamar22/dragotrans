Dragotrans
===========



Dragotrans is a **free** and **unlimited** python library that
will recognize and translate language from the text. 

Compatible with Python 3.6+.

.

Features
--------

-  Fast and reliable 
   translate.google.com uses
-  Auto language detection
-  Bulk translations
-  Customizable service URL
-  HTTP/2 support

TODO
~~~~

more features are coming soon.

-  Proxy support
-  Internal session management (for better bulk translations)

HTTP/2 support
~~~~~~~~~~~~~~

This library uses httpx for HTTP requests so HTTP/2 is supported by default.




--------------

Installation
------------

To install, either use things like pip with the package "dragotrans"
or download the package and put the "dragotrans" directory into your
python path.

.. code:: bash

    $ pip install dragotrans

Basic Usage
-----------

If source language is not given, this library translate attempts to detect the
source language.

.. code:: python

    >>> from dragotrans import Translator
    >>> translator = Translator()
    >>> translator.translate('안녕하세요.')
    # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
    >>> translator.translate('안녕하세요.', dest='ja')
    # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
    >>> translator.translate('veritas lux mea', src='la')
    # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>


Advanced Usage (Bulk)
~~~~~~~~~~~~~~~~~~~~~

Array can be used to translate a batch of strings in a single method
call and a single HTTP session. The exact same method shown above works
for arrays as well.

.. code:: python

    >>> translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
    >>> for translation in translations:
    ...    print(translation.origin, ' -> ', translation.text)
    # The quick brown fox  ->  빠른 갈색 여우
    # jumps over  ->  이상 점프
    # the lazy dog  ->  게으른 개

Language detection
~~~~~~~~~~~~~~~~~~

The detect method, as its name implies, identifies the language used in
a given sentence.

.. code:: python

    >>> from dragotrans import Translator
    >>> translator = Translator()
    >>> translator.detect('이 문장은 한글로 쓰여졌습니다.')
    # <Detected lang=ko confidence=0.27041003>
    >>> translator.detect('この文章は日本語で書かれました。')
    # <Detected lang=ja confidence=0.64889508>
    >>> translator.detect('This sentence is written in English.')
    # <Detected lang=en confidence=0.22348526>
    >>> translator.detect('Tiu frazo estas skribita en Esperanto.')
    # <Detected lang=eo confidence=0.10538048>

DragoTrans as a command line application
-----------------------------------------

.. code:: bash

    $ translate -h
    usage: translate [-h] [-d DEST] [-s SRC] [-c] text

    Python Google Translator as a command-line tool

    positional arguments:
      text                  The text you want to translate.

    optional arguments:
      -h, --help            show this help message and exit
      -d DEST, --dest DEST  The destination language you want to translate.
                            (Default: en)
      -s SRC, --src SRC     The source language you want to translate. (Default:
                            auto)
      -c, --detect

    $ translate "veritas lux mea" -s la -d en
    [veritas] veritas lux mea
        ->
    [en] The truth is my light
    [pron.] The truth is my light

    $ translate -c "안녕하세요."
    [ko, 1] 안녕하세요.

--------------

Note on library usage
---------------------



Contributing
-------------------------

Contributions are more than welcomed. See  
`CONTRIBUTING.md <CONTRIBUTING.md>`__

-----------------------------------------

License
-------

Dragotrans is licensed under the MIT License. The terms are as
follows:

::

    The MIT License (MIT)

    Copyright (c) 2015 SuHun Han

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


