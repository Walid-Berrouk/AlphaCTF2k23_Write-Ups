#include<stdio.h>


void win(){
    system("/bin/sh");
}

void init() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

void main(){
    char input[32];
    init();
    printf("[X] BOF:");
    scanf("%s",input);
    puts("???");
}