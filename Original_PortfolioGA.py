from random import random, randint
import datetime
import time
import copy

from Formulas import get_expected_total
from asserts import multi_object_function_to_minimize, Asset

portfolio = [Asset(returns=[0.0874, 0.0952, 0.5843, -0.0568, 0.4661]),
             Asset(returns=[-0.4622, 0.4106, 0.3896, 0.0935, -0.0702]),
             Asset(returns=[0.1282, 0.0709, 0.524, 0.2227, 0.3001]),
             Asset(returns=[0.2359, 0.1590, 0.2213, 0.0170, 0.0363]),
             Asset(returns=[-0.0208, 0.1720, 0.3384, -0.0985, 0.2387]), ]

mean_returns = [0.2352, 0.0722, 0.2491, 0.1339, 0.1259]

def get_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st


def get_distribution(number_weights):
    while True:
        weights = []
        for i in range(number_weights-1):
            weight = random()
            weights.append(weight)
        last_weight = 1 - sum(weights)
        distribution = [last_weight]+weights
        if last_weight < 0:
            pass
        else:
            return distribution


def get_distribution_objective(distributions):
    values = []
    for i in range(len(distributions)):
        distribution = distributions[i]
        objectvalue = multi_object_function_to_minimize(distribution, portfolio)
        distribution_objective = {}
        distribution_objective['distribution'] = distribution
        distribution_objective['objective'] = objectvalue
        values.append(distribution_objective)
    new_distribution_objectives = sorted(values, key=lambda x: x['objective'])
    return new_distribution_objectives

def create_parents(number_parents):
    distributions = []
    for i in range(number_parents):
        distribution = get_distribution(5)
        distributions.append(distribution)
    new_distribution_objectives = get_distribution_objective(distributions)
    return new_distribution_objectives


def crossover(distribution1, distribution2):
    child = []
    for i in range(len(distribution1)):
        child.append((distribution1[i] + distribution2[i]) / 2)
    return child

def evolution(parents, number_children):
    children = []
    for i in range(number_children):
        index = randint(0, len(parents) - 1)
        index2 = randint(0, len(parents) - 1)
        parent1 = parents[index]['distribution']
        parent2 = parents[index2]['distribution']
        child = crossover(parent1, parent2)
        children.append(child)
    children = get_distribution_objective(children)
    return children


def get_golden_child(parents, generations=20):
    evolution_set = copy.deepcopy(parents)
    print "Evolve = " + get_time()
    while generations > 0:
        evolution_set = sorted(evolution_set, key=lambda x: x['objective'], reverse=True)[:len(evolution_set)/2]
        print get_expected_total(evolution_set[0]['distribution'], mean_returns), evolution_set[0]
        print get_expected_total(evolution_set[len(evolution_set)/2]['distribution'], mean_returns), evolution_set[len(evolution_set)/2]
        print get_expected_total(evolution_set[-1]['distribution'], mean_returns), evolution_set[-1]
        children = evolution(evolution_set, len(evolution_set))
        evolution_set = children+evolution_set
        generations = generations - 1
        print str(len(evolution_set)) + ' = ' + get_time()

    return evolution_set[0]


def test(number_parents):
    print "Start = " + get_time()
    parents = create_parents(number_parents)
    child = get_golden_child(parents, 10)


if __name__ == '__main__':
    test(100000)









