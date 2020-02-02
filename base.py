import pyglet

HEIGHT = 600
WIDTH = 800

ICONS = {
    'icon1': {'x': WIDTH * 0.02, 'y': HEIGHT * 0.9, 'name': 'icon1', 'img': 'images/carre_34_blue.png'},
    'icon2': {'x': WIDTH * 0.02, 'y': HEIGHT * 0.8, 'name': 'icon2', 'img': 'images/carre_34_pink.png'},
    'icon3': {'x': WIDTH * 0.02, 'y': HEIGHT * 0.7, 'name': 'icon3', 'img': 'images/carre_34_red.png'},
    'icon4': {'x': WIDTH * 0.02, 'y': HEIGHT * 0.6, 'name': 'icon4', 'img': 'images/carre_34_yellow.png'},
}

ROW = 12
COL = 16

window = pyglet.window.Window(WIDTH, HEIGHT)


class TSprite(pyglet.sprite.Sprite):
    def __init__(self, img, x, y, batch=None, name=''):
        super(TSprite, self).__init__(pyglet.resource.image(img), x, y, batch=batch)
        self.name = name
        self.img = img

        window.push_handlers(self.on_mouse_press)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.opacity = 175

            image = pyglet.image.load(self.img)
            cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
            window.set_mouse_cursor(cursor)


class Board(pyglet.sprite.Sprite):
    # board = [[0]*COL for _ in range(ROW)]

    def __init__(self, arg=None):
        # super(Board, self).__init__()
        self.arg = arg

        window.push_handlers(self.on_mouse_press)

    def on_mouse_press(self, x, y, button, modifiers):
        print(abs((y // 50) - 11), x // 50)
        val_x = abs((y // 50) - 11)
        val_y = x // 50
        pyglet.sprite.Sprite(img=pyglet.resource.image('images/carre_34_blue.png'), x=val_x, y=val_y)


class Base:
    money = 10000
    pause = False

    def __init__(self):
        self.board = Board()
        self.sprite = pyglet.sprite.Sprite(img=pyglet.resource.image('images/background.v4.png'), x=0, y=0)

        money_label = f"{Base.money} $"
        self.money = pyglet.text.Label(money_label, font_size=18, x=WIDTH*0.9, y=HEIGHT*0.95)
        self.icon1 = TSprite(**ICONS['icon1'])
        self.icon2 = TSprite(**ICONS['icon2'])
        self.icon3 = TSprite(**ICONS['icon3'])
        self.icon4 = TSprite(**ICONS['icon4'])

        window.event(self.on_key_press)
        window.event(self.on_draw)
        window.push_handlers(self.on_mouse_press)

        pyglet.clock.schedule(self.game_loop)
        pyglet.app.run()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_draw(self):
        window.clear()
        self.sprite.draw()
        self.money.draw()
        self.icon1.draw()
        self.icon2.draw()
        self.icon3.draw()
        self.icon4.draw()

    def game_loop(self, _):
        self.money.text = f"{int(self.money.text[:-1]) - 1} $"

    def on_key_press(self, symbol, modifiers):
        if symbol == 112:
            if Base.pause:
                Base.pause = False
                pyglet.clock.schedule(self.game_loop)
            else:
                Base.pause = True
                pyglet.clock.unschedule(self.game_loop)


Base()
