#include <stdio.h>
#include <string.h>

#define BUFF_LEN 0x40

// flag - riftCTF{tr4c1ng-mAkes-17-SUPeR-345Y}

int main(){

	char buff[BUFF_LEN];
	printf("--=[ Super Easy Crackme ]=--\n");
	printf("passwd > ");
	fgets(buff, BUFF_LEN, stdin);

	if(!strncmp(buff, "riftCTF{tr4c1ng-mAkes-17-SUPeR-345Y}", 36)){
		puts("Correct Password...");
	} else {
		puts("Wrong Password...");
	}

	return 0;
}