#include <time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char day[10]; 
char date[10]; 
char conditionActivateFile[50] = "InOut\\conditionActivate.txt";
char conditionDailyMenu[10];
int conditionClearLog;
char Monday[10] = "Saturday";


void findTime(){ 
    time_t timer; 
    struct tm* tm_info;  

    time(&timer); 
    tm_info = localtime(&timer); 

    strftime(day, 10, "%A", tm_info); 
    strftime(date, 10, "%x", tm_info); 


}
void countDay(){
    if(strcmp(day,Monday) == 0){
        if(conditionClearLog <=1){
            conditionClearLog++;
        }
    }
}


int main(){

    FILE *f = fopen(conditionActivateFile, "r");

    fscanf(f,"%s", &conditionDailyMenu);
    fscanf(f,"%d", &conditionClearLog);
    
    fclose(f);

    findTime();
    countDay();


    if(strcmp(day,Monday) == 0)
        if(strcmp(conditionDailyMenu, date) != 0){
            f= fopen(conditionActivateFile, "w");
            fprintf(f,"%s\n", date);
            system("FilterFood.exe");
            system("DailyMenu.exe");
            if(conditionClearLog != 2){
                fprintf(f,"%d",conditionClearLog);
            }
            if(conditionClearLog == 2){
                conditionClearLog =0;
                fprintf(f,"%d",conditionClearLog);
                system("clearFoodLog.exe");
            }
        }

    fclose(f);

    
}