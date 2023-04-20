#include "at89c51ed2.h"

void T1M1Delay();

void main()
{
	while(1)
	{
	 	P2 = 0x00;
		T1M1Delay();
		P2 = 0x10;
		T1M1Delay();
		P2 = 0x20;
		T1M1Delay();
		P2 = 0x30;
		T1M1Delay();
	}
}

void T1M1Delay()
{
	unsigned int i;
	for(i=0; i<5; i++)
	{
		TMOD = 0x10;	//Select timer1 in mode1
		TH1=0x4B; 		//Load TH1 with 0x4B
		TL1=0xFE;	    //Load TL1 with 0xFE
		TR1=1;
		while(TF1 == 0);//Monitor overflow flag
		TR1=0;			//Stop the timer
		TF1=0;			//Clear overflow flag
	}
}
