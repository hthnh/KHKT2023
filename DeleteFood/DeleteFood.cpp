#include <stdio.h>
#include <string.h>
char AllFood[100] = "D:\\code\\KHKT-Order\\InOut\\AllFood.txt";
char deleteID[100] = "D:\\code\\KHKT-Order\\InOut\\deleteID.txt"; int ID;
struct Food{
    int ID;
    char Name[50];
    int PickTime;
    char LastPick[10];
    int Calories;
};Food F[1000];

void importFood(){
    FILE *f = fopen(AllFood,"r");
    int i = 0;
    while(1){
        fscanf(f,"%d",&F[i].ID);
        fscanf(f,"%s",&F[i].Name);
        fscanf(f,"%d",&F[i].PickTime);
        fscanf(f,"%s",&F[i].LastPick);
        fscanf(f,"%d",&F[i].Calories);
        if(F[i].ID == 0) break;
        i++;
    }  
    fclose(f);
}

void deleteFood(int i){
    
    while(1){
        F[i].ID = F[i+1].ID;
        strcpy(F[i].Name,F[i+1].Name);
        F[i].PickTime = F[i+1].PickTime;
        strcpy(F[i].LastPick,F[i+1].LastPick);
        F[i].Calories = F[i+1].Calories;
        if(F[i+1].ID == 0) break;
        i++;
    }
}

void OutFood(){
    FILE *file = fopen(AllFood,"w");
    int i = 0;
    while(1){
        fprintf(file,"%d\n%s\n%d\n%s\n%d\n",F[i].ID,F[i].Name,F[i].PickTime,F[i].LastPick,F[i].Calories );
        i++;
        if(F[i].ID == 0)break;
    }
    fclose(file);
}
int main(){
    importFood();
    FILE *f= fopen(deleteID, "r");
    fscanf(f,"%d",&ID);
    fclose(f);
    int i = 0;
        while(1){
            if (F[i].ID == ID){
                deleteFood(i);
            }
            if(F[i].ID == 0) break;
            i++;
        }
        

    
    OutFood();
}
