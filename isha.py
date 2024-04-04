from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import numpy as np

# Simulate sales data (assuming this part is necessary for the team's project)
np.random.seed(42)
dates = pd.date_range(start='2019-01-01', end='2021-12-31', freq='M')
trend = np.linspace(100, 300, len(dates))
seasonality = 100 * np.sin(np.linspace(0, 3*np.pi, len(dates)))
noise = np.random.normal(loc=0, scale=20, size=len(dates))
sales = trend + seasonality + noise
sales_data = pd.DataFrame({'Date': dates, 'Sales': sales})
sales_data.set_index('Date', inplace=True)

# Fit an ARIMA model and forecast
model = ARIMA(sales_data['Sales'], order=(5, 1, 0))
model_fit = model.fit()
forecast = model_fit.get_forecast(steps=12)
mean_forecast = forecast.predicted_mean
conf_int = forecast.conf_int()
forecast_dates = pd.date_range(
    start=sales_data.index[-1] + pd.offsets.MonthEnd(1), periods=12, freq='M')

# Plotting the forecast for next 12 months
plt.figure(figsize=(10, 6))
plt.plot(sales_data.index, sales_data['Sales'],
         label='Historical Monthly Sales')
plt.plot(forecast_dates, mean_forecast, color='red', label='Forecasted Sales')
plt.fill_between(
    forecast_dates, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3)
plt.title('Sales Forecast for the Next 12 Months')
