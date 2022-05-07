"""
Algoritmo: Gauss-Jordan
Autor: Thiago Silveira Nobre
Data: 03/05/2022
"""

import numpy as np

def identidade(n):
  I = np.zeros((n,n))
  for i in range(n):
    I[i][i] = 1
  return I

def soma(B, C, numLin, numCol, linAltC, linAgntC, const):
  for i in range(numCol):
    C[linAltC][i] += const*C[linAgntC][i]
  for i in range(numLin):
    B[i][linAgntC] -= const*B[i][linAltC]
  return B, C

def multiplica(B, C, numLin, numCol, linC, const):
  for i in range(numCol):
    C[linC][i] *= const
  for i in range(numLin):
    B[i][linC] /= const
  return B, C

def fatorar(C):
  """
  print("A:")
  print(C)
  print("")
  """
  numLin, numCol = np.shape(C)
  B = identidade(numLin)
  """
  print("B:")
  print(B)
  print("")
  print("C:")
  print(C)
  print("")
  """
  precisaMuitoPivot = False
  startCol = 0
  endLin = 0
  for lin in range(numLin):
    if precisaMuitoPivot:
      precisaMuitoPivot = False
      for linEsp in range(lin, numLin):
        for colEsp in range(startCol, numCol):
          if C[linEsp][colEsp] != 0:
            """
            print("Foi encontrado um pivot para a linha",endLin+1,"na linha",linEsp+1,"coluna",colEsp+1)
            print("")
            """
            startCol = colEsp + 1
            """
            print("Linha",endLin+1,"recebe linha",endLin+1,"mais linha",linEsp+1,"vezes",1/C[linEsp][colEsp])
            print("")
            """
            soma(B, C, numLin, numCol, endLin, linEsp, 1/C[linEsp][colEsp])
            """
            print("B:")
            print(B)
            print("")
            print("C:")
            print(C)
            print("")
            """
            for i in range(numLin):          
              if i != endLin and C[i][colEsp] != 0:
                """
                print("Linha",i+1,"recebe linha",i+1,"menos linha",endLin+1,"vezes",C[i][colEsp])
                print("")
                """
                soma(B, C, numLin, numCol, i, endLin, -1*C[i][colEsp])
                """
                print("B:")
                print(B)
                print("")
                print("C:")
                print(C)
                print("")
                """
    precisaPivot = True
    for col in range(startCol, numCol):
      if not precisaPivot:
        break
      if C[lin][col] != 0:
        """
        print("Pivot: linha",lin+1,"e coluna",col+1)
        print("")
        """
        startCol = col + 1
        if C[lin][col] != 1:
          """
          print("Deixando o pivot com o valor 1: dividindo a linha",lin+1,"por",C[lin][col])    
          print("")
          """
          multiplica(B, C, numLin, numCol, lin, 1/C[lin][col])
          """
          print("B:")
          print(B)
          print("")
          print("C:")
          print(C)
          print("")
          """
        for i in range(numLin):         
          if i != lin and C[i][col] != 0:
            """
            print("Linha",i+1,"recebe linha",i+1,"menos linha",lin+1,"vezes",C[i][col])
            print("")
            """
            soma(B, C, numLin, numCol, i, lin, -1*C[i][col])
            """
            print("B:")
            print(B)
            print("")
            print("C:")
            print(C)
            print("")
            """
        precisaPivot = False
      elif col == (numCol - 1) and not precisaMuitoPivot:
        precisaMuitoPivot = True
        endLin = lin
  linNula = []
  for lin in range(numLin):
    for col in range(numCol):
      if C[lin][col] != 0:
        break
      if col == numCol - 1:
        linNula.append(lin+1)
  if len(linNula) != 0:
    """
    print("Limpando linhas nulas:",linNula)
    print("")
    """
    j = 0
    for i in linNula:
      C = np.delete(C,i-1-j,0)
      B = np.delete(B,i-1-j,1)
      j += 1
  """
  print("B:") 
  print(B)
  print("")
  print("C:")
  print(C)
  print("")
  """
  return B, C

"""
C = np.zeros((4, 8))
C[0] = [1, 1, 11, 101, 11, 2, 13, 2]
C[1] = [1, 2, 12, 102, 21, 3, 10, 2]
C[2] = [1, 3, 13, 103, 31, 4, 7, 2]
C[3] = [1, 4, 14, 104, 41, 5, 4, 3]

B, C = fatorar(C)
"""
