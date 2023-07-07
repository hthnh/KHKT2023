#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int i = 0;
#define AllFood "InOut\\AllFood.txt"
#define IDfood "InOut\\IDfood.txt"

struct Food{
    int ID;
    char Name[50];
    char TimeOfDay[3];
    int withRice;
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000];


void importFood(){
    struct Temp{char temp[50];};Temp t[7];
    int i = 0,y = 0;
    FILE *fp = fopen(AllFood,"r");
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
        F[y].Calories = atoi(t[6].temp);
        y++;

    }
    free(line_buf);
    line_buf = NULL;

    fclose(fp);

}

int main(){
    importFood();

    FILE *f = fopen(IDfood,"w");
    fprintf(f,"%d",F[i-1].ID + 1);
    fclose(f);

}