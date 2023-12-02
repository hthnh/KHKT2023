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


int numberOfFood =0,numberOfFoodBreakfast[2],numberOfFoodDinner[2],numberOfFoodLunch[2],numberOfPeople,kcal,positiveLimit, negativeLimit, len;
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
};Food F[1000], B[1000], D[1000], L[1000];

// Struct for food of week Breakfast Lunch Dinner
struct Menu{
    char Name[50];
    int carb;
    int protein;
    int fat;
};

struct Days{
    struct Menu Dinner;
    struct Menu Lunch;
    struct Menu Breakfast;
};Days Ds[7];


struct Diet{
    float carb;
    float protein;
    float fat;
};Diet DNeed;

    
void CountFood(){
    while(1>0){
        if(F[numberOfFood].ID == 0) break;
        numberOfFood++;
    }
}

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
        }while(i<10);
        i = 0;
        F[y].ID = atoi(t[0].temp);
        strncpy(F[y].Name,t[1].temp,strlen(t[1].temp)-1);
        strncpy(F[y].TimeOfDay,t[2].temp,strlen(t[2].temp)-1);
        F[y].withRice = atoi(t[3].temp);
        F[y].PickTime = atoi(t[5].temp);
        strncpy(F[y].LastPick,t[4].temp,strlen(t[4].temp)-1);
        F[y].kcal = atoi(t[6].temp);
        F[y].Carb = atoi(t[7].temp);
        F[y].Protein = atoi(t[8].temp);
        F[y].Fat = atoi(t[9].temp);
        y++;

    }
    free(line_buf);
    line_buf = NULL;
    fclose(fp);
    CountFood();
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
            fprintf(f,"%d\n%s\n%s\n%d\n%d\n%s\n%d\n%d\n%d\n%d\n",F[j].ID,F[j].Name,F[j].TimeOfDay,F[j].withRice,F[j].PickTime,F[j].LastPick,F[j].kcal,F[j].Carb,F[j].Protein,F[j].Fat);
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
        F[i].Carb = F[i+1].Carb;
        F[i].Protein = F[i+1].Protein;
        F[i].Fat = F[i].Fat;
        i++;
    }
}


int Breakfast(){
 int y = 0;
    for(int i = 0; i < numberOfFood; i++){
        if(strchr(F[i].TimeOfDay, '1') != NULL){
            B[y].ID = F[i].ID;
            strcpy(B[y].Name ,F[i].Name);
            strcpy(B[y].TimeOfDay ,F[i].TimeOfDay);
            B[y].withRice = F[i].withRice;
            B[y].PickTime = F[i].PickTime;
            strcpy(L[y].LastPick ,F[i].LastPick);
            B[y].kcal = F[i].kcal ;
            B[y].Carb = F[i].Carb;
            B[y].Protein = F[i].Protein;
            B[y].Fat = F[i].Fat;
            y++;
        }
    }
    return y;
}

int Lunch(){
    int y = 0;
    for(int i = 0; i < numberOfFood; i++){
        if(strchr(F[i].TimeOfDay, '2') != NULL){
            L[y].ID = F[i].ID;
            strcpy(L[y].Name ,F[i].Name);
            strcpy(L[y].TimeOfDay ,F[i].TimeOfDay);
            L[y].withRice = F[i].withRice;
            L[y].PickTime = F[i].PickTime;
            strcpy(L[y].LastPick ,F[i].LastPick);
            L[y].kcal = F[i].kcal ;
            L[y].Carb = F[i].Carb;
            L[y].Protein = F[i].Protein;
            L[y].Fat = F[i].Fat;
            y++;
        }
    }
    return y;
}
int Dinner(){
    int y=0;
   for(int i = 0; i < numberOfFood; i++){
        if(strchr(F[i].TimeOfDay, '3') != NULL){
            D[y].ID = F[i].ID;
            strcpy(D[y].Name ,F[i].Name);
            strcpy(D[y].TimeOfDay ,F[i].TimeOfDay);
            D[y].withRice = F[i].withRice;
            D[y].PickTime = F[i].PickTime;
            strcpy(D[y].LastPick ,F[i].LastPick);
            D[y].kcal = F[i].kcal ;
            D[y].Carb = F[i].Carb;
            D[y].Protein = F[i].Protein;
            D[y].Fat = F[i].Fat;
            y++;
        }
    }
    return y;
}
bool check_dupl(){
    for(int j = 0; j<7; j++){
        if(strcmp(B[numberOfFoodBreakfast[1]].Name, Ds[j].Breakfast.Name) == 0) return true;
        if(strcmp(B[numberOfFoodBreakfast[1]].Name, Ds[j].Lunch.Name) == 0) return true;
        if(strcmp(B[numberOfFoodBreakfast[1]].Name, Ds[j].Dinner.Name) == 0) return true;
        if(strcmp(L[numberOfFoodLunch[1]].Name, Ds[j].Lunch.Name) == 0) return true;
        if(strcmp(L[numberOfFoodLunch[1]].Name, Ds[j].Breakfast.Name) == 0) return true;
        if(strcmp(L[numberOfFoodLunch[1]].Name, Ds[j].Dinner.Name) == 0) return true;
        if(strcmp(D[numberOfFoodDinner[1]].Name, Ds[j].Dinner.Name) == 0) return true;
        if(strcmp(D[numberOfFoodDinner[1]].Name, Ds[j].Breakfast.Name) == 0) return true;
        if(strcmp(D[numberOfFoodDinner[1]].Name, Ds[j].Lunch.Name) == 0) return true;
    }
    return false;
}
void a(int y){
    if(numberOfFoodBreakfast[1] >= numberOfFoodBreakfast[0]){
        numberOfFoodLunch[1] += 1;
        numberOfFoodBreakfast[1] = 0;
        a(y);
        return;
    }
    if(numberOfFoodLunch[1] >= numberOfFoodLunch[0]){
        numberOfFoodDinner[1] += 1;
        numberOfFoodLunch[1] = 0;
        numberOfFoodBreakfast[1] = 0;
        a(y);
        return;
    }
    if(numberOfFoodDinner[1]>= numberOfFoodDinner[0]) return;
    int carb = B[numberOfFoodBreakfast[1]].Carb + L[numberOfFoodLunch[1]].Carb + D[numberOfFoodDinner[1]].Carb;
    int protein = B[numberOfFoodBreakfast[1]].Protein + L[numberOfFoodLunch[1]].Protein + D[numberOfFoodDinner[1]].Protein;
    int fat = B[numberOfFoodBreakfast[1]].Fat + L[numberOfFoodLunch[1]].Fat + D[numberOfFoodDinner[1]].Fat;
    if( carb <= DNeed.carb + (positiveLimit/4) || carb >= DNeed.carb - (negativeLimit/4)){
        if( protein <= DNeed.protein + (positiveLimit/4) || protein >= DNeed.protein - (negativeLimit/4)){ 
            if( fat <= DNeed.fat + (positiveLimit/9) || fat >= DNeed.fat - (negativeLimit/9)){
                if(check_dupl()) return;
                strcpy(Ds[y].Breakfast.Name,B[numberOfFoodBreakfast[1]].Name);
                strcpy(Ds[y].Lunch.Name,L[numberOfFoodBreakfast[1]].Name);
                strcpy(Ds[y].Dinner.Name,D[numberOfFoodBreakfast[1]].Name);
                numberOfFoodBreakfast[1] = 0;
                return;
            }else{
        numberOfFoodBreakfast[1] += 1;
        a(y);
        return;
    }
        }else{
        numberOfFoodBreakfast[1] += 1;
        a(y);
        return;
    }
    }else{
        numberOfFoodBreakfast[1] += 1;
        a(y);
        return;
    }
    return;
}

void b(){
    numberOfFoodBreakfast[0] = Breakfast();
    numberOfFoodDinner[0] = Dinner();
    numberOfFoodLunch[0] = Lunch();

    for(int i = 0; i < 7; i++){
        a(i);
        numberOfFoodBreakfast[1] = 0;
        numberOfFoodDinner[1] = 0;
        numberOfFoodLunch[1] = 0;
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


// void findFood(){
//     int i=0, j=0;
//     while (1){
//         while(1>0){
//         if(B[numberOfFoodBreakfast].ID == 0) break;
//         numberOfFoodBreakfast++;
//     }
//         if(i == numberOfFoodBreakfast) break;
//         if(B[i].Carb <= DNeed.carb + positiveLimit/4){
//             if(B[i].Protein <= DNeed.protein + positiveLimit/4){
//                 if(B[i].Fat <= DNeed.fat + positiveLimit/4){
//                     if(B[i].Carb >= DNeed.carb - negativeLimit/4){
//                         if(B[i].Protein >= DNeed.protein - negativeLimit/4){
//                             if(B[i].Fat >= DNeed.fat - negativeLimit/4){
//                                 updateFoodLog(B[i].ID);
//                                     strcpy(Ds[i].Breakfast.Name,B[i].Name);
//                                     Ds[i].Breakfast.carb = B[i].Carb;
//                                     Ds[i].Breakfast.protein = B[i].Protein;
//                                     Ds[i].Breakfast.fat = B[i].Fat;
//                                     while(1){
//                                         if(B[j+1].ID == 0) break;
//                                         B[j].ID = B[j+1].ID;
//                                         strcpy(B[j].Name,B[j+1].Name);
//                                         strcpy(B[j].TimeOfDay,B[j+1].TimeOfDay);
//                                         B[j].withRice = B[j+1].withRice;
//                                         B[j].PickTime = B[j+1].PickTime;
//                                         strcpy(B[j].LastPick,B[j+1].LastPick);
//                                         B[j].kcal = B[j+1].kcal;
//                                         j++;
//                                 } 
//                             }
//                         }
//                     }
//                 }
//             }
//         }
//     }
    
// }


void check(){
    int i = 0;
    for(int i = 0; i< 7;){
        printf("%s %s %s %d \n",Ds[i].Breakfast.Name,Ds[i].Dinner.Name,Ds[i].Lunch.Name, i);
        i++;
    }  
}

int main(){
    importFood();
    findNutrition();
    b();
    Output();


    return 0;
}