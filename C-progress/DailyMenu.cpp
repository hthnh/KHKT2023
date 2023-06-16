#include <stdio.h>
#include <string.h>
#include <time.h>



char WeeklyLog[100] = "InOut\\WeeklyLog.txt";
char FoodAfterFilter[100] = "InOut\\FoodAfterFilter.txt";
char caloriesIN[50] = "InOut\\TotalCalories.txt";
int numberOfPeople;
int calories;
int numberOfFood = 0;
int chooseOfUser;
int positiveLimit, negativeLimit;
char cantfind[20] = "can't find any food";
char date[10];

struct Food{
    int ID;
    char Name[50];
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000];



struct Breakfast{
    char Name[50];
    float caloNeed;
};Breakfast B[7];

struct Lunch{
    char Name[50];
    float caloNeed;
};Lunch L[7];

struct Dinner{
    char Name[50];
    float caloNeed;
};Dinner D[7];


void importFood(){
    FILE *f = fopen(FoodAfterFilter,"r");
    int i = 0;
    while(1){
        fscanf(f,"%d",&F[i].ID);
        if(F[i].ID == 0 ) break;
        fscanf(f,"%s",&F[i].Name);
        fscanf(f,"%d",&F[i].PickTime);
        fscanf(f,"%s",&F[i].LastPick);
        fscanf(f,"%d",&F[i].Calories);
        i++;
    }  
    fclose(f);
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
    L[0].caloNeed = calories * 0.5;
    D[0].caloNeed = calories * 0.3;
    if(chooseOfUser == 0){
        positiveLimit = 0;
        negativeLimit = calories * 0.1;
    } else if(chooseOfUser == 1){
        positiveLimit = calories * 0.1; 
        negativeLimit = 0;
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
    findTime();
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
            fprintf(f,"\n%d\n%s\n%d\n%s\n%d",F[j].ID,F[j].Name,F[j].PickTime,F[j].LastPick,F[j].Calories);
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







void BFast(){
    int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){  
            if( F[j].Calories <= B->caloNeed + positiveLimit ){
                strcpy(B[i].Name,cantfind);
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

void LNch(){
     int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){
            strcpy( L[i].Name,cantfind); 
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

void DNer(){
    int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){
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

void check(){
    int i = 0;
    printf("%d\n",calories);
    printf(" B:%.2f L:%.2f D:%.2f chenh lech cho phep %d %d",B[0].caloNeed,L[0].caloNeed,D[0].caloNeed, positiveLimit , negativeLimit);
    printf(" %s", date);
    for(i = 0; i<=6; i++){
        printf("\n%s",B[i].Name);
    }
    printf(" \n");
    for(i = 0; i<=6; i++){
        printf("\n%s",L[i].Name);
    }
    printf(" \n");
    for(i = 0; i<=6; i++){
        printf("\n%s",D[i].Name);
    }
}

int main(){

importFood();

importCalories();
findCaloNeed();
findTime();
CountFood();
BFast();
LNch();
DNer();
check();




}