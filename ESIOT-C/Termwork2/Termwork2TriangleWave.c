#include<at89c51ed2.H>
void main()
{
	unsigned char count;
	while(1)
	{
		for(count=0;count<255;count++)
		P0 = count;
		for(count=255;count>0;count--)
		P0 = count;
	}
}