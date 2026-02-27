def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for _ in range(order):
        for i in range(len(series) - 1):
            series[i] = series[i + 1] - series[i]
        series = series[:len(series) - 1]
    return series