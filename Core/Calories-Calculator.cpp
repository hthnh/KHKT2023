#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define heightWeight "InOut\\heightWeight.txt"
#define TotalCalories "InOut\\TotalCalories.txt"
float calories[1000], totalcalo = 0;
int len =0;
struct CaloriesCalculator{
    int sex; // 0 = male  1 = female 
    int height;
    int weight;
    int age;
    int Style;  /*
                1 = khong van dong hoac ngoi nhieu
                2 = van dong nhe nhung khong lien tuc
                3 = moi tuan luyen tap 3-5 lan 
                4 = moi ngay deu luyen tap
                5 = tinh chat cong viec gan lien voi the thao
                */
    int Type;   /*
                1 = Gain weight
                2 = Loss weight
                3 = Normal
                */
        

}; CaloriesCalculator C[1000];

void addMenber(){
    struct Temp{char temp[50];};Temp t[7];
    int i = 0,y = 0;
    FILE *fp = fopen(heightWeight,"r");
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
        }while(i<6);
        i = 0;
        C[y].sex = atoi(t[0].temp);
        C[y].height = atoi(t[1].temp);
        C[y].weight = atoi(t[2].temp);
        C[y].age = atoi(t[3].temp);
        C[y].Style = atoi(t[4].temp);
        C[y].Type = atoi(t[5].temp);
        y++;
        len++;

    }
    free(line_buf);
    line_buf = NULL;

    fclose(fp);

}

int main(){
    addMenber();
    int i = 0;
    do{
    if (C[i].sex == 0){
        calories[i] = (6.25 * C[i].height) + (10 * C[i].weight) - (5 * C[i].age) + 5;
    }else if(C[i].sex == 1){
        calories[i] = (6.25 * C[i].height) + (10 * C[i].weight) - (5 * C[i].age) - 161;
    }
    if(C[i].Style == 1) calories[i] *= 1.232;
    if(C[i].Style == 2) calories[i] *= 1.375;
    if(C[i].Style == 3) calories[i] *= 1.55;
    if(C[i].Style == 4) calories[i] *= 1.725;
    if(C[i].Style == 5) calories[i] *= 1.9;
    totalcalo += calories[i];
    i++;
    }while (i < len);
    
    FILE *f = fopen(TotalCalories,"w");
    fprintf(f,"%d",len);
    fprintf(f,"\n%.2f",totalcalo);
    fprintf(f,"\n%d",C[0].Type);

    

    return 0;

}