const int buttonPin = 6;

bool sendMsg = true;
String results = "1";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  // If sendMsg == false, then the pi is playing a sound byte.  Don't check for a trigger.
  if (sendMsg)
  {
    if (digitalRead(buttonPin) == HIGH)
    {
      Serial.println(2);
      digitalWrite(LED_BUILTIN, HIGH);
      sendMsg = false;
    }
    else
    {
      Serial.println(1);
    }
  }

  // Try to read a heartbeat from the pi.
  if (Serial.available())
  {
    // If the pi sends a "1", then it is not playing a sound byte anymore and is ready to play another.
    results = Serial.readString();
    if (results == "1")
    {
      sendMsg = true;
    }
  }

  // The delay is mostly meant for testing purposes.
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);
}
