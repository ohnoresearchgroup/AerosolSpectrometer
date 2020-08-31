int PINhiRef = 13;
int PINpumpControl = 12;

int PINvalve5 = 5;
int PINvalve6 = 6;

void setup() {
  // set the baud rate
  Serial.begin(9600); 

  // set the output pin
  pinMode(PINhiRef,OUTPUT);
  pinMode(PINpumpControl,OUTPUT);
  pinMode(PINvalve5,OUTPUT);
  pinMode(PINvalve6,OUTPUT);
  
  digitalWrite(PINhiRef,HIGH);
  digitalWrite(PINpumpControl,LOW);
  digitalWrite(PINvalve5,HIGH);
  digitalWrite(PINvalve6,HIGH);

}

void loop() {
  char inByte = ' ';
  if(Serial.available()){ 
    char inByte = Serial.read(); // read the incoming data

    if (inByte == 'A'){
      digitalWrite(PINpumpControl,HIGH);
      Serial.println("pumpon");
    }

    if (inByte == 'B'){
      digitalWrite(PINpumpControl,LOW);
      Serial.println("pumpoff");
    }

    if (inByte == 'C') {
      Serial.println("good");
    }

    if (inByte == 'D'){
      digitalWrite(PINvalve5,LOW);
      Serial.println("atomon");
    }
    if (inByte == 'E'){
      digitalWrite(PINvalve5,HIGH);
      Serial.println("atomoff");
    }

    if (inByte == 'F'){
      digitalWrite(PINvalve6,LOW);
      Serial.println("cellparton");
    }
    if (inByte == 'G'){
      digitalWrite(PINvalve6,HIGH);
      Serial.println("cellpartoff");
    }
    
  }
  else {
    delay(50); // delay for 1/10 of a second
  }
}
