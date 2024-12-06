from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

#class PongBall(Widget):

    # velocity of the ball on x and y axis
    #vel_x = NumericProperty(0)
    #vel_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as a shorthand, 
    # just like e.g. w.pos for w.x and w.y

    



class PongApp(App):
    def build(self):
        return PongGame()
    
if __name__ == '__main__':
    PongApp().run()
