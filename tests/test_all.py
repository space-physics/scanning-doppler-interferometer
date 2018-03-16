#!/usr/bin/env python
import pandas
import scanning_doppler_interferometer as sdi

txtfn = 'data/PKR_2017_061_date_03_02_sky_5577_nz0115.txt'

def test_txtload():

    dat = sdi.txt2dat(txtfn)

    assert isinstance(dat,pandas.DataFrame)