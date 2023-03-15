# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ApA8m85fHtKKoYOTO53LC2Yo_8i1NXZb
"""

import random as rd

class TS():
    def __init__(self, tabu_tenure, max_coef, step):
        self.tabu_tenure = tabu_tenure
        self.max_coef=max_coef 
        self.step=step 
        self.Initial_solution = self.get_InitialSolution()
        self.tabu_str, self.Best_solution, self.Best_objvalue = self.TSearch()
        
    # Generate random initial solution
    def get_InitialSolution(self, show=False):
        X=rd.randint(1,self.max_coef)
        Y=rd.randint(1,self.max_coef)
        Z=rd.randint(1,self.max_coef)
        initial_solution=[X,Y,Z]
        if show == True:
            print("initial Random Solution: {}".format(initial_solution))
        return initial_solution
    # Objective function
    def Objfun(self, solution, show = False):
        '''
        f=10*X+15*Y+20*Z
        4X+2Y<=400
        2X+2Y+2Z<=300
        X+2Y+3Z<=200
        X+Y+2Z<= 900
        X,Y,Z>=0
        '''
        tabu=False
        X=solution[0]
        Y=solution[1]
        Z=solution[2]
        c1=4*X+2*Y
        if c1>400:
            tabu=True
        c2=2*X+2*Y+2*Z
        if c2>300:
            tabu=True
        c3=1*X+2*Y+3*Z
        if c3>200:
            tabu=True
        c4=1*X+1*Y+2*Z
        if c3>900:
            tabu=True
        c5=1*X+1*Y+1*Z
        if c5<0:
            tabu=True
        objfun_value=10*X+15*Y+20*Z
        if show == True:
            print("\n","#"*8, "The Objective function value for {} solution  is: {}".format(solution ,objfun_value),"#"*8)
        return objfun_value,tabu

    def GenertaeNeigbour(self, solution):
        '''
        Takes a  solution 
        returns a new neighbor solution
       '''
        X=solution[0]
        Y=solution[1]
        Z=solution[2]
     
        solution = solution.copy()
        # Genertae neighbour
        # X,Y,Z are positives
        if (X-self.step)<0:
            a=1
        else:
            a=X-self.step
  
        solution[0]=rd.randint(a,X+self.step)
        if (Y-self.step)<0:
            a=1
        else:
            a=Y-self.step
        solution[1]=rd.randint(a,Y+self.step)
        if (Z-self.step)<0:
            a=1
        else:
            a=Z-self.step
        solution[2]=rd.randint(a,Z+self.step)
        return solution

    # Generate Tabu List
    def GenerateTabu(self, solution):
        dict = {}
        for _ in range(self.tabu_tenure):
            candidate_solution = self.GenertaeNeigbour(solution)
            candidate_objvalue,tabu = self.Objfun(candidate_solution)
            new_neibour=(candidate_solution[0],candidate_solution[1],candidate_solution[2])
            dict[new_neibour] = {'Value': candidate_objvalue, 'tabu': tabu }
        return dict

    def TSearch(self):
        '''The implementation Tabu search algorithm
        '''
        # Parameters:
        tenure =self.tabu_tenure
        best_solution = self.Initial_solution
        tabu_structure = self.GenerateTabu(best_solution)
        best_objvalue,_ = self.Objfun(best_solution)
        current_solution = self.Initial_solution
        current_objvalue = self.Objfun(current_solution)

        print("#"*30, "TS with Tabu Tenure: {}\nInitial Solution: {}, Initial Objvalue: {}".format(
            tenure, current_solution, current_objvalue), "#"*30, sep='\n\n')
        iter = 1
        Terminate = 0
        while Terminate < 100:
            print('\n\n### iter {}###  Current_Objvalue: {}, Best_Objvalue: {}'.format(iter, current_objvalue,
                                                                                    best_objvalue))
            # Searching the whole neighborhood of the current solution:
         
            tabu_structure=self.GenerateTabu(current_solution)
            # Admissible move
            while True:
                # select the solution with the highest ObjValue in the neighborhood (max)
                best_sol = max(tabu_structure, key =lambda x: tabu_structure[x]['Value'])
                SolValue = tabu_structure[best_sol]["Value"]
                tabu=tabu_structure[best_sol]["tabu"]
                # Not Tabu
                if not tabu :
                    # make it
                    current_solution = [best_sol[0],best_sol[1],best_sol[2]]
                    current_objvalue = SolValue
                    # Best Improving sol
                    if SolValue > best_objvalue:
                        best_solution = current_solution
                        best_objvalue = current_objvalue
                        print("   best_sol0: {}, Objvalue: {} => Best Improving => Admissible".format(best_sol,                                                                             current_objvalue))
                        Terminate = 0
                    else:
                        print("   ##Termination: {}## best_sol: {}, Objvalue: {} => Least non-improving => "
                              "Admissible".format(Terminate,best_sol,current_objvalue))
                        Terminate=Terminate+1
                        break
                # If tabu
                else:
                    tabu_structure[best_sol]["Value"] = -100
                    print("   best_sol2: {}, Objvalue: {} => Tabu => Inadmissible".format(best_sol,current_objvalue))
                    continue
        print('#'*50 , "Performed iterations: {}".format(iter), "Best found Solution: {} , Objvalue: {}".format(best_solution,best_objvalue), sep="\n")
        return tabu_structure, best_solution, best_objvalue


test = TS(tabu_tenure=200, max_coef=30, step=20)