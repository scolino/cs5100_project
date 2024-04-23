"""
The code in this file implements a genetic algorithm used for feature selection within the project. 
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from random import randint

np.random.seed(123)


class GeneticFeatures:
    """
    This class implements a genetic algorithm for feature selection.
    """

    def __init__(self, features, target, population_size, n_parents, model, mutation_rate, n_gen) -> None:
        """
        Initalizes a genetic features algorithm class.

        Parameters:
            features: matrix of predictive features
            target: target response
            population_size: number of possible solutions to generate
            n_parents: 
            model:
            mutation_rate: percent of genes that randomly change
            n_gen: number of generations to iterate through

        """
        self.size = population_size
        self.n_features = features.shape[1]
        self.population = []
        self.model = model
        self.mutation_rate = mutation_rate
        self.n_parents = n_parents
        self.n_gen = n_gen
        self.best_scores = []
        self.best_chromosomes = []
        self.average_score = []
        self.selected_genes = np.zeros(self.n_features)
        
        self.X_tr, self.X_te, self.y_tr, self.y_te = train_test_split(features, target, test_size=0.2, random_state=123)


    def initialize_population(self):
        """
        Initializes a random population by selecting 30 percent of features to be turned off for each chromosome.
        """
        for _ in range(self.size):
            chromosome = np.ones(self.n_features, dtype=bool)     
            chromosome[:int(0.3*self.n_features)]=False             
            np.random.shuffle(chromosome)
            self.population.append(chromosome)
        

    def fitness_score(self):
        scores = []
        for chromosome in self.population:
            # Fit and predict on the given model
            self.model.fit(self.X_tr.iloc[:,chromosome],self.y_tr)         
            predictions = self.model.predict(self.X_te.iloc[:,chromosome])

            # fitness determined my mean square error
            scores.append(mean_squared_error(self.y_te,predictions, squared=False))

        scores, temp_pop = np.array(scores), np.array(self.population) 
        inds = np.argsort(scores) 

        # Population get sorted by fitness scores                                 
        self.fitness_scores, self.population = list(scores[inds]), list(temp_pop[inds,:]) 

        self.best_chromosomes.append(self.population[0])
        self.best_scores.append(self.fitness_scores[0])
        self.average_score.append(sum(self.fitness_scores)/ len(self.fitness_scores))

        # Keep track of seelcted gemes in best chromosomes

    def track_genes(self, chromosome):
        pass


    def selection_crossover(self):
        """
        Creates a new chromosome by selecting half the genes of the first chromosome and half the genes of the second
        chromosome.
        """
        pop_next_gen = []
        parents = self.population[:self.n_parents]

        for i in range(0,self.n_parents-1):
            child_1 , child_2 = parents[i] , parents[i+1]
            new_par = np.concatenate((child_1[:len(child_1)//2],child_2[len(child_1)//2:]))
            pop_next_gen.append(new_par)
        
        return pop_next_gen


    def mutation(self):
        """
        Randomly change half the chromosomes.
        """
        current_population = self.selection_crossover()   

        # Get number of chromosomes to mutate
        mutation_range = int(self.mutation_rate*self.n_features)
        pop_next_gen = []
        for n in range(0,len(current_population)):
            chromo = current_population[n]

            # Sample chromosomes to change
            indices = np.arange(0,self.n_features - 1)
            np.random.shuffle(indices)
            selected_chromosomes = indices[:mutation_range]

            for pos in selected_chromosomes:
                chromo[pos] = not chromo[pos]  
  
            pop_next_gen.append(chromo)
    
        self.population = self.population[:self.n_parents] + pop_next_gen
    

    def run(self):
        print("Starting Genetic Feature Selection")
        self.initialize_population()

        for i in range(self.n_gen):
            self.fitness_score()
            self.mutation()
        
        print("Genetic Feature Selection Complete")

    
    def get_fitness_scores(self):
        return self.best_scores
    
    def get_last_chromosome(self):
        return self.best_chromosomes[-1]
    
    def run_best_chromosome(self):
        chromosome = self.best_chromosomes[-1]
        # Fit and predict on the given model
        self.model.fit(self.X_tr.iloc[:,chromosome],self.y_tr)         
        predictions = self.model.predict(self.X_te.iloc[:,chromosome])

        return self.model