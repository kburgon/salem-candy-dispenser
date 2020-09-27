const int buttonPin = 2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  if (digitalRead(buttonPin) == HIGH)
  {
    Serial.println(2);
  }
  else
  {
    Serial.println(1);
  }

  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);
}
