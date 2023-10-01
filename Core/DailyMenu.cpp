#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define WeeklyLog "InOut\\WeeklyLog.txt"
#define FoodAfterFilter "InOut\\FoodAfterFilter.txt"
#define caloriesIN "InOut\\TotalCalories.txt"
#define DailyFood "InOut\\DailyFood.txt"
#define cantfind "can't find any food"
#define Properties "InOut\\Properties.txt"


int numberOfFood = 0,numberOfPeople,kcal,positiveLimit, negativeLimit, len;
char date[10];
int type, diet;
struct Food{
    int ID;
    char Name[50];
    char TimeOfDay[4];
    int withRice;
    int PickTime;
    char LastPick[15];
    int kcal;
    int Carb; //gam
    int Protein;
    int Fat;
};Food F[1000];

// Struct for food of week Breakfast Lunch Dinner
struct Menu{
    char Name[50];
    float carb;
    float protein;
    float fat;
};

struct Day{
    struct Menu Dinner;
    struct Menu Lunch;
    struct Menu Breakfast;
}; Day D[7];


struct Diet{
    float carb;
    float protein;
    float fat;
};Diet DNeed;

void importFood(){
    struct Temp{char temp[50];};Temp t[10];
    int i = 0,y = 0;
    FILE *fp = fopen(FoodAfterFilter,"r");
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
        F[y].kcal = atoi(t[6].temp);
        F[y].Carb = atoi(t[7].temp);
        F[y].Protein = atoi(t[8].temp);
        F[y].Fat = atoi(t[9].temp);
        y++;

    }
    free(line_buf);
    line_buf = NULL;

    fclose(fp);

}
    
    void CountFood(){
    while(1>0){
        if(F[numberOfFood].ID == 0) break;
        numberOfFood++;
    }
}

void importCalories(){
    float temp;
    FILE *f = fopen(caloriesIN,"r");
    fscanf(f,"%d",&numberOfPeople);
    fscanf(f,"%f",&temp);
    kcal = int(temp);
    kcal = kcal / numberOfPeople;

    fclose(f);
}

void ImportProperties(){
    FILE *f = fopen(Properties, "r");
    fscanf(f,"%d",&type);
    fscanf(f, "%d", &diet);
}


void findNutrition(){
    importCalories();
    ImportProperties();
    if(type == 1) {
        negativeLimit = 0;
        positiveLimit = 0.15 * kcal;
    }
    if(type == 2){
        negativeLimit = 0.15 * kcal;
        positiveLimit = 0;
    }
    if(type == 3){
        negativeLimit = 0.075 * kcal;
        positiveLimit = 0.075 * kcal;
    }
    switch (diet)
    {
    case 1:
        DNeed.carb = 0.35 * kcal / 4;
        DNeed.protein = 0.43 * kcal / 4;
        DNeed.fat = 0.22 * kcal / 9;
        break;
    case 2:
        DNeed.carb = 0.25 * kcal / 4;
        DNeed.protein = 0.35 * kcal / 4;
        DNeed.fat = 0.4 * kcal / 9;
    case 3:
        DNeed.carb = 0.7 * kcal / 4;
        DNeed.protein = 0.15 * kcal / 4;
        DNeed.fat = 0.15 * kcal / 9;
        break;
    default:
        break;
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

void updateFoodLog(int ID){
 FILE *f = fopen(WeeklyLog,"a");
 int j = 0;
    while (1){
        if( ID == F[j].ID){
            updateLastPick(j);
            updatePickTime(j);
            fprintf(f,"%d\n%s\n%s\n%d\n%d\n%s\n%d\n",F[j].ID,F[j].Name,F[j].TimeOfDay,F[j].withRice,F[j].PickTime,F[j].LastPick,F[j].kcal);
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
        F[i].kcal = F[i+1].kcal;
        i++;
    }
}



void findFood(){
    int j;
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){ 
            if(strchr(F[j].TimeOfDay,'1') == NULL) break;
            if( F[j].Carb <= DNeed.carb + positiveLimit/4){
                if (F[j].Carb >= DNeed.carb - negativeLimit/4){
                    if(F[j].Protein <= DNeed.protein + positiveLimit/4){
                        if(F[j].Protein >= DNeed.protein - negativeLimit/4){
                            if(F[j].Fat <= DNeed.fat + positiveLimit/9){
                                if(F[j].Fat >= DNeed.fat - negativeLimit/9/4){
                                    updateFoodLog(F[j].ID);
                                    strcpy( D[i].Breakfast.Name, F[j].Name);
                                    D[i].Breakfast.carb = F[j].Carb;
                                    D[i].Breakfast.protein = F[j].Protein;
                                    D[i].Breakfast.fat = F[j].Fat;
                                    clearFood(j);
                                    break;
                                }
                            }
                        }
                    }                      
                }
            } 
        }
    }
    for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){ 
            if(strchr(F[j].TimeOfDay,'2') == NULL) break;
            if( F[j].Carb <= DNeed.carb + positiveLimit/4){
                if (F[j].Carb >= DNeed.carb - negativeLimit/4){
                    if(F[j].Protein <= DNeed.protein + positiveLimit/4){
                        if(F[j].Protein >= DNeed.protein - negativeLimit/4){
                            if(F[j].Fat <= DNeed.fat + positiveLimit/9){
                                if(F[j].Fat >= DNeed.fat - negativeLimit/9){
                                    updateFoodLog(F[j].ID);
                                    strcpy( D[i].Dinner.Name, F[j].Name);
                                    D[i].Lunch.carb = F[j].Carb;
                                    D[i].Lunch.protein = F[j].Protein;
                                    D[i].Lunch.fat = F[j].Fat;
                                    clearFood(j);
                                    break;
                                }
                            }
                        }
                    }                      
                }
            } 
        }
    }
     for(int i = 0; i<=6; i++){
        for(j = 0; j<= numberOfFood-1; j++){ 
            if(strchr(F[j].TimeOfDay,'2') == NULL) break;
            if( F[j].Carb <= DNeed.carb + positiveLimit /4){
                if (F[j].Carb >= DNeed.carb - negativeLimit /4){
                    if(F[j].Protein <= DNeed.protein + positiveLimit /4){
                        if(F[j].Protein >= DNeed.protein - negativeLimit /4){
                            if(F[j].Fat <= DNeed.fat + positiveLimit/9){
                                if(F[j].Fat >= DNeed.fat - negativeLimit/9){
                                    updateFoodLog(F[j].ID);
                                    strcpy( D[i].Dinner.Name, F[j].Name);
                                    D[i].Dinner.carb = F[j].Carb;
                                    D[i].Dinner.protein = F[j].Protein;
                                    D[i].Dinner.fat = F[j].Fat;
                                    clearFood(j);
                                    break;
                                }
                            }
                        }
                    }                      
                }
            } 
        }
    }
}


void check(){
    int i = 0;
    while(1){
        printf("%s",D[i].Breakfast.Name);
        printf("%d",1);
        if(F[i].ID == 0 ) break;
        i++;
    }  
}

int main(void){
    CountFood();
importFood();
findNutrition();

findFood();
check();
    return 0;

}