var create = document.getElementById('create');
var createf = document.getElementById('createf');
var edit = document.getElementById('edit');
var editf = document.getElementById('editf');
var del = document.getElementById('delete');
var delf = document.getElementById('deletef');
var inp= document.getElementById('inp');

createf.style.display = "none";
editf.style.display = "none";
delf.style.display = "none";
inp.style.display = "none";


create.onclick = ()=>{
    inp.style.display = "block";
    createf.style.display = "block";
    editf.style.display = "none";
    delf.style.display = "none";
};
edit.onclick = ()=>{
    inp.style.display = "block";
    createf.style.display = "none";
    editf.style.display = "block";
    delf.style.display = "none";

};
del.onclick =()=>{
    inp.style.display = "block";
    createf.style.display = "none";
    editf.style.display = "none";
    delf.style.display = "block";
};