from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongGame(Widget):
    ball = ObjectProperty(None)
    p1 = ObjectProperty(None)
    p2 = ObjectProperty(None)

    
    def serve_ball(self):
        # as the name of the function suggest, it serves the ball on 
        # randomized directions when the game starts.
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        # the main purpose of this function is give the ability
        # of update the game screen to the computer. 
        self.ball.move()
        # bounce off paddles
        self.p1.bounce_ball(self.ball)
        self.p2.bounce_ball(self.ball)
        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # went off to a side to score point?
        if self.ball.x < self.x:
            self.p2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.p1.score += 1
            self.serve_ball(vel=(-4, 0))
    
    # input settings
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.p1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.p2.center_y = touch.y
        


class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property from kivy.properties so we can use ball.velocity as a shorthand, 
    # just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # adding movement vector using Vector function (imported from kivy.vector)
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
    
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()

        # this line updates the game 60 times per second which means
        #  our game's FPS is 60.
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
    
if __name__ == '__main__':
    PongApp().run()
