def rabbit_population(n,k):
    population = [1, 1] # INITIAL POPULATION (in pairs)
    for i in range(n-2): 
        next_month_population = population[-1] + population[-2]*k
        population.append(next_month_population)
    return f"Total: {population[-1]}\nReproducible: {population[-2]}\nNewborn: {population[-1] - population[-2]}"

if  __name__ == '__main__':
    print(rabbit_population(5, 3))
