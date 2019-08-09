from cranlogs import cran_downloads
import pandas as pd

def test_simple():
    df = cran_downloads('ggplot2')
    assert len(df) == 1

