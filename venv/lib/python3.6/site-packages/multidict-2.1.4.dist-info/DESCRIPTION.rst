=========
multidict
=========

Multidicts are useful for working with HTTP headers, URL
query args etc.

The code was extracted from aiohttp_ library.

Introduction
------------

*HTTP Headers* and *URL query string* require specific data structure:
*multidict*. It behaves mostly like a regular ``dict`` but it may have
several *values* for the same *key*.

``multidict`` has four multidict classes:
``MultiDict``, ``MultiDictProxy``, ``CIMultiDict``
and ``CIMultiDictProxy``.

Immutable proxies (``MultiDictProxy`` and
``CIMultiDictProxy``) provide a dynamic view for the
proxied multidict, the view reflects underlying collection changes. They
implement the ``collections.abc.Mapping`` interface.

Regular mutable (``MultiDict`` and ``CIMultiDict``) classes
implement ``collections.abc.MutableMapping`` and allows to change
their own content.


*Case insensitive* (``CIMultiDict`` and
``CIMultiDictProxy``) ones assume the *keys* are case
insensitive, e.g.::

   >>> dct = CIMultiDict(key='val')
   >>> 'Key' in dct
   True
   >>> dct['Key']
   'val'

*Keys* should be ``str`` or ``istr`` instances.

The library has optional Cython_ optimization for sake of speed.


License
-------

Apache 2


.. _aiohttp: https://github.com/KeepSafe/aiohttp
.. _Cython: http://cython.org/

2.1.4 (2016-12-1)
------------------

* Remove LICENSE filename extension @ MANIFEST.in file #31

2.1.3 (2016-11-26)
------------------

* Add a fastpath for multidict extending by multidict


2.1.2 (2016-09-25)
------------------

* Fix `CIMultiDict.update()` for case of accepting `istr`


2.1.1 (2016-09-22)
------------------

* Fix `CIMultiDict` constructor for case of accepting `istr` #11


2.1.0 (2016-09-18)
------------------

* Allow to create proxy from proxy

* Add type hints (PEP-484)


2.0.1 (2016-08-02)
------------------

* Don't crash on `{} - MultiDict().keys()` and similar operations #6


2.0.0 (2016-07-28)
------------------

* Switch from uppercase approach for case-insensitive string to
  `str.title()` #5

* Deprecase `upstr` class in favor of `istr` alias.

1.2.2 (2016-08-02)
------------------

* Don't crash on `{} - MultiDict().keys()` and similar operations #6

1.2.1 (2016-07-21)
------------------

* Don't expose `multidict.__version__`


1.2.0 (2016-07-16)
------------------

* Make `upstr(upstr('abc'))` much faster


1.1.0 (2016-07-06)
------------------

* Don't double-iterate during MultiDict initialization #3

* Fix CIMultiDict.pop: it is case insensitive now #1

* Provide manylinux wheels as well as Windows ones

1.0.3 (2016-03-24)
------------------

* Add missing MANIFEST.in

1.0.2 (2016-03-24)
------------------

* Fix setup build


1.0.0 (2016-02-19)
------------------

* Initial implementation

