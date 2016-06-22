from random import randint

femalenames = ['Marcy', 'Karla', 'Hannah', 'Natalie', 'Emily', 'April', 'Hunter', 'Riley', 'Eva', 'Carla', 'Valerie',
               'Alexis', 'Sophie', 'Bridget', 'Diana', 'Sara', 'Stacey', 'Blake', 'Alex', 'Katy', 'Katelyn', 'Nicole',
               'Brenda', 'Paola', 'Carol', 'Caitlin', 'Veronica', 'Alexandra', 'Gabriela', 'Danielle', 'Gabrielle',
               'Isabel', 'Madison', 'Bella', 'Stephanie', 'Paula', 'Andrea', 'Jacky', 'Andrea', 'Donna', 'Antonia',
               'Georgia', 'Andy', 'Susan', 'Linda', 'Dorothy', 'Elizabeth', 'Gracie', 'Sheila', 'Barbara', 'Lisa',
               'Ivy']
malenames = ['John', 'Hector', 'Alex', 'Caleb', 'Paul', 'Chris', 'Joshua', 'Anthony', 'George', 'Charles', 'Edward',
             'Hunter', 'Riley', 'Brandon', 'Nathan', 'Brad', 'Mark', 'Carlos', 'Alexis', 'Jason', 'Kevin',
             'Matthew', 'Donald', 'Stephen', 'James', 'Michael', 'Blake', 'Brian', 'Brett', 'Steven', 'Enrique',
             'Travis', 'Joseph', 'Andrew', 'Khalil', 'Dean', 'Carl', 'Don', 'Peter', 'George', 'Gerald', 'Joe',
             'Robert', 'Andy', 'Tom', 'Thomas', 'Alexander', 'Walter', 'Franklin', 'Tyler', 'Gael', 'Max',
             'Ryan', 'Luke', 'Jake', 'Jimmy']
genders = ['male', 'female', '']
languages = ['english', 'spanish', 'french', 'other']
lastnames = ['Jones', 'Gardner', 'Hall', 'Phillips', 'Johnson', 'Reynolds', 'Evans', 'Brooks', 'Scott', 'Young',
             'Smith', 'Wilson', 'Davis', 'Miller', 'Thompson', 'Moore', 'Dotts', 'Anthony', 'Anderson', 'Taylor',
             'Brown', 'Martin', 'Harris', 'White', 'Jackson', 'Walker', 'Lee', 'Lewis', 'Casey', 'Swift', 'Adams',
             'Walker', 'Carter', 'Clark', 'Dick', 'Howard', 'Curry', 'Douglas', 'Marshall', 'Hodge', 'Walter',
             'Franklin', 'Western', 'Tyler', 'Butler', 'Lopez', 'Wang', 'Thomas', 'OBrien', 'Collins', 'Morrow',
             'Walsh']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
         'November', 'December']
ethnicities = ['African_American', 'Hispanic', 'White', 'Other']

def individual():
    index = randint(0, 2)
    gender = genders[index]
    index = randint(0, 3)
    language = languages[index]
    names = femalenames + malenames
    index = randint(0, len(names) - 1)
    name = names[index]
    index = randint(0, len(lastnames) - 1)
    lastname = lastnames[index]
    year = randint(1950,1997)
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    index = randint(0, len(months) - 1)
    month = months[index]
    day = randint(1,31)
    ethnicity = ['African_American', 'Hispanic', 'White', 'Other']
    index = randint(0, len(ethnicities) - 1)
    ethnicity = ethnicities[index]

    return {
    'name' : name,
    'lastname' : lastname,
    'language' : language,
    'gender' : gender,
    'year' : year,
    'month' : month,
    'day' : day,
    'ethnicity' : ethnicity
}

def population(count):
    return [individual() for x in xrange(count)]

def fitness(individual):
    value = 0
    if individual['gender'] == 'male':
        if individual['name'] in malenames:
            value = 1
    elif individual['gender'] == 'female':
        if individual['name'] in femalenames:
            value = 1
    else:
        value = 0
    if individual['ethnicity'] == 'African_American':
        if individual['language'] == 'english' or individual['language'] == 'french' or individual['language'] == 'other':
            return value + 1
    elif individual['ethnicity'] == 'White':
        if individual['language'] == 'english' or individual['language'] == 'french' or individual['language'] == 'other':
            return value + 1
    elif individual['ethnicity'] == 'Hispanic':
        if individual['language'] == 'spanish':
            return value + 1
    else:
        return value + 1
    return value

person = individual()

pop = population(5000)
print pop
def grade(pop):
    sum = 0.0
    for individual in pop:
        sum = sum + fitness(individual)
    return sum /len(pop)
print grade(pop)

def get_fitness(individual):
    return individual['fitness']

def evolve(population):
    for individual in population:
        individual['fitness'] = fitness(individual)
    new_population = sorted(population, key=get_fitness)
    new_population = new_population[4500:]
    children = []
    for i in xrange(0, 5000):
        index = randint(0, (len(new_population)) - 1)
        index2 = randint(0, (len(new_population)) - 1)
        parent1 = new_population[index]
        parent2 = new_population[index2]
        child = {}
        child['name'] = parent1['name']
        child['gender'] = parent1['gender']
        child['day'] = parent1['day']
        child['month'] = parent1['month']
        child['lastname'] = parent2['lastname']
        child['ethnicity'] = parent2['ethnicity']
        child['language'] = parent2['language']
        child['year'] = parent2['year']
        children.append(child)
    return children
print evolve(pop)


from random import random, randint
def mutate(new_population):
    chance_to_mutate = 0.1
    for i in new_population:
        if chance_to_mutate > random():
            index = randint(0, 2)
            gender = genders[index]
            i['gender'] = gender
            index = randint(0, 3)
            language = languages[index]
            i['language'] = language
            names = femalenames + malenames
            index = randint(0, len(names) - 1)
            name = names[index]
            i['name'] = name
            index = randint(0, len(lastnames) - 1)
            lastname = lastnames[index]
            i['lastname'] = lastname
            index = randint(0, len(months) - 1)
            month = months[index]
            i['month'] = month
            index = randint(0, len(ethnicities) - 1)
            ethnicity = ethnicities[index]
            i['ethnicity'] = ethnicity

    return new_population

print grade(evolve(pop))
print grade(mutate(evolve(pop)))

print mutate(evolve(pop))

population = mutate(evolve(pop))

def individuals(population, gender):
    count = 0
    for i in xrange(0, 5000):
        if population[i]['gender'] == gender:
            count = count + 1
    return count
print individuals(population, 'male')
print individuals(population, 'female')
print individuals(population, '')


def ethnicities(population, ethnicity):
    count = 0
    for i in xrange(0, 5000):
        if population[i]['ethnicity'] == ethnicity:
            count = count + 1
    return count
print ethnicities(population, 'Hispanic')
print ethnicities(population, 'White')
print ethnicities(population, 'African_American')
print ethnicities(population, 'Other')


def language(population, language):
    count = 0
    for i in xrange(0, 5000):
        if population[i]['language'] == language:
            count = count + 1
    return count
print language(population, 'spanish')
print language(population, 'english')
print language(population, 'french')
print language(population, 'other')

import csv
with open('data.csv', 'w') as csvfile:
    fieldnames = ['name', 'lastname', 'gender', 'ethnicity', 'language', 'month', 'day', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow(dict(zip(fieldnames,fieldnames)))
    writer.writerow({'name': 'Alex', 'lastname': 'Evans', 'gender': 'male', 'ethnicity': 'White', 'language': 'other',
                     'month': 'January', 'day': '25', 'year': '1988'})
