import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.draw_circle_filled(100, 500, 50, arcade.color.LIGHT_YELLOW)
    arcade.draw_circle_filled(170, 550, 100, arcade.color.DARK_BLUE)



def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

    # Draw Nose
    arcade.draw_circle_filled(x, 190 + y, 8, arcade.color.ORANGE)

    #Draw Hat
    arcade.draw_lrtb_rectangle_filled(x - 50, x + 50, 250 + y,230 + y, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(x - 30, x + 30, 280 + y,230 + y, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(x - 30, x + 30, 260 + y,250 + y, arcade.color.GRAY)

    #Draw Buttons
    arcade.draw_circle_filled(x, 150 + y, 8, arcade.color.BLACK)
def draw_snow_person_1(x, y):
    """ Draw another snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x - 100, y, arcade.color.BLACK, 5)

    # Snow
    arcade.draw_circle_filled(x - 100, 30 + y, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 100, 70 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 100, 100 + y, 20, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 107.5, 105 + y, 2.5, arcade.color.BLACK)
    arcade.draw_circle_filled(x - 92.5, 105 + y, 2.5, arcade.color.BLACK)

    # Draw Nose
    arcade.draw_circle_filled(x -100 , y + 100, 4, arcade.color.ORANGE)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)

    draw_snow_person_1(on_draw.snow_person1_x, 70)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 1


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150







# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/100)
    arcade.run()

main()