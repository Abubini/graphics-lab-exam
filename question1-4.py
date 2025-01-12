import numpy as np

import pygame




def find_matrix_shape(matrix):
    print(matrix.shape)
matrix = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])

find_matrix_shape(matrix)




#for question 2!

def compute_cross_product(array1, array2):
    result =  np.cross(array1,array2)
    print(result)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
compute_cross_product(arr1,arr2)



#for question 3!

matrix1 = np.array(
[
[3,4,3],
[1,2,3],
[4,2,1]
]
)
U, S, V = np.linalg.svd(matrix1)
    
def reconstruct_matrix(U,S,V):
    original_matrix = (U @ np.diag(S) @ V)
    print(original_matrix)


reconstruct_matrix(U,S,V)


#for question 4!

#AAAAAAA



import pygame
pygame.init()

width, height = 500, 400
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("grapics lab test")
screen.fill(white)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                pygame.quit()
            run = False
        pygame.draw.line(screen, green, (50, 50), (250, 250), 3)
        pygame.draw.polygon(screen, blue, [(250, 0), (100,150), (400, 150)])
        pygame.draw.polygon(screen, blue, [(100, 150), (-50,300), (250, 300)])
        pygame.draw.polygon(screen, blue, [(400, 150), (250,300), (550, 300)])
        pygame.draw.circle(screen, red, (250, 200), 5)
    pygame.display.flip()
   
#BBBBBBBB


