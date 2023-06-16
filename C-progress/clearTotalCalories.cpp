#include <stdio.h>
char TotalCalories[100] = "InOut\\TotalCalories.txt";

int main(){
    FILE *f = fopen(TotalCalories,"w");
    fprintf(f,"");
    fclose(f);
    return 0;
}

 
