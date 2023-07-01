import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		self.sprite = pygame.image.load(image)
		width = self.sprite.get_width()
		height = self.sprite.get_height()
		self.image = pygame.transform.scale(self.sprite, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft  = (x, y)
		self.clicked = False

	def press(self,pos):
		action = False
		if self.rect.collidepoint(pos):
				action = True

		return action

		