import numpy


class Asset(object):
    def __init__(self, returns):
        assert isinstance(returns, list)
        self.returns = returns

    def r(self):
        """ Expected return for this asset"""
        return sum(self.returns)


def expected_return(w, r):
    """ the total expected return of portfolio

    :param w: (list) the weights of the individual asserts
    :param r: (list) the expected return for every assert
    :return:
    """
    assert(len(w) == len(r))
    expected_return = 0
    for i in range(0, len(w)):
        expected_return = expected_return + w[i] * r[i]
    return expected_return


def objective_function_of_the_porfolio_variance(w, assets):
    """
    :param w: (list) the weights of the individual asserts
    :param assets: list of assets
    :return:
    """
    portfolio_variance = 0
    for i in range(0, len(w)):
        portfolio_variance += w[i]*w[i]*numpy.std(assets[i].returns)
    # Dhttp://stackoverflow.com/questions/15317822/calculating-covariance-with-python-and-numpy
    covariance = 0
    for i in range(0, len(assets)):
        for j in range(i+1, len(assets)):

            covariance += 2 * w[i] * w[j] * numpy.cov(assets[i].returns, assets[j].returns)[0][1]
    # print("Variance: ", portfolio_variance)
    # print("Covariance: ", covariance)
    return portfolio_variance + covariance


def multi_object_function_to_minimize(w, assets):
    portfolio_variance = objective_function_of_the_porfolio_variance(w, assets)
    asset_returns = [asset.r() for asset in assets]
    return expected_return(w, asset_returns) - portfolio_variance


if __name__ == '__main__':
    portfolio = [Asset(returns=[0.1, -0.1, 0.1]),
                 Asset(returns=[-0.2, 0, 0.8]),]
    print portfolio[0].r()
    print portfolio[1].r()
    print(multi_object_function_to_minimize([0.9, 0.1], portfolio))
    print(multi_object_function_to_minimize([0.5, 0.5], portfolio))
    print(multi_object_function_to_minimize([0.1, 0.9], portfolio))

    portfolio = [Asset(returns=[0.1, -0.1, 0.1]),
                 Asset(returns=[-0.2, 0, 0.8]),
                 Asset(returns=[0.25, 0.10, -0.05]), ]
    print portfolio[0].r()
    print portfolio[1].r()
    print(multi_object_function_to_minimize([0.9, 0.1, 0.0], portfolio))
    print(multi_object_function_to_minimize([0.33, 0.33, 0.33], portfolio))
    print(multi_object_function_to_minimize([0.1, 0.5, 0.1], portfolio))
    print(multi_object_function_to_minimize([0.1, 0.1, 0.5], portfolio))
