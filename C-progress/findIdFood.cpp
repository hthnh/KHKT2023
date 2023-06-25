#include <stdio.h>



int i = 0;
char AllFood[100] = "InOut\\AllFood.txt";
char IDfood[100] = "InOut\\IDfood.txt";

struct Food{
    int ID;
    char Name[50];
    int PickTime;
    char LastPick[15];
    int Calories;
};Food F[1000];


void importFood(){
    FILE *f = fopen(AllFood,"r");
    while(1){
        fscanf(f,"%d",&F[i].ID);
        if(F[i].ID == 0 ) break;
        fscanf(f,"%s",&F[i].Name);
        fscanf(f,"%d",&F[i].PickTime);
        fscanf(f,"%s",&F[i].LastPick);
        fscanf(f,"%d",&F[i].Calories);
        i++;
    }  
    fclose(f);
}

int main(){
    importFood();

    FILE *f = fopen(IDfood,"w");
    fprintf(f,"%d",F[i-1].ID + 1);
    fclose(f);

}