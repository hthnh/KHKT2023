function SearchList() {// search function in Order
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myDish");
  li = ul.getElementsByTagName('li');

  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}

function addDish(id,nameFood) { //for User
  var ul = document.getElementById("myDish");
  var li = document.createElement("li");
  var a = document.createElement("a");
  a.appendChild(document.createTextNode(nameFood));//name of more list
  li.appendChild(a);//name of more list
  a.setAttribute("class", id); // added line :setAttribute(thuoc tinh,gia tri thuoc tinh)
  li.setAttribute("class", id); // added line :setAttribute(thuoc tinh,gia tri thuoc tinh)
  li.appendChild(a);
  ul.appendChild(li);
}
// them do an b= id gia tri bang ten phan loai


function addFoodToTable(food,id){
  var td = document.getElementById(id);
  td.innerHTML = food;
}

function Time(){
  var t = document.getElementById("time");
  var today = new Date();
  var date = today.getDate()+'-'+(today.getMonth()+1)+'-'+today.getFullYear();
  t.innerHTML = date;
}


