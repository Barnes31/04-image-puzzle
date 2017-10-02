
import sys, pygame, random

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

#pygame stuff
pygame.init()

size = (width, height) = (400,400)

dimensions = (rows,columns) = (4,4)

font= pygame.font.SysFont("arial",64)

screen = pygame.display.set_mode(size)

#Square object
class Square:
                color = ' '
                label = ' '
                position = (-1, -1)
                size =(0,0)
                visible = True
                

                def __init__ (self, x, y, width, height):
                                self.position = (x,y)
                                self.size = (width, height)                            

                def check_proximity (self, xy):
                                '''checks if the the given square is directly next to the empty square'''
                                if (abs(xy[0] - self.position[0])) > 1:
                                                return False
                                if (abs(xy[1] - self.position[1])) > 1:
                                                return False
                                if (abs (xy[1] - self.position[1])) == 1 and (abs(xy[0] - self.position[0])) ==1:
                                                return False
                                if xy[0] < 0 or xy[0] > 3:
                                                return False
                                if xy[1] < 0 or xy[1] > 3:
                                                return False
                                return True
                            
                def swap_position (self, xy):
                                '''swaps the position of the empty square and the given/clicked square'''
                                self.position = xy
                                
                def draw_square(self, draw, screen):
                                ''' add the square to the draw object '''
                                if self.visible:
                                                (x1,y1) = self.position
                                                (w,h) = self.size
                                                (x,y) = (x1 * w,y1 * h)
                                                draw.rect(screen, self.color, (x,y,w,h))
                                                f = font.render(self.label,True,(0,0,0))
                                                (fwidth,fheight) = font.size(self.label)
                                                #center the font
                                                (fx,fy) = (x + (w - fwidth)/2,y + (h - fheight)/2)
                                                screen.blit(f,(fx,fy))
                                                return draw
	    
def draw_puzzle(puzzle):
                '''draws the squares on the screen'''
                screen.fill((0,0,0))
                for i in range (len(puzzle)):
                                puzzle[i].draw_square(pygame.draw,screen)
                pygame.display.flip()
                                            
def calculate_xy(pos, puzzle):
                '''calulates which square is the target'''
                (w,h) = (width/columns, height/rows)
                return (int(pos[0]//w), int(pos[1]//h))
            
def rand_puzzle(count, puzzle):
                '''randomizes the puzzle'''
                for empty in puzzle:
                                if not empty.visible:
                                            for color in range(count):
                                                            xy = (x,y) = (empty.position[0] + random.randint(-1,1), empty.position[1] + random.randint (-1,1))
                                                            if empty.check_proximity(xy):
                                                                                for p in puzzle:
                                                                                                    if p.position == xy:
                                                                                                                    p.swap_position(empty.position)
                                                                                                                    empty.swap_position(xy)
                return puzzle
            
colors = {
                'bright lime' : [0,255,0],
                'violet' : [204, 153, 255],
                 'blue' : [153,153,255],
                'green' : [153,255,204],
                'Light blue' : [153,255,255],
                'red' : [255,153,153],
                'pink' : [255,153,255],
                'lime' : [153,255,153],
                'baby' : [153,204,255],
                'pink2' : [255,0,255],
                'baby2' : [0,128,255],
                'purple2' : [127,0,255],
                'blue2' : [0,0,255],
                'brightb' : [0,255,255],
                'brightg' : [0,255,128],
}
colorlist = list(colors.keys())

# build puzzle
puzzle = []
count = 0

for y in range (4):
                for x in range (4):
                                colorlist = list(colors.keys())
                                sqr = Square (x, y, width / columns, height / rows)
                                sqr.color = colors[colorlist[count % len(colors)]]
                                sqr.label = str(count + 1)
                                count = count + 1
                                sqr.visible = True
                                puzzle.append(sqr)
puzzle[len(puzzle) -1].visible = False

puzzle = rand_puzzle(100, puzzle)

draw_puzzle(puzzle)

Solved = False

emptySqr = puzzle[15]

while not Solved:
                for event in pygame.event.get():
                                if event.type == pygame.QUIT: sys.exit()
                                # handle MOUSEBUTTONUP
                                if event.type == pygame.MOUSEBUTTONUP:
                                                pos = pygame.mouse.get_pos()
                                                xy = calculate_xy(pos,puzzle)
                                                print(xy)
                                                for empty in puzzle:
                                                                if not empty.visible:
                                                                                if empty.check_proximity(xy):
                                                                                                for color in puzzle:
                                                                                                                if color.position == xy:
                                                                                                                                color.swap_position(empty.position)
                                                                                                                                empty.swap_position(xy)
                                                                                                                                draw_puzzle(puzzle)
                               
                                Solved = True 
                                for i in range(len(puzzle)):
                                                xy = (x,y) = (i % columns, i //  rows)
                                                if puzzle[i].position != xy:
                                                                Solved = False
                                if Solved:
                                                for empty in puzzle:
                                                                empty.visible = True

print('Congratulations! You won!')

