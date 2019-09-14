void setup ()
{
  DDRD |= 4 ; // pin 2 set to output - 4 == 1<<2
}

void loop ()
{
  PIND = 4 ;  // toggle pin 2 with 1 instruction
  PIND = 4 ;  // toggle pin 2 with 1 instruction
  delayMicroseconds (5000) ;
}
