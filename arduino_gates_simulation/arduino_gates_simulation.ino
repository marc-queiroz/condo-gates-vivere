/*
  Button

  Turns on and off a light emitting diode(LED) connected to digital pin 13,
  when pressing a pushbutton attached to pin 2.

  The circuit:
  - LED attached from pin 13 to ground through 220 ohm resistor
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.

  created 2005
  by DojoDave <http://www.0j0.org>
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Button
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin0 = 2;     // the number of the pushbutton pin
const int buttonPin1 = 3;
const int ledPin0 = 13;      // the number of the LED pin
const int ledPin1 = 12;
const long interval = 12000;
unsigned long previousMillis0 = 0;
unsigned long previousMillis1 = 0;

// variables will change:
int button0State = 0;         // variable for reading the pushbutton status
int button1State = 0;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin0, OUTPUT);
  pinMode(ledPin1, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin0, INPUT);
  pinMode(buttonPin0, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  button0State = digitalRead(buttonPin0);
  button1State = digitalRead(buttonPin1);

  unsigned long currentMillis = millis();
  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (button0State == HIGH) {
    // turn LED on:
    digitalWrite(ledPin0, HIGH);
    previousMillis0 = currentMillis;
  }

  if (button1State == HIGH) {
    // turn LED on:
    digitalWrite(ledPin1, HIGH);
    previousMillis1 = currentMillis;
  }

  if (currentMillis - previousMillis0 > interval) {
    // turn LED off:
    digitalWrite(ledPin0, LOW);
  }

  if (currentMillis - previousMillis1 > interval) {
    // turn LED off:
    digitalWrite(ledPin1, LOW);
  }
}
