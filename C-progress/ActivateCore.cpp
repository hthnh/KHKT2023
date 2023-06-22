#include <time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char day[10]; 
char date[10]; 
char conditionActivateFile[50] = "InOut\\conditionActivate.txt";
char conditionDailyMenu[10];
char conditionClearLog[10];
char Monday[10] = "Monday";


void findTime(){ 
    time_t timer; 
    struct tm* tm_info;  

    time(&timer); 
    tm_info = localtime(&timer); 

    strftime(day, 10, "%A", tm_info); 
    strftime(date, 10, "%x", tm_info); 

}

int main(){

    FILE *f = fopen(conditionActivateFile, "r");

    fscanf(f,"%s", &conditionDailyMenu);
    fscanf(f,"%s", &conditionClearLog);
    
    fclose(f);

    findTime();

    f= fopen(conditionActivateFile, "w");

    if(strcmp(day,Monday) == 0)
        if(strcmp(conditionDailyMenu, date) != 0){
            fprintf(f,"%s", date);
            system("FilterFood.exe");
            system("DailyMenu.exe");

        }


    fclose(f);


    
}