.. highlight:: shell

============
cran_downloads
============

.. ipython:: python

   from cranlogs import cran_downloads 

Parameters:

- packages: a string representing one package, or a list of multiple packages.
- when: "last-day", "last-week", or "last-month". When defined, start and end will be ignored.
- start: start date with format year-month-day.
- start: end date with format year-month-day.

Examples
---------------

To get daily downloads for package ggplot2 from 2019-08-01 to 2019-08-03, we need to define
the packages as ggplot2, start time as 2019-08-01, and the end time as 2019-08-03.

.. ipython:: python

   cran_downloads(packages='ggplot2', start='2019-08-01', end='2019-08-03')

We can also get the package downloads for last day, last week, and last month by defining 
when='last-day', when='last-week', or when='last-month'. 

.. ipython:: python

   cran_downloads(packages='ggplot2', when='last-day')

In fact, if no timing information is defined, the default will be 'last-day'.

.. ipython:: python

   cran_downloads(packages='ggplot2')

We can get data for multiple packages.

.. ipython:: python

   cran_downloads(packages=['ggplot2','dplyr'], start='2019-08-01', end='2019-08-03' )

And we can get data for R installers downloads. 

.. ipython:: python

   cran_downloads(packages=['R'], when='last-week' )
