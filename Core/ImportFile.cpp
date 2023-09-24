#include <stdio.h>

int main(){
    FILE *f;
    f = fopen("InOut\\AllFood.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\conditionActivate.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\DailyFood.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\deleteID.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\FoodAfterFilter.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\heightWeight.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\IDfood.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\TotalCalories.txt","w");
    fprintf(f,"");
    fclose(f);
    f = fopen("InOut\\WeeklyLog.txt","w");
    fprintf(f," ");
    fclose(f);
}