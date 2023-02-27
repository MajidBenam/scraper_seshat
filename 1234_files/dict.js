function is_touch_device() {
 return (('ontouchstart' in window)
      || (navigator.MaxTouchPoints > 0)
      || (navigator.msMaxTouchPoints > 0));
}
 

if (document.domain != "www.popjisyo.com"){

ic="<img border=0 src='http://www.manythings.org/z/ic/";
ic2=".png' height=28 width=28 />";
dt = document.title;
document.write('<div class="noprinter notipod"><table class="dict" align=right width="100"><tr><td align=center><div style="background-color=#DEDEDE; width=100px; padding: 5px;"><small>');

//if (!is_touch_device()) {
// 
//document.write('<script src="http://site.answers.com/main/js/web_answertip.js?ANSW.nafid=8" type="text/javascript"></script>');
//document.write('<span id="answerTipEnabled"></span>');

//document.write('Double-click any word to see what it means.<br /><script type="text/javascript">ANSW.Trigger.showLogoIfEnabled("AnswerTips_icon_75x60.gif","");</script>');

//}

//document.write('<br />RedmondLabs');
//document.write ("<br /><a href=\"javascript:(function(){g_SRWebURL='http://redmondlabs.com/eslr';g_origURL=document.location.href;ddscript=document.createElement('SCRIPT');ddscript.type='text/javascript';ddscript.src='http://redmondlabs.com/eslr/js/jquery-1.4.1.min.js';document.getElementsByTagName('body')[0].appendChild(ddscript);ddscript2=document.createElement('SCRIPT');ddscript2.type='text/javascript';ddscript2.src='http://redmondlabs.com/eslr/js/highlight.js?v=0.9.4071.23206';document.getElementsByTagName('body')[0].appendChild(ddscript2);})();\">ESL Reader</a>")

document.write('<br /><br />PopJisyo');
document.write ("<br /><a href='https://www.popjisyo.com/WebHint/AddHint2.aspx?d=1&e=iso-8859-1&r=e&s=0&du=http%253a%252f%252fwww.m-w.com%252fcgi-bin%252fdictionary%253fbook%253dDictionary%2526va%253d&u="+location.href+"'>Japanese</a>")
document.write ("<br /><a href='https://www.popjisyo.com/WebHint/AddHint2.aspx?d=20&e=iso-8859-1&r=e&s=0&du=http%253a%252f%252fwww.m-w.com%252fcgi-bin%252fdictionary%253fbook%253dDictionary%2526va%253d&u="+location.href+"'>Korean</a>")
document.write ("<br /><a href='https://www.popjisyo.com/WebHint/AddHint2.aspx?d=14&e=iso-8859-1&r=e&s=0&du=http%253a%252f%252fwww.m-w.com%252fcgi-bin%252fdictionary%253fbook%253dDictionary%2526va%253d&u="+location.href+"'>Spanish</a>")
document.write ("<br /><a href='https://www.popjisyo.com/WebHint/AddHint2.aspx?d=12&e=iso-8859-1&r=e&s=0&du=http%253a%252f%252fwww.m-w.com%252fcgi-bin%252fdictionary%253fbook%253dDictionary%2526va%253d&u="+location.href+"'>Webster's 1913</a>")

document.write('<br /><br />Share');
document.write ("<br /><a href='http://www.facebook.com/sharer.php?u="+location.href+"'>"+ic+"facebook"+ic2+"</a>")
document.write ("<a href='http://del.icio.us/post?url="+location.href+"&title="+dt+"'>"+ic+"delicious"+ic2+"</a>")
document.write ("<a href='http://digg.com/submit?phase=2&url="+location.href+"&title="+dt+"'>"+ic+"digg"+ic2+"</a>")

document.write("<br /><br /><a href=\"javascript:popw='';Q='';x=document;y=window;if(x.selection)%20{Q=x.selection.createRange().text;}%20else%20if%20(y.getSelection)%20{Q=y.getSelection();}%20else%20if%20(x.getSelection)%20{Q=x.getSelection();}popw%20=%20y.open('https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=&su='%20+%20escape(document.title)%20+%20'&body='%20+%20escape(Q)%20+%20escape('\n')%20+%20escape(location.href)%20+%20'&zx=RANDOMCRAP&shva=1&disablechatbrowsercheck=1&ui=1','gmailForm','scrollbars=yes,width=680,height=510,top=175,left=75,status=no,resizable=yes');if%20(!document.all)%20T%20=%20setTimeout('popw.focus()',50);void(0);\">Gmail This</a>");

document.write('</small></td></tr></table></div>');

}