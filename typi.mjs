export function typi(writer){
var str=writer;
var l=str.length;
let i=1;
var inter=setInterval(function(){
if(i==l){clearInterval(inter);}

var disp=document.getElementsByTagName("body")[0];
disp.innerHTML=str.substr(0,i);
i++;

},150);}
