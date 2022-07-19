import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint

def soma(C, numCol, linAltC, linAgntC, const):
  for i in range(numCol):
    C[linAltC][i] += const*C[linAgntC][i]

def multiplica(C, numCol, linC, const):
  for i in range(numCol):
    if(C[linC][i] != 0):
      C[linC][i] *= const

def troca(C, numCol, linTroca1, linTroca2):
  for i in range(numCol):
    temp = C[linTroca1][i]
    C[linTroca1][i] = C[linTroca2][i]
    C[linTroca2][i] = temp

def transpostar(C, num_pont):
  Ct = np.zeros((3, num_pont))
  for i in range(num_pont):
    for j in range(3):
      Ct[j][i] = C[i][j]
  return Ct

def aleatorios(As, A, s, lista1, lista2, lista3, max, min, qnt):
  maior = 0
  menor = 0
  maior_x = 0
  menor_x = 0
  maior_y = 0
  menor_y = 0
  for i in range(qnt):
    As[i][2] = 1
    A[i][2] = 1
    n = randint(min, max)
    As[i][0] = n
    A[i][0] = n
    if(maior_x < As[i][0]):
      maior_x = As[i][0]
    if(menor_x > As[i][0]):
      menor_x = As[i][0]
    lista1.append(n)
    n = randint(min, max)
    As[i][1] = n
    A[i][1] = n
    if(maior_y < As[i][1]):
      maior_y = As[i][1] 
    if(menor_y > As[i][1]):
      menor_y = As[i][1]
    lista2.append(n)
    n = randint(min, max)
    As[i][3] = n
    s[i] = n
    if(maior < As[i][3]):
      maior = As[i][3]
    if(menor > As[i][3]):
      menor = As[i][3]
    if(maior > maior_x and maior > maior_y):
      maior_x = maior
      maior_y = maior
    if(menor < menor_x and menor < menor_y):
      menor_x = menor
      menor_y = menor
    lista3.append(n)
  return lista1, lista2, lista3, As, A, s, maior_x, menor_x, maior_y, menor_y

def reduzir(C):
  numLin, numCol = np.shape(C)
  numCol -= 1
  print("")
  print("Matriz:")
  print(C)
  print("")
  startLin = 0
  for col in range(numCol):
    precisaPivot = True
    for lin in range(startLin, numLin):
      if not precisaPivot:
        break
      if C[lin][col] != 0:
        print("Pivot: linha",lin+1,"e coluna",col+1)
        print("")
        if lin != startLin:
          print("Linha",lin+1,"troca com linha",startLin+1)
          troca(C, numCol+1, lin, startLin)
          print("")
          print(C)
          print("")
          lin = startLin
        startLin += 1
        if C[lin][col] != 1:
          print("Deixando o pivot com o valor 1: dividindo a linha",lin+1,"por",C[lin][col])    
          print("")
          multiplica(C, numCol + 1, lin, 1/C[lin][col])
          print("Matriz:")
          print(C)
          print("")
        for i in range(numLin):
          if i != lin and C[i][col] != 0:
            print("Linha",i+1,"recebe linha",i+1,"menos linha",lin+1,"vezes",C[i][col])
            print("")
            soma(C, numCol + 1, i, lin, -1*C[i][col])
            print("Matriz:")
            print(C)
            print("")
        precisaPivot = False
  return C

while True:
  num_pont = int(input("Informe a quantidade de pontos que deseja inserir(>= 3): "))
  print("")
  if(num_pont >= 3):
    break
  print("Valor inválido, tente novamente.")  
  print("")
resposta = 3
while(resposta != 1 and resposta != 2):
  print("Selecione uma das opções:")
  print("(1) Escolher cada um dos pontos.")
  print("(2) Selecionar aleatoriamente os pontos.")
  print("")
  resposta = int(input("Valor: "))
  print("")
ponto_x = []
ponto_y = []
ponto_z = []
A = np.zeros((num_pont, 3))
s = np.zeros((num_pont, 1))
As = np.zeros((num_pont, 4))
if(resposta == 1):
  maior = 0
  menor = 0
  maior_x = 0  
  menor_x = 0
  maior_y = 0
  menor_y = 0
  for i in range(num_pont):
    print("Ponto",i+1)
    ponto_x.append(int(input("Valor de x: ")))
    As[i][0] = A[i][0] = ponto_x[i]
    if(maior_x < As[i][0]):
      maior_x = As[i][0]
    if(menor_x > As[i][0]):
      menor_x = As[i][0]
    ponto_y.append(int(input("Valor de y: ")))
    As[i][1] = A[i][1] = ponto_y[i]
    if(maior_y < As[i][1]):
      maior_y = As[i][1] 
    if(menor_y > As[i][1]):
      menor_y = As[i][1]
    ponto_z.append(int(input("Valor de z: ")))
    print("")
    As[i][3] = s[i] = ponto_z[i]
    if(maior < As[i][3]):
      maior = As[i][3]
    if(menor > As[i][3]):
      menor = As[i][3]
    if(maior > maior_x and maior > maior_y):
      maior_x = maior
      maior_y = maior
    if(menor < menor_x and menor < menor_y):
      menor_x = menor
      menor_y = menor
    As[i][2] = A[i][2] = 1
else:
  range_p = 0
  range_n = 0
  while(range_p == 0 and range_n == 0):
    range_p = int(input("Maior valor possível de coordenada: "))
    range_n = int(input("Menor valor possível de coordenada: "))
  ponto_x, ponto_y, ponto_z, As, A, s, maior_x, menor_x, maior_y, menor_y = aleatorios(As, A, s, ponto_x, ponto_y, ponto_z, range_p+1, range_n+1, num_pont)
As = reduzir(As)
if(As[2][2] == 0 and As[2][3] == 0):
  fig = plt.figure(figsize = (10, 10))
  eixos = plt.axes(projection="3d")
  eixos.scatter3D(ponto_x, ponto_y, ponto_z, alpha = 1, color='red')
  eixos.set_xlabel('X') 
  eixos.set_ylabel('Y') 
  eixos.set_zlabel('Z') 
  plt.show()
  print("Os",num_pont,"pontos são colineares entre si. Portanto, existem infinitos planos que os contém.")
  fig = plt.figure(figsize = (10, 10))
  eixos = plt.axes(projection="3d")
  eixos.scatter3D(ponto_x, ponto_y, ponto_z, alpha = 1, color='red')
  eixos.plot3D(ponto_x, ponto_y, ponto_z, 'blue')
  eixos.set_xlabel('X') 
  eixos.set_ylabel('Y') 
  eixos.set_zlabel('Z') 
  plt.show()
else:
  At = transpostar(A, num_pont)
  while(np.linalg.det(np.matmul(At,A)) == 0):
    As[0][0] -= 0.00000005
    A[0][0] -= 0.00000005
    As[0][1] -= 0.00000002
    A[0][1] -= 0.00000002
    As[0][3] += 0.00000002
    s[0] += 0.00000002
    At = transpostar(A, num_pont)
  mentira = False
  for i in range(3, num_pont):
    if(As[i][3] != 0):
      mentira = True
  if(As[2][2] == 0 and As[2][3] != 0):
    mentira = True
  if(not mentira):
    x = np.arange(2*menor_x, 2*maior_x, 0.5)
    y = np.arange(2*menor_y, 2*maior_y, 0.5)
    x, y = np.meshgrid(x, y)
    z = As[0][3] * x + As[1][3] * y + As[2][3]   
    fig = plt.figure(figsize = (10, 10))
    eixos = Axes3D(fig, auto_add_to_figure = False)
    fig.add_axes(eixos)
    eixos.plot_surface(x,y,z, alpha = 0, cmap='viridis', edgecolor='none')
    eixos.scatter3D(ponto_x, ponto_y, ponto_z, alpha = 1, color='red')  
    eixos.set_xlabel('X') 
    eixos.set_ylabel('Y') 
    eixos.set_zlabel('Z') 
    plt.show()
    print("Plano:",As[0][3],"* x +",As[1][3],"* y +",As[2][3],"= z")
    x = np.arange(2*menor_x, 2*maior_x, 0.5)
    y = np.arange(2*menor_y, 2*maior_y, 0.5)
    x, y = np.meshgrid(x, y)
    z = As[0][3] * x + As[1][3] * y + As[2][3]   
    fig = plt.figure(figsize = (10, 10))
    eixos = Axes3D(fig, auto_add_to_figure = False)
    fig.add_axes(eixos)
    eixos.plot_surface(x,y,z, alpha = 0.5, cmap='viridis', edgecolor='none')
    eixos.scatter3D(ponto_x, ponto_y, ponto_z, alpha = 1, color='red')  
    eixos.set_xlabel('X') 
    eixos.set_ylabel('Y') 
    eixos.set_zlabel('Z') 
    plt.show()
  else:
    print("Sistema sem solução!")
    print("")
    print(ponto_z)
    A = np.matmul(At, A)
    s = np.matmul(At, s)
    invAAt = np.linalg.inv(A)
    s = np.matmul(invAAt, s)
    x = np.arange(2*menor_x, 2*maior_x, 0.5)
    y = np.arange(2*menor_y, 2*maior_y, 0.5)
    x, y = np.meshgrid(x, y)
    z = s[0] * x + s[1] * y + s[2]  
    fig = plt.figure(figsize = (10, 10))
    eixos = Axes3D(fig, auto_add_to_figure = False)
    fig.add_axes(eixos)
    eixos.plot_surface(x,y,z, alpha = 0, cmap='viridis', edgecolor='none')
    eixos.scatter3D(ponto_x, ponto_y, ponto_z, alpha = 1, color='red')  
    eixos.set_xlabel('X') 
    eixos.set_ylabel('Y') 
    eixos.set_zlabel('Z') 
    plt.show()
    print("Plano próximo do ideal:",s[0],"* x +",s[1],"* y +",s[2],"= z")
    x = np.arange(2*menor_x, 2*maior_x, 0.5)
    y = np.arange(2*menor_y, 2*maior_y, 0.5)
    x, y = np.meshgrid(x, y)
    z = s[0] * x + s[1] * y + s[2]  
    fig = plt.figure(figsize = (10, 10))
    eixos = Axes3D(fig, auto_add_to_figure = False)
    fig.add_axes(eixos)
    eixos.plot_surface(x,y,z, alpha = 0.5, cmap='viridis', edgecolor='none')
    eixos.scatter3D(ponto_x, ponto_y, ponto_z, alpha = 1, color='red')  
    eixos.set_xlabel('X') 
    eixos.set_ylabel('Y') 
    eixos.set_zlabel('Z') 
    plt.show()