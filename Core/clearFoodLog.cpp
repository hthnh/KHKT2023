#include <stdio.h>

char WeeklyLog[100] = "D:\\code\\KHKT-Order\\InOut\\WeeklyLog.txt";

int main(){
    FILE *f = fopen(WeeklyLog,"w");
    fprintf(f,"");
    fclose(f);
    return 0;
}