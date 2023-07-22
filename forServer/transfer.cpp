#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "cJson.c"
#include "cJson.h"
int y = 0;

#define AllFood "AllFood.txt"
#define OutFood "AllFood.json"



struct Food{
    int ID;
    char Name[50];
    char TimeOfDay[4];
    int withRice;
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000];



void importFood(){
    struct Temp{char temp[50];};Temp t[7];
    int i = 0;
    FILE *fp = fopen(AllFood,"r");
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

void Out(){
    cJSON *data = NULL;
    cJSON *foods = NULL;
    cJSON *food = NULL;
    cJSON *ID = NULL;
    cJSON *Name = NULL;
    cJSON *TimeOfDay = NULL;
    cJSON *withRice = NULL;
    cJSON *PickTime = NULL;
    cJSON *LastPick = NULL;
    cJSON *Calories = NULL;

    data = cJSON_CreateObject();

    foods = cJSON_CreateArray();
    cJSON_AddItemToObject(data,"Food",foods);

    
    for(int i = 0; i <= y; i++){
        food = cJSON_CreateObject();
        cJSON_AddItemToArray(foods,food);
        ID = cJSON_CreateNumber(F[i].ID);
        cJSON_AddItemToObject(food,"ID",ID);
        Name = cJSON_CreateString(F[i].Name);
        cJSON_AddItemToObject(food,"Name",Name);
        TimeOfDay = cJSON_CreateString(F[i].TimeOfDay);
        cJSON_AddItemToObject(food,"TimeOfDay",TimeOfDay);
        withRice = cJSON_CreateNumber(F[i].withRice);
        cJSON_AddItemToObject(food,"withRice",withRice);
        PickTime = cJSON_CreateNumber(F[i].PickTime);
        cJSON_AddItemToObject(food,"PickTime",PickTime);
        LastPick = cJSON_CreateString(F[i].LastPick);
        cJSON_AddItemToObject(food,"LastPick",LastPick);
        Calories = cJSON_CreateNumber(F[i].Calories);
        cJSON_AddItemToObject(food,"Calories",Calories);
    }

    char *json_str = cJSON_Print(data);

    FILE *f = fopen(OutFood,"w");
    fputs(json_str,f);
    fclose(f);
    cJSON_free(json_str);
    cJSON_Delete(data);
}

int main() {

    importFood();
    Out();

    return 0;

    
}