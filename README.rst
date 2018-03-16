.. image:: https://travis-ci.org/scivision/scanning-doppler-interferometer.svg?branch=master
    :target: https://travis-ci.org/scivision/scanning-doppler-interferometer
    
.. image:: https://ci.appveyor.com/api/projects/status/1a1ujuhlupob96m9?svg=true
    :target: https://ci.appveyor.com/project/scivision/scanning-doppler-interferometer

===============================
scanning-doppler-interferometer
===============================
Get, Parse, Plot: Scanning Doppler Interferomter data from PI Mark Conde's instruments.


.. image:: data/winds_sdi_python.png
   :alt: SDI wind line plot
   
   
Install
=======
::

    pip install -e .
    
    
Self-test::

    pytest -v
    
    
    
Usage
=====
::

    ./PlotWinds.py data/PKR_2017_061_date_03_02_sky_5577_nz0115.txt
