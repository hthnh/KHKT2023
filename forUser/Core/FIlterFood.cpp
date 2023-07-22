#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define AllFood "InOut\\AllFood.txt"
#define WeeklyLog "InOut\\WeeklyLog.txt"
#define FoodAfterFilter "InOut\\FoodAfterFilter.txt"
struct Food{
    int ID;
    char Name[50];
    char TimeOfDay[3]; 
    int withRice;
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000],FF[100];

void importFood(){
    struct Temp{char temp[50];};Temp t[7];
    int i = 0,y = 0;
    FILE *fp = fopen(AllFood,"r");
    if( feof(fp) ) return;
    char *line_buf = NULL;
    size_t line_buf_size = 0;
    ssize_t line_size;
    line_size = getline(&line_buf, &line_buf_size, fp);

    while (line_size >= 0)
    {
        do{
        strcpy(t[i].temp,line_buf);
        line_size = getline(&line_buf, &line_buf_size, fp);
        i++;
        }while(i<7);
        i = 0;
        F[y].ID = atoi(t[0].temp);
        strncpy(F[y].Name,t[1].temp,strlen(t[1].temp)-1);
        strncpy(F[y].TimeOfDay,t[2].temp,strlen(t[2].temp)-1);
        F[y].withRice = atoi(t[3].temp);
        strncpy(F[y].LastPick,t[4].temp,strlen(t[4].temp)-1);
        F[y].PickTime = atoi(t[5].temp);
        F[y].Calories = atoi(t[6].temp);
        y++;

    }
    free(line_buf);
    line_buf = NULL;

    fclose(fp);

}

void importFoodLog(){
    FILE *fp = fopen(WeeklyLog,"r");
    if( feof(fp) ) return;
    struct Temp{char temp[50];};Temp t[7];
    int i = 0,y = 0;
    char *line_buf = NULL;
    size_t line_buf_size = 0;
    ssize_t line_size;
    line_size = getline(&line_buf, &line_buf_size, fp);

    while (line_size >= 0)
    {
        do{
        strcpy(t[i].temp,line_buf);
        line_size = getline(&line_buf, &line_buf_size, fp);
        i++;
        }while(i<7);
        i = 0;
        FF[y].ID = atoi(t[0].temp);
        strncpy(FF[y].Name,t[1].temp,strlen(t[1].temp)-1);
        strncpy(FF[y].TimeOfDay,t[2].temp,strlen(t[2].temp)-1);
        FF[y].withRice = atoi(t[3].temp);
        strncpy(FF[y].LastPick,t[4].temp,strlen(t[4].temp)-1);
        FF[y].PickTime = atoi(t[5].temp);
        FF[y].Calories = atoi(t[6].temp);
        y++;

    }
    free(line_buf);
    line_buf = NULL;

    fclose(fp);
}
void clearFood(int i){
    while(1){
        F[i].ID = F[i+1].ID;
        strcpy(F[i].Name,F[i+1].Name);
        strcpy(F[i].TimeOfDay,F[i+1].TimeOfDay);
        F[i].withRice = F[i+1].withRice;
        F[i].PickTime = F[i+1].PickTime;
        strcpy(F[i].LastPick,F[i+1].LastPick);
        F[i].Calories = F[i+1].Calories;
        if(F[i+1].ID == 0) break;
        i++;
    }
}


void OutFood(){
    FILE *file = fopen(FoodAfterFilter,"w");
    int i = 0;
    while(1){
        fprintf(file,"%d\n%s\n%s\n%d\n%d\n%s\n%d\n",F[i].ID,F[i].Name,F[i].TimeOfDay,F[i].withRice,F[i].PickTime,F[i].LastPick,F[i].Calories );
        i++;
        if(F[i].ID == 0)break;
    }
    fclose(file);
}







int main(){
    importFood();
    importFoodLog();

    int i = 0;
    int y = 0;
    while(1){
            y = 0;
        while(1){
            if (F[i].ID == FF[y].ID){
                clearFood(i);
            }
            
            if(F[y].ID == 0) break;
            y++;
        }
        if(F[i].ID == 0) break;
        i++;
    }
    
    OutFood();


    return 0;
}
