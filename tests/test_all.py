#!/usr/bin/env python
import pytest
import pandas
from pathlib import Path
import scanning_doppler_interferometer as sdi

R = Path(__file__).resolve().parents[1] / 'data'
txtfn = R / 'PKR_2017_061_date_03_02_sky_5577_nz0115.txt'


def test_txtload():

    dat = sdi.txt2dat(txtfn)

    assert isinstance(dat, pandas.DataFrame)


if __name__ == '__main__':
    pytest.main(['-x', __file__])
