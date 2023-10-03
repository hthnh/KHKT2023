#include <stdio.h>
#define WeeklyLog "InOut\\WeeklyLog.txt"

int main(){
    FILE *f = fopen(WeeklyLog,"w");
    fprintf(f," ");
    fclose(f);
    return 0;
}