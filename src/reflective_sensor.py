import RPi.GPIO as GPIO
from rpi_pins import sensorPins as sPins

class ReflectiveSensor:
  """Class used for controlling and setting up the reflective sensors.
     Callback methods are used for interrupts.
  """
  def leftCloseCallback(self, channel):
    print("Left Close Sensor triggered")


  def leftFarCallback(self, channel):
    print("Left Far Sensor triggered")


  def centerCallback(self, channel):
    print("Center Sensor triggered")


  def rightFarCallback(self, channel):
    print("Right Far Sensor triggered")


  def rightCloseCallback(self, channel):
    print("Right Close Sensor triggered")


  def initSensorPins(self):
    """Initializing Pins used for the sensors.
        They are listed as inputs, digital data is being extracted from them.
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #pin setup input
    GPIO.setup(sPins.LEFT_CLOSE, GPIO.IN)
    GPIO.setup(sPins.LEFT_FAR, GPIO.IN)
    GPIO.setup(sPins.RIGHT_CLOSE, GPIO.IN)
    GPIO.setup(sPins.RIGHT_FAR, GPIO.IN)
    GPIO.setup(sPins.CENTER, GPIO.IN)

    #setting up interrupts
    GPIO.add_event_detect(sPins.LEFT_CLOSE, GPIO.RISING,
                          callback = self.leftCloseCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.LEFT_FAR, GPIO.RISING,
                          callback = self.leftFarCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.RIGHT_CLOSE, GPIO.RISING,
                          callback = self.rightCloseCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.RIGHT_FAR, GPIO.RISING,
                          callback = self.rightFarCallback, bouncetime = 20)
    GPIO.add_event_detect(sPins.CENTER, GPIO.RISING,
                          callback = self.centerCallback, bouncetime = 20)


  def getStatus(self, sensorPin):
    """Method getting status of reflective sensor

    Args:
        sensorPin (int): Pin of the sensor

    Returns:
        int : 1 when light gets reflected, 0 when nothing to reflect
    """
    sPin = int(sensorPin)
    GPIO.setup(sPin, GPIO.IN)
    print(GPIO.input(sPin))
    return GPIO.input(int(sensorPin))

def main():
  # #argument parser for debugging
  # parser = argparse.ArgumentParser()
  # parser.add_argument('sensorPin')
  # parser.add_argument(' ', action='store_true')
  # args = parser.parse_args()

  # #testing sensor
  RSensor = ReflectiveSensor()
  RSensor.initSensorPins()
  # if not args.sensorPin:
  #   args = parser.parse_args('sensorPin')
  #   RSensor.getStatus(args.sensorPin)
  while(1):
    pass

if __name__ == "__main__":
  main()
