"""
The code in this file implements a genetic algorithm used for feature selection within the project. 
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from random import randint


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
            population_size: 

        """
        self.size = population_size
        self.n_features = features.shape[1]
        self.population = []
        self.model = model
        self.mutation_rate = mutation_rate
        self.n_parents = n_parents
        self.n_gen = n_gen
        self.best_scores = []
        

        self.X_tr, self.X_te, self.Y_tr, self.Y_te = train_test_split(data, target, test_size=0.25, random_state=42)


    def initialize_population(self):
        """
        Initializes a random population by selecting 30 percent of features to be turned on.
        """
        for i in range(self.size):
            chromosome = np.ones(self.n_features, dtype=np.bool)     
            chromosome[:int(0.3*self.n_features)]=False             
            np.random.shuffle(chromosome)
        self.population.append(chromosome)
        

    def fitness_score(self):
        scores = []
        for chromosome in self.population:
            self.model.fit(self.X_tr.iloc[:,chromosome],self.Y_tr)         
            predictions = self.model.predict(self.X_te.iloc[:,chromosome])
            # should this be changed
            scores.append(accuracy_score(self.y_te,predictions))
        scores, temp_pop = np.array(scores), np.array(self.population) 
        inds = np.argsort(scores) 

        # Population get sorted by fitness scores                                   
        self.fitness_scores, self.population = list(scores[inds][::-1]), list(temp_pop[inds,:][::-1]) 

        self.best_scores.append(scores[:1])


    def selection(self):
        """
        Gets the best fit "parents". Update function to work with class.
        """
        population_nextgen = []
        for i in range(self.n_parents):
            population_nextgen.append(self.population[i])
        
        return population_nextgen


    def crossover(self):
        """
        Double check this function
        """
        pop_after_selection = self.selection()
        pop_next_gen = pop_after_selection
        for i in range(0,len(pop_after_selection),2):
            new_par = []
            child_1 , child_2 = pop_next_gen[i] , pop_next_gen[i+1]
            new_par = np.concatenate((child_1[:len(child_1)//2],child_2[len(child_1)//2:]))
            pop_next_gen.append(new_par)
        
        return pop_next_gen


    def mutation(self):
        current_population = self.crossover()   
        mutation_range = int(self.mutation_rate*self.n_feat)
        pop_next_gen = []
        for n in range(0,len(current_population)):
            chromo = current_population[n]
            rand_posi = [] 
            for i in range(0,mutation_range):
                pos = randint(0,self.n_feat-1)
                rand_posi.append(pos)
            for j in rand_posi:
                chromo[j] = not chromo[j]  
            pop_next_gen.append(chromo)
    
        self.population = pop_next_gen
    

    def run(self):
        best_chromo= []
        best_score= []
    
        for i in range(self.n_gen):
            scores, pop_after_fit = self.fitness_score(population_nextgen)
            population_nextgen = self.mutation()
            best_chromo.append(pop_after_fit[0])
            best_score.append(scores[0])
            
        return best_chromo,best_score

    

