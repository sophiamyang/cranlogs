.. highlight:: shell

============
cran_downloads
============

.. ipython:: python

   import cranlogs 

Examples
---------------

To get daily downloads for package ggplot2 from 2019-08-01 to 2019-08-03, we need to define
the packages as ggplot2, start time as 2019-08-01, and the end time as 2019-08-03.

.. ipython:: python

   cranlogs.cran_downloads(packages='ggplot2', start='2019-08-01', end='2019-08-03')

We can also get the package downloads for last day, last week, and last month by defining 
when='last-day', when='last-week', or when='last-month'. 

.. ipython:: python

   cranlogs.cran_downloads(packages='ggplot2', when='last-day')

In fact, if no timing information is defined, the default will be 'last-day'.

.. ipython:: python

   cranlogs.cran_downloads(packages='ggplot2')

We can get data for multiple packages.

.. ipython:: python

   cranlogs.cran_downloads(packages=['ggplot2','dplyr'], start='2019-08-01', end='2019-08-03' )

And we can get data for R installers downloads. 

.. ipython:: python

   cranlogs.cran_downloads(packages=['R'], when='last-week' )
