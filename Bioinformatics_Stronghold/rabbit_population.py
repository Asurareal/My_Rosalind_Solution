def rabbit_population(n,k):
    population = [1, 1] # INITIAL POPULATION (in pairs)
    for i in range(n-2): 
        next_month_population = population[-1] + population[-2]*k
        population.append(next_month_population)
    return population[-1]

if  __name__ == '__main__':
    print(rabbit_population(5, 3))
