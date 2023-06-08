#include <stdio.h>

char WeeklyLog[100] = "InOut\\WeeklyLog.txt";

int main(){
    FILE *f = fopen(WeeklyLog,"w");
    fprintf(f,"");
    fclose(f);
    return 0;
}