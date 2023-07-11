#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define WeeklyLog "InOut\\WeeklyLog.txt"
#define FoodAfterFilter "InOut\\FoodAfterFilter.txt"
#define caloriesIN "InOut\\TotalCalories.txt"
#define DailyFood "InOut\\DailyFood.txt"
#define cantfind "can't find any food"


int numberOfFood = 0,numberOfPeople,chooseOfUser,calories,positiveLimit, negativeLimit;
char date[10];

struct Food{
    int ID;
    char Name[50];
    char TimeOfDay[4];
    int withRice;
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000];

// Struct for food of week Breakfast Lunch Dinner
struct Menu{
    char Name[50];
    float caloNeed;
};Menu B[7],L[7],D[7];




void importFood(){
    struct Temp{char temp[50];};Temp t[7];
    int i = 0,y = 0;
    FILE *fp = fopen(FoodAfterFilter,"r");
    char *line_buf = NULL;
    size_t line_buf_size = 0;
    ssize_t line_size;
    line_size = getline(&line_buf, &line_buf_size, fp);

    while (line_size >= 0)
    {
        do{
        i++;
        strcpy(t[i].temp,line_buf);
        line_size = getline(&line_buf, &line_buf_size, fp);
        }while(i<7);
        i = 0;
        F[y].ID = atoi(t[0].temp);
        strncpy(F[y].Name,t[1].temp,strlen(t[1].temp)-1);
        strncpy(F[y].TimeOfDay,t[2].temp,strlen(t[1].temp)-1);
        F[y].withRice = atoi(t[3].temp);
        strncpy(F[y].LastPick,t[4].temp,strlen(t[1].temp)-1);
        F[y].PickTime = atoi(t[5].temp);
        F[y].Calories = atoi(t[6].temp);
        y++;

    }
    free(line_buf);
    line_buf = NULL;

    fclose(fp);

}
    

void importCalories(){
    FILE *f = fopen(caloriesIN,"r");
    fscanf(f,"%d",&numberOfPeople);
    fscanf(f,"%d",&calories);
    fscanf(f,"%d",&chooseOfUser);
    calories+=1;
    calories = calories / numberOfPeople;
    fclose(f);
}

void findCaloNeed(){
    B[0].caloNeed = calories * 0.2;
    L[0].caloNeed = calories * 0.35;
    D[0].caloNeed = calories * 0.3;
    if(chooseOfUser == 2){
        positiveLimit = 0;
        negativeLimit = calories * 0.1;
    } else if(chooseOfUser == 1){
        positiveLimit = calories * 0.1; 
        negativeLimit = 0;
    } else if(chooseOfUser == 3){
        positiveLimit = calories * 0.05;
        negativeLimit = calories * 0.05;
    }
}


void findTime(){ 
    time_t timer; 
    struct tm* tm_info;  
    char day[3]; 
    char month[3]; 
    char year[5]; 
    char xet[2] = "/";

    time(&timer); 
    tm_info = localtime(&timer); 

    strftime(day, 3, "%d", tm_info); 
    strftime(month, 3, "%m", tm_info); 
    strftime(year, 5, "%Y", tm_info); 

    strcpy(date,strcat(day,xet));
    strcat(date,month);
    strcat(date,xet);
    strcat(date,year);

}
void updateLastPick(int i){
    strcpy(F[i].LastPick,date);
}

int updatePickTime(int i){
    return F[i].PickTime++;
}

void updateFoodLog(int i){
 FILE *f = fopen(WeeklyLog,"a");
 int j = 0;
    while (1){
        if( i == F[j].ID){
            updateLastPick(j);
            updatePickTime(j);
            fprintf(f,"\n%d\n%s\n%s\n%d\n%d\n%s\n%d",F[j].ID,F[j].Name,F[i].TimeOfDay,F[i].withRice,F[j].PickTime,F[j].LastPick,F[j].Calories);
            break;
        }
        j++;
    }
   fclose(f); 
}
void clearFood(int i){
    while(1){
        if(F[i+1].ID == 0) break;
        F[i].ID = F[i+1].ID;
        strcpy(F[i].Name,F[i+1].Name);
        strcpy(F[i].TimeOfDay,F[i+1].TimeOfDay);
        F[i].withRice = F[i+1].withRice;
        F[i].PickTime = F[i+1].PickTime;
        strcpy(F[i].LastPick,F[i+1].LastPick);
        F[i].Calories = F[i+1].Calories;
        i++;
    }
}
void CountFood(){
    while(1>0){
        if(F[numberOfFood].ID == 0) break;
        numberOfFood++;
    }
}







void Breakfast(){
    int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){ 
            if(strchr(F[j].TimeOfDay,'1') != NULL) 
                if( F[j].Calories <= B->caloNeed + positiveLimit ){
                    if (F[j].Calories >= B->caloNeed - negativeLimit){
                        updateFoodLog(F[j].ID);
                        strcpy(B[i].Name, F[j].Name);
                        clearFood(j);
                        break;
                    }
                } 
        }
    }
}

void Lunch(){
     int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){
            if(strchr(F[j].TimeOfDay,'2') != NULL) 
                if( F[j].Calories <= L->caloNeed + positiveLimit ){
                        if (F[j].Calories >= L->caloNeed - negativeLimit){
                        updateFoodLog(F[j].ID);
                        strcpy( L[i].Name, F[j].Name);
                        clearFood(j);
                        break;
                    }
                }
        }
    }
}

void Dinner(){
    int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){
            if(strchr(F[j].TimeOfDay,'3') != NULL) 
                if( F[j].Calories <= D->caloNeed + positiveLimit ){
                    if (F[j].Calories >= D->caloNeed - negativeLimit ){   
                    updateFoodLog(F[j].ID);
                    strcpy( D[i].Name, F[j].Name);
                    clearFood(j);
                    break;
                    }
                }
        }
    }
}


void Output(){
    int i;
    FILE *f = fopen(DailyFood,"w");
    for(i = 0; i<=6; i++){
        fprintf(f,"%s\n",B[i].Name);
    }
    for(i = 0; i<=6; i++){
        fprintf(f,"%s\n",L[i].Name);
    }
    for(i = 0; i<=6; i++){
        fprintf(f,"%s\n",D[i].Name);
    }
}

void check(){
    int i = 0;
    while(1){
        printf("%d",&F[i].ID);
        if(F[i].ID == 0 ) break;
        printf("%s",&F[i].Name);
        printf("%d",&F[i].PickTime);
        printf("%s",&F[i].LastPick);
        printf("%d",&F[i].Calories);
        i++;
    }  
}

int main(void){

importFood();
importCalories();
findCaloNeed();
findTime();
Breakfast();
Lunch();
Dinner();
Output();



}