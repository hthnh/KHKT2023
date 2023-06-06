#include <stdio.h>
#include <string.h>
#include <time.h>



char WeeklyLog[100] = "D:\\code\\KHKT-Order\\InOut\\WeeklyLog.txt";
char FoodAfterFilter[100] = "D:\\code\\KHKT-Order\\InOut\\FoodAfterFilter.txt";
char caloriesIN[50] = "D:\\code\\KHKT-Order\\InOut\\TotalCalories.txt";
int numOfPeople;
int calories;
char date[20];

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
};Lunch L[5];

struct Dinner{
    char Name[50];
    float caloNeed;
};Dinner D[5];


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
    fscanf(f,"%d",&numOfPeople);
    fscanf(f,"%d",&calories);
    calories+=1;
    fclose(f);
}

void findCaloNeed(){
    B[0].caloNeed = calories * 0.2;
    L[0].caloNeed = calories * 0.5;
    D[0].caloNeed = calories * 0.3;
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

    char date2[20];
    strcpy(date2,strcat(day,xet));
    strcat(date2,month);
    strcat(date2,xet);
    strcat(date2,year);
    strcpy(date,date2);

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










void BFast(){
    int j = 0;
    for(int i = 0; i<=6; i++){
        while(1){
            if(F[j].Calories <= B->caloNeed + 3 && F[j].Calories <= B->caloNeed - 3){
                updateFoodLog(F[j].ID);
                strcpy(B[i].Name, F[j].Name);
                j=0;
                break;
            }
            j++;
        }
    }
}

void LNch(){
    int j = 0;
    for(int i = 0; i<=6; i++){
        while(1){
            if(F[j].Calories <= L->caloNeed + 3 && F[j].Calories <= L->caloNeed - 3){
                updateFoodLog(F[j].ID);
                strcpy(L[i].Name, F[j].Name);
                updatePickTime(F[j].PickTime);
                j=0;
                break;
            }
            j++;
        }
    }
}

void DNer(){
    int j = 0;
    for(int i = 0; i<=6; i++){
        while(1){
            if(F[j].Calories <= D->caloNeed + 3 && F[j].Calories <= D->caloNeed - 3){
                updateFoodLog(F[j].ID);
                strcpy(D[i].Name, F[j].Name);
                j=0;
                break;
            }
            j++;
        }
    }
}

void check(){
    int i = 0;
    while(1){
        if(F[i].ID ==0) break;
        printf("%d\n",F[i].ID);
        printf("%s\n",F[i].Name);
        printf("%d\n",F[i].PickTime);
        printf("%s\n",F[i].LastPick);
        printf("%d\n",F[i].Calories);
        i++;
    }
    // printf("%d\n",calories);
    // printf("%.2f %.2f %.2f",B[0].caloNeed,L[0].caloNeed,D[0].caloNeed);
    // printf(" %s", date);
    // for(i = 0; i<=6; i++){
    //     printf("\n%s",B[i].Name);
    // }
    // printf(" \n");
    // for(i = 0; i<=6; i++){
    //     printf("\n%s",L[i].Name);
    // }
    // printf(" \n");
    // for(i = 0; i<=6; i++){
    //     printf("\n%s",D[i].Name);
    // }
}

int main(){

importFood();
importCalories();
findCaloNeed();
findTime();
BFast();
LNch();
DNer();


check();


}