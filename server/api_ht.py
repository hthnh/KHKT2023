from flask import Flask, jsonify, request
import json
import mysql.connector
import os

mydb = mysql.connector.connect(host = "hthnh.ddns.net", port = "2006", user = "root", password = "1234", database = "User_Information", autocommit=True)

app = Flask(__name__)
mycursor = mydb.cursor()

def number_of_user():
    mycursor.execute("SELECT COUNT(*) FROM Identification")
    for x in mycursor.fetchall():
        return int(x[0])
def next_id_user():
    mycursor.execute("SELECT max(id) FROM Identification")
    for x in mycursor.fetchall():
        return int(x[0]) + 1
def get_users():
    count_user()
    mycursor.execute("SELECT * FROM Identification")
    users = []
    info_user = mycursor.fetchall()
    y = 0
    for i in range(int(number_of_user())):
        user = {}
        temp = info_user
        tempi = temp[i]
        user = {'id': tempi[0], 'username':tempi[1], 'password':tempi[2]}
        users.append(user)
    return users



@app.route('/user',methods=['GET']) #all user
def alluser():
    return jsonify(get_users())




@app.route('/user/<int:id>', methods=['GET']) #user by id
def get_user_by_id(id: int):
    user = get_user(id)
    if user is None:
        return jsonify({ 'error': 'User does not exist'}), 404
    return jsonify(user)

def get_user(id):
    return next((e for e in users if e['id'] == id), None)




@app.route('/register', methods=['POST']) #register
def create_user():
    user = json.loads(request.data)
    if not user_is_valid(user):
        return jsonify({ 'error': 'Invalid user properties.' }), 400
    user['id'] = next_id_user()
    insert_query = ("INSERT INTO `User_Information`.`Identification` (`id`, `username`, `userpassword`) VALUES ('%s', '%s', '%s');"%(user['id'],user['username'],user['password']))
    mycursor.execute(insert_query)
    os.system("./register.exe")
    return jsonify(user), 201

def user_is_valid(user):
    temp = {}
    key = {}
    i = 0
    for x in user.keys():
        temp[i] = x
        i += 1
    key[0] = temp[0]
    key[1] = temp[1]
    if (key[0] != 'username' and key[1] != "password"):
        return False
    return True


@app.route('/login',methods=['POST']) #login
def give_id_user():
    user = json.loads(request.data)
    temp = {}
    i = 0
    for x in user.values():
        temp[i] = x
        i += 1
    username = temp[0]
    userpassword = temp[1]
    mycursor.execute("select username from Identification;")
    if check_username(username,mycursor.fetchall()):
        mycursor.execute("select userpassword from Identification where (`username` = '%s');"%(username))
        if check_password(userpassword,mycursor.fetchall()):
            mycursor.execute("select id from Identification where (`userpassword` = '%s');"%(userpassword))
            return jsonify(mycursor.fetchall()), 202       
    return jsonify({ 'error': 'user not found.' }), 404

def check_username(un_user, un_server):
    for x in un_server:
        if  un_user in x:
            return True
    return False
def check_password(pw_user, pw_server):
    for x in pw_server:
        if pw_user in x:
            return True
    return False


if __name__ == '__main__':
    app.run(host = "192.168.10.40",port=5000)