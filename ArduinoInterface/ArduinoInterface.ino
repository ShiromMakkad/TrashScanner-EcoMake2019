void setup(void)
{
  //Begin Serial
  Serial.begin(115200);

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

        //Set motor power
    
        //Diplay data
        Serial.print(getSensorData());
        Serial.print(",");
  
        Serial.println("");
    }
}

int getSensorData() {
  return 2;
}
