//To interface 16x2 LCD with 8051 microcontroller
#include"at89C51ed2.h"
#include<intrins.h>

//Function Prototypes
void lcd_init(void);
void lcd_comm(void);
void lcd_data(void);

//Global variables
unsigned char arr1[16]={"GITCSE"};
unsigned char arr2[16]={"MICROCONTROLLER"};
unsigned char temp1,temp2;

void main(void)
{
	unsigned char i;
	AUXR=0x10;		//To access eternal RAM
	lcd_init();

	temp1 = 0x80;	//Command to display line 1st position
	lcd_comm();

	for(i=0;i<6;i++)
	{
		temp2 = arr1[i];
		lcd_data();
	}

	temp1 = 0xC0;	//Command to display line 1st position
	lcd_comm();

	for(i=0;i<15;i++)
	{
		temp2 = arr2[i];
		lcd_data();
	}
}