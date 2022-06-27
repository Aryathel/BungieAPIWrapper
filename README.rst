Bungie API Wrapper
==================

A Python wrapper for the `Bungie API <https://bungie-net.github.io/multi/>`_ utilizing
`Pydantic <https://pydantic-docs.helpmanual.io/>`_ for response parsing and
my `API Framework <https://apiframework.readthedocs.io/en/latest/>`_ for making requests.


Note
----
    This is still *very much* a work in progress, I would really recommend not using this in
    its current state. I will eventually release this as a PyPi package, I hope.


Disclaimer
----------
    The Bungie API is *massive*. Because of this, and with the fact that I am currently
    only testing endpoints with my own account, much of the API will not be *fully*
    typed correctly. I can only fix the issues I come across, after all.

    In this regard, if you use this API wrapper and come across any issues with response
    parsing, **please** create an issue and show the errors that you came across. I can
    and will fix any issues I can.
