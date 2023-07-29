        #include <ShiftRegister74HC595.h>
        // CREATE SHIFT REGISTER OBJECT (NUMBER OF SHIFT REGISTERS, DATA PIN, CLOCK PIN, LATCH PIN)
        // CONNECT CN2 to CN8
        ShiftRegister74HC595 sr (2, 12,10,11); 
        uint8_t  numberB[] = {B00111111, //0
                      B00000110, //1 
                      B01011011, //2
                      B01001111, //3 
                      B01100110, //4
                      B01101101, //5
                      B01111101, //6
                      B00000111, //7
                      B01111111, //8
                      B01101111 //9
                     };

        void setup()
        {
          
        }

        void loop() 
        {
         for(int i=0;i<10;i++)
         {
          for (int j = 0; j < 10; j++) 
          {
            uint8_t pinValues[] = {numberB[i],numberB[j]};
            sr.setAll(pinValues); 
            delay(1000); 
          }
         }
        }
        
