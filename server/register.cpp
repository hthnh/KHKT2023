#include <mysql/mysql.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
main() {
	char id_last_user[100];
	MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	
	char *server = "localhost";
	char *user = "root";
	char *password = "1234"; /* set me first */
	char *database = "User_Information";
	
	conn = mysql_init(NULL);
	
	/* Connect to database */
	if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
		fprintf(stderr, "%s0\n", mysql_error(conn));
		exit(1);
	}
	
	if (mysql_query(conn, "use User_Information;")){
		fprintf(stderr, "%s0.5\n", mysql_error(conn));
		exit(1);
	}
	
	/* send SQL query */
	if (mysql_query(conn, "select max(id) from Identification;" )){
		fprintf(stderr, "%s1\n", mysql_error(conn));
		exit(1);
		}
	res = mysql_use_result(conn);
	while((row = mysql_fetch_row(res)) !=NULL){
		sprintf(id_last_user, "%s", row[0]);
	}

	char create_query[200];
	char use_query[200];

	sprintf(create_query, "create database A%s;",id_last_user);
	sprintf(use_query, "Use A%s;",id_last_user);
	if (mysql_query(conn, create_query )){
	 	fprintf(stderr, "%s2\n", mysql_error(conn));
	 	exit(1);
	}
	if (mysql_query(conn, use_query)){
		fprintf(stderr, "%s3\n", mysql_error(conn));
		exit(1);
	}
	if (mysql_query(conn, " create table AllFood("
		"IDFood int not null,"
		"Name nvarchar(50) not null,"
    	"TimeOfDay char(4),"
     	"withRice bit,"
		"Picktime int,"
		"Lastpick char(15),"
    	"kcal int,"
		"Carb int,"
    	"Protein int,"
		"Fat int,"
    	"primary key(IDFood));")) {
	 	fprintf(stderr, "%s4\n", mysql_error(conn));
	 	exit(1);
	 	}

	if (mysql_query(conn ,"create table DailyFood("
		"Day int not null,"
	 	"Breakfast nvarchar(50) not null,"
	 	"Lunch nvarchar (50) not null,"
		"Dinner nvarchar (50) not null );")) {
	 	fprintf(stderr, "%s5\n", mysql_error(conn));
	 	exit(1);
	}


	if (mysql_query(conn, "create table FoodAfterFilter("
		"IDFood int not null,"
		"Name nvarchar(50) not null,"
    	"TimeOfDay char(4),"
		"withRice bit,"
    	"Picktime int,"
		"Lastpick char(15),"
    	"kcal int,"
		"Carb int,"
    	"Protein int,"
		"Fat int);")) {
		fprintf(stderr, "%s6\n", mysql_error(conn));
	 	exit(1);
	}

	if (mysql_query(conn, "create table IDfood(IDFood int);")) {
		fprintf(stderr, "%s7\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "create table Properties(type int,diet int);")) {
		fprintf(stderr, "%s8\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "Create table TotalCalories(numberOfMember int,totalcalo float);")) {
		fprintf(stderr, "%s9\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "create table WeeklyLog("
		"IDFood int not null,"
		"Name nvarchar(50) not null,"
		"TimeOfDay char(4),"
		"withRice bit,"
		"Picktime int,"
		"Lastpick char(15),"
		"kcal int,"
		"Carb int,"
		"Protein int,"
		"Fat int,"
		"primary key(IDFood));")) {
		fprintf(stderr, "%s10\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "create table conditionActivate(Date char(15), conditionClearLog int);")) {
		fprintf(stderr, "%s11\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "create table deleteID(IDFood int);")) {
		fprintf(stderr, "%s12\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "create table heightWeight(Gender int,Height int,Weight int,Age int,Style int);")) {
		fprintf(stderr, "%s13\n", mysql_error(conn));
		exit(1);
	}
	/* close connection */
	mysql_free_result(res);
	mysql_close(conn);
}