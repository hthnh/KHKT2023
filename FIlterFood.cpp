#include <stdio.h>
#include <string.h>

char AllFood[100] = "D:\\code\\KHKT-Order\\InOut\\AllFood.txt";
char WeeklyLog[100] = "D:\\code\\KHKT-Order\\InOut\\WeeklyLog.txt";
char FoodAfterFilter[100] = "D:\\code\\KHKT-Order\\InOut\\FoodAfterFilter.txt";
struct Food
{
    int ID;
    char Name[50];
    int PickTime;
    int LastPick;
    int Calories;
};Food F[1000],FF[100];

void importFood(){
    FILE *f = fopen(AllFood,"r");
    int i = 0;
    while(1){
        fscanf(f,"%d",&F[i].ID);
        fscanf(f,"%s",&F[i].Name);
        fscanf(f,"%d",&F[i].PickTime);
        fscanf(f,"%d",&F[i].LastPick);
        fscanf(f,"%d",&F[i].Calories);
        if(F[i].ID >= 999998) break;
        i++;
    }  
    fclose(f);
}

void importFoodLog(){
    FILE *f = fopen(WeeklyLog,"r");
    int i = 0;
    while(1){
        fscanf(f,"%d",&FF[i].ID);
        fscanf(f,"%s",&FF[i].Name);
        fscanf(f,"%d",&FF[i].PickTime);
        fscanf(f,"%d",&FF[i].LastPick);
        fscanf(f,"%d",&FF[i].Calories);
        if(FF[i].ID >= 999998) break;
        i++;
    }  
    fclose(f);
}
void clearFood(int i){
    while(1){
        F[i].ID = F[i+1].ID;
        strcpy(F[i].Name,F[i+1].Name);
        F[i].PickTime = F[i+1].PickTime;
        F[i].LastPick = F[i+1].LastPick;
        F[i].Calories = F[i+1].Calories;
        if(F[i+1].ID >= 999998) break;
        i++;
    }
}

void OutFood(){
    FILE *f = fopen(FoodAfterFilter,"w");
    int i = 0;
    while(1){
        if(F[i].ID >= 999998){
            fprintf(f,"999999");
            break;
        }
        fprintf(f,"%d\n%s\n%d\n%d\n%d\n",F[i].ID,F[i].Name,F[i].PickTime,F[i].LastPick,F[i].Calories );
        i++;
    }
    fclose(f);
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
            
            if(F[y].ID >= 999998) break;
            y++;
        }
        if(F[i].ID >= 999998) break;
        i++;
    }
    
    OutFood();


    return 0;
}