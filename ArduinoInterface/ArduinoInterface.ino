#include <Stepper.h>
int FourPin = 12;
int FivePin = 11;
int SixPin = 10;
int SevenPin = 9;

double lastMotor1 = 0;
double lastMotor2 = 0;
     
Stepper motor1(512, FourPin, FivePin, SixPin, SevenPin); 

void setup(void)
{
  //Begin Serial
  Serial.begin(115200);
  pinMode(FourPin, OUTPUT);
  pinMode(FivePin, OUTPUT);
  pinMode(SixPin, OUTPUT);
  pinMode(SevenPin, OUTPUT);
     
  // this line is for Leonardo's, it delays the serial interface
  // until the terminal window is opened
  while (!Serial);
      
    Serial.begin(9600);
    motor.setSpeed(20);

  delay(5000);
  
  Serial.println("A");
}



void loop() {
   delay(10); //This is the minimum delay that removes data errors + 3ms for good measure. This will likely change with hardware and needs to be adjusted. 
  
   if(Serial.available() > 0) {
        char receivedChars[256];
        Serial.readBytes(receivedChars, Serial.available());
  
        char* commands = strtok(receivedChars, ",");

        double motor1 = strtod(commands, NULL);
        commands = strtok (NULL, " ,.-");
  
        double motor2 = strtod(commands, NULL);
        commands = strtok (NULL, " ,.-");

        if(motor1 != lastMotor1) {
            motor1.step(motor1);
            lastMotor1 = motor1
        }

        if(motor2 != lastMotor2) {
          lastMotor2 = motor2;
        }
    
        //Diplay data
        Serial.print(getSensorData());
        Serial.print(",");
  
        Serial.println("");
    }
}

int getSensorData() {
  return 2;
}
