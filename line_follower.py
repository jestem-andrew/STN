from gamepad_control import GamepadControl
from motor_driver import MotorDriver
import RPi.GPIO as GPIO

from inputs import get_gamepad
from inputs import devices


class LineFollower:
  """Main class used for controlling the line follower.
  """
  def useGamePad(self):
    MotorDriver.goDirection(GamepadControl.getGamepadDirection())



if __name__ == "main":
  LineFollower.useGamePad()
