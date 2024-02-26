/******************************************************************************
ADXL377_example.ino
Simple example for using the ADXL377 accelerometer breakout.
Jordan McConnell @ SparkFun Electronics
3 July 2014
https://github.com/sparkfun/ADXL377_Breakout

This example collects raw accelerometer data from the ADXL377 sensor using
analog reads and then converts it into common units (g's) and prints the
result to the Serial Monitor.

Developed/Tested with:
Arduino Uno
Arduino IDE 1.0.5

This code is beerware.
Distributed as-is; no warranty is given. 
******************************************************************************/

// Make sure these two variables are correct for your setup

int scale = 200; // 3 (±3g) for ADXL337, 200 (±200g) for ADXL377
boolean micro_is_5V = true; // Set to true if using a 5V microcontroller such as the Arduino Uno, false if using a 3.3V microcontroller, this affects the interpretation of the sensor data

int xRawMin = 512; //337.5?
int xRawMax = 512;
 
int yRawMin = 512;
int yRawMax = 512;
 
int zRawMin = 512;
int zRawMax = 512;

int counter = 0;

float maxX;
float maxY;
float maxZ;

unsigned long mytime;
void setup()
{
  // Initialize serial communication at 115200 baud
  Serial.begin(115200);
}

// Read, scale, and print accelerometer data
void loop()
{
  // Get raw accelerometer data for each axis
  int rawX = analogRead(A2);
  int rawY = analogRead(A1);
  int rawZ = analogRead(A0);
  mytime = millis();

  
  
  // Scale accelerometer ADC readings into common units
  // Scale map depends on if using a 5V or 3.3V microcontroller
  float scaledX, scaledY, scaledZ; // Scaled values for each axis
  if (micro_is_5V) // Microcontroller runs off 5V
  {
    scaledX = mapf(rawX, 0, 675, -scale, scale); // 3.3/5 * 1023 =~ 675
    scaledY = mapf(rawY, 0, 675, -scale, scale);
    scaledZ = mapf(rawZ, 0, 675, -scale, scale);
  }
  else // Microcontroller runs off 3.3V
  {
    scaledX = mapf(rawX, 0, 1023, -scale, scale);
    scaledY = mapf(rawY, 0, 1023, -scale, scale);
    scaledZ = mapf(rawZ, 0, 1023, -scale, scale);
  }
  
  // Print out raw X,Y,Z accelerometer readings
  //Serial.print("X: "); Serial.println(rawX);
  //Serial.print("Y: "); Serial.println(rawY);
  //Serial.print("Z: "); Serial.println(rawZ);
  //Serial.println();
  
  // Print out scaled X,Y,Z accelerometer readings
  //Serial.print("X: "); Serial.print(scaledX); Serial.println(" g");
  //Serial.print("Y: "); Serial.print(scaledY); Serial.println(" g");
  //Serial.print("Z: "); Serial.print(scaledZ); Serial.println(" g");
  //Serial.println();

  if (scaledX > maxX)
  {
   maxX = scaledX;
  }

    if (scaledY > maxY)
  {
   maxY = scaledY;
  }

    if (scaledZ > maxZ)
  {
   maxZ = scaledZ;
  }
    
  //Print data to Serial Monitor
  //Serial.print("X: "); Serial.print(maxX); Serial.println();
  //Serial.print("Y: "); Serial.print(maxY); Serial.println();
  //Serial.print("Z: "); Serial.print(maxZ); Serial.println();
  //Serial.println();

 //Print data to Serial Plotter
  //Serial.print(scaledX);
  //Serial.print("\t");
  //Serial.print(scaledY);
  //Serial.print("\t");
  //Serial.print(scaledZ);
  //Serial.println();
  
  
  // Print data to Python Code
  counter = counter + 1;
  //Serial.print(counter);
  //Serial.print(" ");
  Serial.print(scaledX);
  Serial.print(",");
  Serial.print(scaledY);
  Serial.print(",");
  Serial.print(scaledZ);
  Serial.print(",");
  Serial.print(mytime);
  Serial.println(",");
  delay(2); // Minimum delay of 2 milliseconds between sensor reads (500 Hz)
}



// Same functionality as Arduino's standard map function, except using floats
float mapf(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
