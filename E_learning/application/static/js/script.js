console.log('hi');

//profile section division
function openCity(cityName, elmnt, color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "#7fd2f3";
    }
    document.getElementById(cityName).style.display = "block";
    elmnt.style.backgroundColor = color;
}
document.getElementById("defaultOpen").click();

// edit User
let editUser = document.getElementById("edit");
let editLinkBtn = document.getElementById("editBtn");
let useritems = document.getElementById("useritems");
let cancelCng = document.getElementById("cancelCng");
let msg = document.getElementById("msg");

editLinkBtn.addEventListener("click", () => {
    console.log('clicked')
    editUser.style.display = "block";
    useritems.style.display = "none";
})

cancelCng.addEventListener("click", () => {
    console.log('cancel');
    editUser.style.display = "none";
    useritems.style.display = "block";
})

let curimg = document.getElementById('defpic');
let updimg = document.getElementById('updpic');
let btnupd = document.getElementById('updbtn');
