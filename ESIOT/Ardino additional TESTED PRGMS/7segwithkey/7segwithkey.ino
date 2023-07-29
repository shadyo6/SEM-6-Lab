/*
*  Example testing sketch to Display keypad values on Seven Segment display 
*  By pressing the key on key on keypad same value is displayed on both Seven segment displays
*
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
* Connect CN10 - CN5  //Connect the 4*4 keypad
* Connect CN2  - CN8  //Connect 7 Segment Display
*/
#include <ShiftRegister74HC595.h>
#include <Keypad.h>
const byte numRows= 4; //number of rows on the keypad
const byte numCols= 4; //number of columns on the keypad

//keymap defines the key pressed according to the row and columns just as appears on the keypad
char keymap[numRows][numCols]=
{
{'0', '4', '8', 'c'},
{'1', '5', '9', 'd'},
{'2', '6', 'a', 'e'},
{'3', '7', 'b', 'f'}
};

char hexvalues[6] = {B01011111, B01111100,B00111001,B01011110, B01111001,B01110001}; //Seve values from Characters 'a' to 'f'

ShiftRegister74HC595 sr (2,12,10,11); 
uint8_t  numberB[] = {B00111111, //0
                      B00000110, //1 
                      B01011011, //2
                      B01001111, //3 
                      B01100110, //4
                      B01101101, //5
                      B01111101, //6
                      B00000111, //7
                      B01111111, //8
                      B01101111  //9
                     };
byte colPins[numRows] = {2,3,4,5}; //Rows 0 to 3
byte rowPins[numCols]= {6,7,8,9}; //Columns 0 to 3

Keypad myKeypad= Keypad(makeKeymap(keymap), rowPins, colPins, numRows, numCols);

        void setup()
        {
          Serial.begin(9600);
        }

void loop() 
   {
          char keypressed = myKeypad.getKey();
          Serial.println("keypressed : "+String(keypressed));
          if (keypressed != NO_KEY)
            {
              Serial.print(keypressed);
              int i = keypressed - '0';
              if(i<10)
              {
              uint8_t pinValues[] = {numberB[i],numberB[i]};
              sr.setAll(pinValues); 
              delay(100);
              }
              else
              {
              i = keypressed - 'a';
              uint8_t pinValues[] = {hexvalues[i],hexvalues[i]};
              sr.setAll(pinValues); 
              delay(100);
              }
            }
    }
        
