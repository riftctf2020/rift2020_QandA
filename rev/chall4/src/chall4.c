#include <stdio.h>
#include <string.h>

#define BUFF_LEN 0x40

// flag - riftCTF{---=[Did_Y0U_kN0W_YoU_CoU1D_ActuallY_FinD_ThE_FlaG_1n_m3M0rY]=--}

int strncmp_my(const char * a, const char *b, int len){

	int m = 0;
	for(int i = 0; (i < len) && (a[i] != '\x00') && (b[i] != '\x00'); i++){
		m |= a[i] ^ b[i];
	}

	return m;
}


int main(){

	char buff[BUFF_LEN];
	printf("--=[ Very Hard Crackme ]=--\n");
	printf("passwd > ");
	fgets(buff, BUFF_LEN, stdin);

	unsigned char s[] = 
	{

	    0x6e, 0xf0, 0xec, 0x02, 0x6b, 0x24, 0xb1, 0x31, 
	    0x06, 0xeb, 0x57, 0xf6, 0x5f, 0x90, 0x15, 0xe6, 
	    0x1a, 0x15, 0x93, 0x1f, 0xba, 0x43, 0xd7, 0x3a, 
	    0xd2, 0x80, 0x7a, 0x0c, 0xab, 0xcc, 0x0a, 0xfa, 
	    0x93, 0xdd, 0xe8, 0x96, 0xa7, 0x75, 0xe9, 0x1d, 
	    0xfc, 0x68, 0x7d, 0x01, 0x54, 0x96, 0x5a, 0x85, 
	    0xcf, 0xd2, 0xc8, 0x9f, 0xed, 0x1c, 0x6a, 0x29, 
	    0xda, 0xd1, 0x30, 0x82, 0x7d, 0x82, 0xf1, 0xeb, 
	    0xe0, 0x24, 0x15, 0x6d, 0x32, 0x30, 0x87, 0x28, 
	    0x5c, 0x85
	};

	for (unsigned int m = 0; m < sizeof(s); ++m)
	{
	    unsigned char c = s[m];
	    c = (c >> 0x3) | (c << 0x5);
	    c += 0x63;
	    c ^= m;
	    c = ~c;
	    c = -c;
	    c = ~c;
	    c = (c >> 0x1) | (c << 0x7);
	    c = ~c;
	    c = -c;
	    c ^= 0x39;
	    c -= 0x40;
	    c ^= 0x48;
	    c = -c;
	    c -= m;
	    c ^= m;
	    c += 0x98;
	    c ^= 0xf3;
	    c = ~c;
	    c ^= m;
	    c -= m;
	    c ^= m;
	    c = (c >> 0x2) | (c << 0x6);
	    c -= m;
	    c = ~c;
	    c ^= 0x42;
	    c = ~c;
	    c = (c >> 0x7) | (c << 0x1);
	    c -= 0x12;
	    c ^= 0x26;
	    c -= m;
	    c ^= m;
	    c -= 0xe1;
	    c = -c;
	    c = ~c;
	    c = (c >> 0x1) | (c << 0x7);
	    c ^= 0x99;
	    c = -c;
	    c ^= m;
	    c += m;
	    c ^= m;
	    c = -c;
	    c -= m;
	    c ^= 0x83;
	    c += m;
	    c ^= 0x2b;
	    c += m;
	    c = ~c;
	    c ^= 0x62;
	    c += 0xdb;
	    c = (c >> 0x1) | (c << 0x7);
	    s[m] = c;
	}


	if(!strncmp_my(buff, s, strlen(s))){
		puts("Correct Password...");
	} else {
		puts("Wrong Password...");
	}

	return 0;
}