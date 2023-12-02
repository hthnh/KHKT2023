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
	char *database = "TheMenuUsername";
	
	conn = mysql_init(NULL);
	
	/* Connect to database */
	if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
		fprintf(stderr, "%s0\n", mysql_error(conn));
		exit(1);
	}
	
	if (mysql_query(conn, "use TheMenuUsername;")){
		fprintf(stderr, "%s0.5\n", mysql_error(conn));
		exit(1);
	}
	
	/* send SQL query */
	if (mysql_query(conn, "select max(id) from User;" )){
		fprintf(stderr, "%s1\n", mysql_error(conn));
		exit(1);
		}
	res = mysql_use_result(conn);
	while((row = mysql_fetch_row(res)) !=NULL){
		sprintf(id_last_user, "%s0000000", row[0]);
	}
	char create_query[200];
	char use_query[100];

	printf("%s",id_last_user);
	sprintf(create_query, "create database A%s;",id_last_user);
	printf("%s",create_query);
	
	/* create Database */
	/* close connection */
	mysql_free_result(res);
	mysql_close(conn);		
}
