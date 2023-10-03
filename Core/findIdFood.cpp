#include <stdio.h>
#include <stdlib.h>
#include <string.h>




#define AllFood "InOut\\AllFood.txt"
#define IDfood "InOut\\IDfood.txt"

int numberOfFood = 0;

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

void CountFood(){
    while(1>0){
        if(F[numberOfFood].ID == 0) break;
        numberOfFood++;
    }
}

int main(){
    importFood();
    CountFood();
    FILE *f = fopen(IDfood,"w");
    fprintf(f,"%d",F[numberOfFood-1].ID + 1);
    fclose(f);

}