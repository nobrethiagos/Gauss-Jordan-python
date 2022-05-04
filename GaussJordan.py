#Algoritmo: Gauss-Jordan
#Autor: Thiago Silveira Nobre
#Data: 03/05/2022

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

def fatorizar(C):
  numLin, numCol = np.shape(C)
  B = identidade(numLin)
  precisaMuitoPivot = False
  startCol = 0
  endLin = 0
  for lin in range(numLin):
    if precisaMuitoPivot:
      precisaMuitoPivot = False
      for linEsp in range(lin, numLin):
        for colEsp in range(startCol, numCol):
          if C[linEsp][colEsp] != 0:
            startCol = colEsp + 1
            soma(B, C, numLin, numCol, endLin, linEsp, 1/C[linEsp][colEsp])
            for i in range(numLin):          
              if i != endLin:
                soma(B, C, numLin, numCol, i, endLin, -1*C[i][colEsp])
    precisaPivot = True
    for col in range(startCol, numCol):
      if not precisaPivot:
        break
      if C[lin][col] != 0:
        startCol = col + 1
        if C[lin][col] != 1:
          multiplica(B, C, numLin, numCol, lin, 1/C[lin][col])
        for i in range(numLin):         
          if i != lin:
            soma(B, C, numLin, numCol, i, lin, -1*C[i][col])
        precisaPivot = False
      elif col == (numCol - 1) and not precisaMuitoPivot:
        precisaMuitoPivot = True
        endLin = lin
  return B, C

C = np.zeros((4, 8))
C[0] = [1, 1, 11, 101, 11, 2, 13, 2]
C[1] = [1, 2, 12, 102, 21, 3, 10, 2]
C[2] = [1, 3, 13, 103, 31, 4, 7, 2]
C[3] = [1, 4, 14, 104, 41, 5, 4, 3]

print("A:")
print(C)
B, C = fatorizar(C)
print("")
print("B:")
print(B)
print("")
print("C:")
print(C)