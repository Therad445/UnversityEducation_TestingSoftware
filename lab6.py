from multiprocessing import Value
from concurrent.futures import ThreadPoolExecutor
import numpy as np


class MatrixParallel:
   def __init__(self, threadNum=1, matrixes=None):
      self.__threadNum = threadNum
      if matrixes:
         self.__matrixes = matrixes
      else:
         self.__matrixes = []
     
   def addMatrix(self, matrix):    
      self.__assertSize(matrix)      

      if len(self.__matrixes) == 0:
            self.__M = matrix.shape[0]
       
      self.__assertEqualSize(matrix)
      
      self.__matrixes.append(matrix)
    

   def __assertLessLength(self, size):
      if len(self.__matrixes) < size:
         raise ValueError("Length matrix is invalid")


   def __assertEqualSize(self, matrix):
      if matrix.shape[0] != self.__M:
         raise ValueError(f"Matrix is not {self.__M}x{self.__M}")


   def __assertSize(self, matrix):
      if matrix.shape[0] != matrix.shape[1] or len(matrix.shape) != 2:
        raise ValueError(f"Matrix must be MxM, not "
                         f"({matrix.shape[0]}, {matrix.shape[1]})")


   def __dot(self, t):
       matrix1, matrix2 = t 
       result = np.eye(self.__M, self.__M)
        
       result = result.dot(matrix1)
       result = result.dot(matrix2)
        
       return result
   

   def __distributeThreads(self, matrixes):
      threads = []
      
      for i in range(0, len(matrixes) - 1, 2):
         threads.append((matrixes[i], matrixes[i + 1]))
      
      if len(matrixes) % 2 != 0:
         threads.append(matrixes[-1])
      
      return threads


   def __threadDot(self, t):
      matrix1, matrix2, buf, threadId = t
      buf[threadId] = self.__dot(matrix1, matrix2)


   def __joinThreads(self, threads):
      for thread in threads:
         thread.join()


   def calculateParallel(self):
       index = 0
       threads = []
       self.__assertLessLength(2)
       result = self.__distributeThreads(self.__matrixes)
       
       while len(result) != 1:
          buf = {}
          dots = []
          
          for res in result:
            if len(res) == 2:
               buf[index] = (res[0], res[1]) 
               index += 1
               
          with ThreadPoolExecutor(max_workers=2) as executor:
             dots = list(executor.map(self.__dot, list(buf.values())))
                       
          if len(result[-1]) != 2:
               dots.append(res)
          
          self.__joinThreads([th[1] for th in threads])
           
          result = self.__distributeThreads(dots)
        
       result = self.__dot((result[0][0], result[0][1]))

       return result
       
        


   def dot(self):
      self.__assertLessLength(2)
      return self.__dot(self.__matrixes[0], self.__matrixes[1])
         
      

def main():
    M = 100

    par = MatrixParallel()
    for i in range(100):
        par.addMatrix(np.eye(M, M))
        
    par.addMatrix(np.arange(M**2).reshape((M, M)))
    par.addMatrix(np.arange(M**2).reshape((M, M)))
    print(par.calculateParallel())



main()