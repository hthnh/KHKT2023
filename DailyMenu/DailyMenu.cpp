#include <stdio.h>
#include <string.h>
#include <time.h>



char WeeklyLog[100] = "D:\\code\\KHKT-Order\\InOut\\WeeklyLog.txt";
char FoodAfterFilter[100] = "D:\\code\\KHKT-Order\\InOut\\FoodAfterFilter.txt";
char caloriesIN[50] = "D:\\code\\KHKT-Order\\InOut\\TotalCalories.txt";
int calories,numOfPeople;
char date[20];

struct Food{
    int ID;
    char Name[50];
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000]; 



struct Breakfast{
    char Monday[50];
    char Tuesday[50];
    char Wednesday[50];
    char Thursday[50];
    char Friday[50];
    char Saturday[50];
    char Sunday[50];
    float caloNeed;
};Breakfast B[5];

struct Lunch{
    char Monday[50];
    char Tuesday[50];
    char Wednesday[50];
    char Thursday[50];
    char Friday[50];
    char Saturday[50];
    char Sunday[50];
    float caloNeed;
};Lunch L[5];

struct Dinner{
    char Monday[50];
    char Tuesday[50];
    char Wednesday[50];
    char Thursday[50];
    char Friday[50];
    char Saturday[50];
    char Sunday[50];
    float caloNeed;
};Dinner D[5];


void importFood(){
    FILE *f = fopen(FoodAfterFilter,"r");
    int i = 0;
    while(1){
        fscanf(f,"%d",&F[i].ID);
        fscanf(f,"%s",&F[i].Name);
        fscanf(f,"%d",&F[i].PickTime);
        fscanf(f,"%d",&F[i].LastPick);
        fscanf(f,"%d",&F[i].Calories);
        if(F[i].ID == 0) break;
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

void updateFoodLog(int i){
 FILE *f = fopen(WeeklyLog,"a");
 int j = 0;
    while (1){
        if(i = F[j].ID){
            fprintf(f,"\n%d\n%s\n%d\n%d\n%d\n",F[i].ID,F[i].Name,F[i].PickTime,F[i].LastPick,F[i].Calories );
            break;
        }
        j++;
    }
   fclose(f); 
}










void Breakfast(){
    int i = 0;
    while(1){
        if(F[i].Calories == B[0].caloNeed){
            
        }
        if(F[i].ID >= 999998) break;
        i++;
    } 
}




void check(){
    int i = 0;
    while(1){
        printf("%d\n",F[i].ID);
        printf("%s\n",F[i].Name);
        printf("%d\n",F[i].PickTime);
        printf("%d\n",F[i].LastPick);
        printf("%d\n",F[i].Calories);
        if(F[i].ID == 0) break;
        i++;
    }
    printf("%d\n",calories);
    printf("%.2f %.2f %.2f",B[0].caloNeed,L[0].caloNeed,D[0].caloNeed);
    printf("%s", date);
}

int main(){

importFood();
importCalories();
findCaloNeed();
findTime();





check();


}
