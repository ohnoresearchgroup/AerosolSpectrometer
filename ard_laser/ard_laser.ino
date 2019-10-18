int PIN = 13;

void setup() {
  // set the baud rate
  Serial.begin(9600); 

  // set the output pin
  pinMode(PIN,OUTPUT);
  digitalWrite(PIN,LOW);
}

void loop() {
  char inByte = ' ';
  if(Serial.available()){ 
    char inByte = Serial.read(); // read the incoming data

    if (inByte == 'N'){
      digitalWrite(PIN,HIGH);
      Serial.println("on");
    }

    if (inByte == 'F'){
      digitalWrite(PIN,LOW);
      Serial.println("off");
    }

    if (inByte == 'C') {
      Serial.println("good");
    }
  }
  delay(50); // delay for 1/10 of a second
}
