import pygame, random, math

pygame.init()

# Set up the display
width, height = 800, 600  # Size of the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Molecule Simulation")

class Molecule:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
    
    def update(self, molecules):
        # Apply basic physics and boundary conditions
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off the edges
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.vx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.vy *= -1
        
        # Interact with other molecules
        for other in molecules:
            if other == self:
                continue
            dx = other.x - self.x
            dy = other.y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance < self.radius + other.radius:
                # Simple collision response
                angle = math.atan2(dy, dx)
                total_mass = self.radius + other.radius
                self.vx -= (other.radius / total_mass) * 2 * dx / distance
                self.vy -= (other.radius / total_mass) * 2 * dy / distance
                other.vx += (self.radius / total_mass) * 2 * dx / distance
                other.vy += (self.radius / total_mass) * 2 * dy / distance

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def generate_molecules(num_molecules):
    molecules = []
    for _ in range(num_molecules):
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)
        radius = random.randint(10, 20)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        molecule = Molecule(x, y, radius, color)
        molecules.append(molecule)
    return molecules

molecules = generate_molecules(50)

# Clock object to control the frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second

# Main loop
running = True
while running:
    # Clear the screen
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update and draw each molecule
    for molecule in molecules:
        molecule.update(molecules)
        molecule.draw()
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(fps)

# Quit pygame
pygame.quit()

