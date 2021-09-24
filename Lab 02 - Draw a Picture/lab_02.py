import arcade.csscolor
arcade.open_window(600,600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
#DRAW BODY OF PENCIL
arcade.draw_lrtb_rectangle_filled(75,525,350,300, arcade.csscolor.YELLOW)

#DRAW THE TIP OF THE PENCIL
arcade.draw_triangle_filled(525,350, 525,300, 560, 325, arcade.csscolor.SANDY_BROWN)
arcade.draw_triangle_filled(540,338, 540,312, 560, 325, arcade.csscolor.BLACK)

#DRAWING LINES ON THE PENCIL
arcade.draw_line(75,340,525,340, arcade.csscolor.SANDY_BROWN)
arcade.draw_line(75,330,525,330, arcade.csscolor.SANDY_BROWN)
arcade.draw_line(75,320,525,320, arcade.csscolor.SANDY_BROWN)
arcade.draw_line(75,310,525,310, arcade.csscolor.SANDY_BROWN)

#DRAWS PENCIL ERASER
arcade.draw_lrtb_rectangle_filled(75, 80, 350, 300, arcade.csscolor.DARK_GREEN)
arcade.draw_lrtb_rectangle_filled(85, 100, 350, 300, arcade.csscolor.DARK_GREEN)
arcade.draw_arc_filled(75, 325, 50, 50, arcade.csscolor.PINK, 90, 270)

#DRAWS ERASER
arcade.draw_lrtb_rectangle_filled(350, 550, 250, 150, arcade.csscolor.DARK_BLUE)
arcade.draw_lrtb_rectangle_filled(350, 550, 200, 195, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(350, 550, 175, 150, arcade.csscolor.BLACK)
arcade.draw_arc_filled(350, 200, 100, 100, arcade.csscolor.WHITE, 90, 270)
arcade.draw_text("ERASER", 350, 150, arcade.csscolor.WHITE, 35, 200)

#DRAWS PEN
arcade.draw_lrtb_rectangle_filled(200, 500, 450, 425, arcade.csscolor.BLACK)
arcade.draw_arc_filled(200, 438, 250, 25, arcade.csscolor.BLACK, 90, 270)
arcade.draw_lrtb_rectangle_filled(205, 210, 450, 425, arcade.csscolor.GOLD)
#TIP OF THE PEN
arcade.draw_triangle_filled(500,450, 500,425, 550, 438, arcade.csscolor.GOLD)
arcade.draw_triangle_filled(540,450, 540,425, 550, 438, arcade.csscolor.SKY_BLUE)

arcade.finish_render()
arcade.run()