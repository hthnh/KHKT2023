#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define AllFood "InOut\\AllFood.txt"
#define deleteID "InOut\\deleteID.txt" 
int ID;
struct Food{
    int ID;
    char Name[50];
    char TimeOfDay[4];
    int withRice;
    int PickTime;
    char LastPick[15];
    int kcal;
    int Carb;
    int Protein;
    int Fat;
};Food F[1000];


void importFood(){
    struct Temp{char temp[50];};Temp t[10];
    int i = 0,y = 0;
    FILE *fp = fopen(AllFood,"r");
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

}
 

void deleteFood(int i){
    while(1){
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
        if(F[i+1].ID == 0) break;
        i++;
    }
}

void OutFood(){
    FILE *f = fopen(AllFood,"w");
    int j = 0;
    while(1){
        fprintf(f,"%d\n%s\n%s\n%d\n%d\n%s\n%d\n%d\n%d\n%d\n",F[j].ID,F[j].Name,F[j].TimeOfDay,F[j].withRice,F[j].PickTime,F[j].LastPick,F[j].kcal,F[j].Carb,F[j].Protein,F[j].Fat);
        j++;
        if(F[j].ID == 0)break;
    }
    fclose(f);
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
