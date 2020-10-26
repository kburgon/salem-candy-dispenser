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
  // put your main code here, to run repeatedly:
  // digitalWrite(LED_BUILTIN, HIGH);
  if (sendMsg)
  {
    if (digitalRead(buttonPin) == HIGH)
    {
      Serial.println(2);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else
    {
      Serial.println(1);
    }
  }

  if (Serial.available())
  {
    results = Serial.readString();
    if (results == "2" || sendMsg == true)
    {
      sendMsg = false;
    }
    else
    {
      sendMsg = true;
    }
  }

  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  results = "1";
  delay(100);
}
