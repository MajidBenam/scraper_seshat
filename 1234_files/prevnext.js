/* JavaScript Copyright (C) 2009, 2015 by Charles Kelly http://www.manythings.org/
 * If you leave this notice in the script, you may
 * use this on your site, "as is" or modified.
 */
var LastPage=4076;
var FirstPage=4002;
var url = document.URL;
var ThisPage=parseInt(url.substring(url.lastIndexOf("\/")+1,url.lastIndexOf("\.")),10);
var NextPage=ThisPage+1;
var PrevPage=ThisPage-1;
var RndPage=Math.floor(Math.random()*(LastPage-FirstPage))+FirstPage;
//RndPage += FirstPage;
document.write('<center><small>');
if (PrevPage >= FirstPage) {
document.write('<a class="btn btn-primary btn-md active" role="button" href="'+PrevPage+'.html">&lt;= Back</a> [ Page ');
}else{
document.write('<a class="btn btn-primary btn-md disabled" role="button" href="'+LastPage+'.html">&lt;= Back</a> [ Page ');
}
//document.write('<small>www.www.manythings.org</small> - ');
document.write(ThisPage);
document.write(' ]');
//document.write('<a href="'+RndPage+'.html">Ramdom Page</a>');
if (NextPage > LastPage) {
document.write(' <a class="btn btn-primary btn-md disabled" role="button" href="'+FirstPage+'.html">Next =&gt;</a>');
}else{
document.write(' <a class="btn btn-primary btn-md active" role="button" href="'+NextPage+'.html">Next =&gt;</a>');
}
document.write('<br /><font color="red">');
//Get Date
var str=document.title;
var patt1=/(\d\d\d\d-\d\d-\d\d)/gi;
// still needs to be fixed for older pages
VOAdate=str.match(patt1);
if (VOAdate != null){document.write(VOAdate);}
document.write('</font></center></small><br />');
