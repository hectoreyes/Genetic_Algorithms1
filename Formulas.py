def get_expected_total(distribution, returns):
    expected_values = []
    for i in range(len(distribution)):
        expected_value = distribution[i] * returns[i]
        expected_values.append(expected_value)
    return sum(expected_values)

def get_max_expected_total(distributions, returns):
    expected_totals = []
    for i in range(len(distributions)):
        distribution = distributions[i]
        expected_total = get_expected_total(distribution, returns)
        expected_totals.append(expected_total)
    return max(expected_totals)







