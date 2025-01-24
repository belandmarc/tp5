# programme fait par Marc-Aurèle Béland
# groupe 406
# Introduction à la librairie Arcade

import arcade

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.width = width
        self.height = height

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        arcade.draw.draw_circle_filled(1100, 670, 100, arcade.color.ORANGE_PEEL, num_segments=10)
        arcade.draw.draw_circle_filled(1100, 670, 80, arcade.color.YELLOW,)
        y = self.height / 2 + 40
        arcade.draw.draw_triangle_filled(250, y + 130, -100, y - 450, 550, y - 450, arcade.color.DIM_GRAY)
        y = self.height / 2 + 40
        arcade.draw.draw_triangle_filled(1000, y + 250, 600, y - 450, 1500, y - 450, arcade.color.GRAY_ASPARAGUS)
        y = self.height / 2 + 40
        arcade.draw.draw_triangle_filled(600, y + 40, 300, y - 450, 900, y - 450, arcade.color.DARK_SLATE_GRAY)
        arcade.draw.draw_arc_filled(600, self._height / 2 + 20, 74, 120, arcade.csscolor.WHITE, 0, 180)
        points = [(250, 600), (148, 400), (338, 400)]
        arcade.draw.draw_polygon_filled(points, arcade.color.SNOW)
        arcade.draw.draw_lrbt_rectangle_filled(0, 1200, 0, 150, arcade.color.GREEN)
        arcade.draw.draw_line(450,  600, 1200, 700, arcade.color.DARK_ORANGE, 10)
        arcade.draw.draw_ellipse_filled(450, 600, 10, 20, arcade.color.DARK_ORANGE, -10)
        affichage = arcade.Text("Paysage de montagne.", 200, 700, arcade.color.BARBIE_PINK)
        affichage.draw()


def main():
    window = MyGame(1200, 800, "Mon dessin d'une montagne")
    arcade.run()


main()
