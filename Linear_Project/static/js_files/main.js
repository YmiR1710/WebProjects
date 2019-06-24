function create_table_form(value){
    document.getElementById("add_block").style.visibility = value;
}
function show_table() {
    document.getElementById(event.srcElement.nextElementSibling.id).style.display === "none" ?
        document.getElementById(event.srcElement.nextElementSibling.id).style.display = "block" :
            document.getElementById(event.srcElement.nextElementSibling.id).style.display = "none";
}
function change_color() {
    if (document.getElementById("list-block").style.backgroundColor === "black"){
        document.getElementById("list-block").style.backgroundColor = "white";
    } else {
        document.getElementById("list-block").style.backgroundColor = "black";
    }
}