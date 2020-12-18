"""
On your terminal run:
pip install alpha_vantage

For the develop version run:
pip install git+https://github.com/RomelTorres/alpha_vantage.git@develop
"""

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt


# Chose your output format, or default to JSON (python dict)
ts = TimeSeries('SD6OYR6MFXCKTNQC', output_format='pandas')
ti = TechIndicators('SD6OYR6MFXCKTNQC')

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
# aapl_sma is a dict, aapl_meta_sma also a dict
aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')


# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
aapl_data['4. close'].plot()
plt.tight_layout()
plt.grid()
plt.show()
