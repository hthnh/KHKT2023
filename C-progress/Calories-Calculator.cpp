#include <stdio.h>

char heightWeight[100] = "InOut\\heightWeight.txt";
char TotalCalories[100] = "InOut\\TotalCalories.txt";
float calories = 0,totalCalo = 0;
int numOfPeople;
struct CaloriesCalculator{
   int sex; // 0 = male  1 = female 
   int height;
   int weight;
   int age;
}; CaloriesCalculator C;
int Style;
/*
1 = khong van dong hoac ngoi nhieu
2 = van dong nhe nhung khong lien tuc
3 = moi tuan luyen tap 3-5 lan 
4 = moi ngay deu luyen tap
5 = tinh chat cong viec gan lien voi the thao
*/


void updateCalories(){
    FILE *f =fopen(TotalCalories,"r");
    fscanf(f,"%d",&numOfPeople);
    fscanf(f,"%f",&totalCalo);
    fclose(f);
    numOfPeople++;
    totalCalo += calories ;
    f = fopen(TotalCalories,"w");
    fprintf(f,"%d\n",numOfPeople);
    fprintf(f,"%.2f",totalCalo);
    fclose(f);
}

int main(){
    FILE *f = fopen(heightWeight,"r");

    fscanf(f,"%d",&C.sex);
    fscanf(f,"%d",&C.height);
    fscanf(f,"%d",&C.weight);
    fscanf(f,"%d",&C.age);
    fscanf(f,"%d",&Style);
    fclose(f);
    if (C.sex == 0){
        calories = (6.25 * C.height) + (10 * C.weight) - (5 * C.age) + 5;
    }else if(C.sex == 1){
        calories = (6.25 * C.height) + (10 * C.weight) - (5 * C.age) - 161;
    }
    if(Style == 1) calories *= 1.2;
    if(Style == 2) calories *= 1.375;
    if(Style == 3) calories *= 1.55;
    if(Style == 4) calories *= 1.725;
    if(Style == 5) calories *= 1.9;

    updateCalories();

    return 0;

}