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
    int TimeOfDay;
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
    /* Đọc dòng đầu tiên trong file */
    line_size = getline(&line_buf, &line_buf_size, fp);

    /* Lặp lại việc đọc và hiển thị nội dung cho tới khi hoàn tất */
    while (line_size >= 0)
    {
        do{
        i++;
        strcpy(t[i].temp,line_buf);
        /* Đọc dòng tiếp theo */
        line_size = getline(&line_buf, &line_buf_size, fp);
        }while(i<7);
        i = 0;
        F[y].ID = atoi(t[0].temp);
        strcpy(F[y].Name,t[1].temp);
        F[y].TimeOfDay = atoi(t[2].temp);
        F[y].withRice = atoi(t[3].temp);
        strcpy(F[y].LastPick,t[4].temp);
        F[y].PickTime = atoi(t[5].temp);
        F[y].Calories = atoi(t[6].temp);
        y++;

    }
    /* Giải phóng buffer */
    free(line_buf);
    line_buf = NULL;

    /* Đóng file pointer */
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
check();




}