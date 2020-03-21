#include <stdio.h>
#include <string.h>

#define BUFF_LEN 0x40

// flag riftCTF{tr4cing_d03snt_w0rk_anyM0r33}

int strncmp_my(const char * a, const char *b, int len){

	int m = 0;
	for(int i = 0; (i < len) && (a[i] != '\x00') && (b[i] != '\x00'); i++){
		m |= a[i] ^ 0x55 ^ b[i];
	}

	return m;
}


int main(){

	char buff[BUFF_LEN];
	printf("--=[ Not So Easy Crackme ]=--\n");
	printf("passwd > ");
	fgets(buff, BUFF_LEN, stdin);

	if(!strncmp_my(buff, "\x27\x3c\x33\x21\x16\x1\x13\x2e\x21\x27\x61\x36\x3c\x3b\x32\xa\x31\x65\x66\x26\x3b\x21\xa\x22\x65\x27\x3e\xa\x34\x3b\x2c\x18\x65\x27\x66\x66\x28", 37)){
		puts("Correct Password...");
	} else {
		puts("Wrong Password...");
	}

	return 0;
}