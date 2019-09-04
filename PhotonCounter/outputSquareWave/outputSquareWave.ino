void setup()
{ 
  DDRB = DDRB | B110000; // Set digital pins 12 and 13 to outputs

}

void loop()
{  
  int T = 50;
  PORTB = B100000;         // Digital pin 13 high
  delayMicroseconds(T);  //30 microsecond delay
  PORTB = B000000;        // Digital pin 13 low 
  delayMicroseconds(T);   //30 microsecond delay   
}
