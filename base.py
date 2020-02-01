import pyglet
# from pyglet.gl import *

# class TSprite(pyglet):
# 	def __init__(self, *args): # imgs, var_x, var_y):

# 		# super(pyglet.sprite.Sprite).__init__(self)
# 		pyglet.sprite.Sprite(
# 			img=pyglet.resource.image(imgs), 
# 			x = var_x, 
# 			y = var_y
# 		)


class Base:
	HEIGHT = 600
	WIDTH = 800

	MONEY = 10000
	PAUSE = 0

	def __init__(self):
		self.window = pyglet.window.Window(Base.WIDTH, Base.HEIGHT)
		self.sprite = pyglet.sprite.Sprite(img=pyglet.resource.image('images/background.v4.png'),x = 0, y = 0)
		self.money = pyglet.text.Label(str(Base.MONEY) + " $", font_size=18, x = Base.WIDTH * 0.9, y = Base.HEIGHT * 0.95)
		self.icon1 = pyglet.sprite.Sprite(img=pyglet.resource.image('images/carre_34_blue.png'), x = Base.WIDTH * 0.02, y = Base.HEIGHT * 0.9)
		self.icon2 = pyglet.sprite.Sprite(img=pyglet.resource.image('images/carre_34_pink.png'), x = Base.WIDTH * 0.02, y = Base.HEIGHT * 0.8)
		self.icon3 = pyglet.sprite.Sprite(img=pyglet.resource.image('images/carre_34_red.png'), x = Base.WIDTH * 0.02, y = Base.HEIGHT * 0.7)
		self.icon4 = pyglet.sprite.Sprite(img=pyglet.resource.image('images/carre_34_yellow.png'), x = Base.WIDTH * 0.02, y = Base.HEIGHT * 0.6)
		# self.test = TSprite('images/counter.png', Base.WIDTH / 2, Base.HEIGHT / 2)


		self.window.event(self.on_key_press)
		self.window.event(self.on_draw)
		self.window.event(self.on_mouse_press)
		
		pyglet.clock.schedule(self.game_loop)

		pyglet.app.run()

	def on_mouse_press(self, x, y, button, modifiers):
		print 'mouse pressed on sprite', self


	def on_draw(self):
		self.window.clear()
		self.sprite.draw()
		self.money.draw()
		self.icon1.draw()
		self.icon2.draw()
		self.icon3.draw()
		self.icon4.draw()
		# self.test.draw()

	def game_loop(self, _):
		self.money.text = str(int(self.money.text[:-1]) - 1) + " $"

	def on_key_press(self, symbol, modifiers):
		if symbol == 112 and Base.PAUSE == 0:
			pyglet.clock.unschedule(self.game_loop)
			Base.PAUSE = 1
		elif symbol == 112 and Base.PAUSE == 1: 
			Base.PAUSE = 0
			pyglet.clock.schedule(self.game_loop)
		
	
Base()