import pygame
from functions import generateRandomArray


def displaySortedArray():
    global sorted
    sorted = True

    # bubble sort algorithm
    for i in range(arrayLength):
        xcor = 0

        for j in range(arrayLength-i-1):
            # highlight the first compared bar
            position = ((xcor, 100), (barWidth, array[j]))
            pygame.draw.rect(window, red, position)

            # highlight the second compared bar
            position = ((xcor + barWidth + barMargin, 100), (barWidth, array[j+1]))
            pygame.draw.rect(window, red, position)

            # show the comparison and wait
            pygame.display.update()
            pygame.time.wait(100//sortingSpeed)

            if array[j] > array[j+1]:
                # clear the first bar -> preparing the swap
                position = ((xcor, 100), (barWidth, array[j]))
                pygame.draw.rect(window, white, position)

                # clear the second bar -> preparing the swap
                position = ((xcor + barWidth + barMargin, 100), (barWidth, array[j+1]))
                pygame.draw.rect(window, white, position)

                # swap elements
                array[j], array[j+1] = array[j+1], array[j]

            # swap or unhighlight the compared bars
            position = ((xcor, 100), (barWidth, array[j]))
            pygame.draw.rect(window, blue, position)
            position = ((xcor + barWidth + barMargin, 100), (barWidth, array[j+1]))
            pygame.draw.rect(window, blue, position)

            pygame.display.update()

            xcor += barWidth + barMargin

        # highlight each iteration's last bar as it is already sorted
        position = ((xcor, 100), (barWidth, array[-i-1]))
        pygame.draw.rect(window, orange, position)

    pygame.display.update()


def displayRandomArray():
    # clear the previous array
    position = ((0, 100), (width, height-100))
    pygame.draw.rect(window, white, position)

    # generate new random array
    global sorted, array
    sorted = False
    array = generateRandomArray(arrayLength, 10, 500)

    # display the new array
    xcor = 0
    for barHeight in array:
        position = ((xcor, 100), (barWidth, barHeight))
        pygame.draw.rect(window, blue, position)
        xcor += barWidth + barMargin

    pygame.display.update()


# initialising the graphics settings
pygame.init()
pygame.display.set_caption("Bubble Sort Visualiser")
font = pygame.font.SysFont('Times New Roman', 25)

white = (255, 255, 255)
black = (000, 000, 000)
blue = (133, 146, 158)
orange = (245, 176, 65)
red = (236, 112, 99)

width = 600
height = 600

window = pygame.display.set_mode((width, height))
window.fill(white)

barWidth = 5
barMargin = 2
arrayLength = width // (barWidth + barMargin) + 1

sortingSpeed = 10  # range: 1-100


# displaying user's options
label = font.render("'SPACE' - RESET  |  'ENTER' - SORT  |  'ESC' - EXIT", True, black)
window.blit(label, (20, 40))
pygame.draw.line(window, black, (0, 97), (width, 97), 4)
pygame.display.update()

displayRandomArray()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            elif event.key == pygame.K_SPACE:
                displayRandomArray()

            elif event.key == pygame.K_RETURN:
                if not sorted:
                    displaySortedArray()
