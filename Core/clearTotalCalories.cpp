#include <stdio.h>
#define TotalCalories "InOut\\TotalCalories.txt"

int main(){
    FILE *f = fopen(TotalCalories,"w");
    fprintf(f,"");
    fclose(f);
    return 0;
}

 
