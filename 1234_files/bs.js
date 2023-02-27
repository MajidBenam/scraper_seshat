/* CK's lightweight BootStrap 3 Parts 2014-02-05*/
a='<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet">';
a+='<link href="http://www.manythings.org/z/bs3/audio/css/miniplayer.css" rel="stylesheet" media="screen"/>';
a+='<link href="http://www.manythings.org/z/bs2015/bs-ck2015c.css" rel="stylesheet">';
a+='<!--[if lt IE 9]>';
a+='<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></scr'+'ipt>';
a+='<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></scr'+'ipt>';
a+='<![endif]-->';
//     <!-- Placed at the end of the document so the pages load faster -->
a+='<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></scr'+'ipt>';
a+='<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></scr'+'ipt>';
// <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
a+='<script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></scr'+'ipt>';
a+='<script type="text/javascript" src="http://www.manythings.org/z/bs3/audio/inc/jquery.jplayer.min.js"></scr'+'ipt>';
a+='<script type="text/javascript" src="http://www.manythings.org/z/bs3/audio/inc/jquery.mb.miniPlayer.js"></scr'+'ipt>';
a+='<script type="text/javascript">$(function(){var ua = navigator.userAgent.toLowerCase();var isAndroid = /android/.test(ua);var isAndroidDefault = isAndroid && !(/chrome/i).test(ua);if(isAndroidDefault){alert("Sorry, your browser does not support this.")}';
a+='$(".audio").mb_miniPlayer({width:300,inLine:false,id3:false,autoPlay:false,skin:\'black\',downloadable:true});';
a+='});</scr'+'ipt>';
a+='<link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.manythings.org/apple-touch-icon-144x144.pngbs">';
a+='<link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.manythings.org/apple-touch-icon-114x114.png">';
a+='<link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.manythings.org/apple-touch-icon-72x72.png">';
a+='<link rel="apple-touch-icon-precomposed" href="http://www.manythings.org/apple-touch-icon-57x57.png">';
document.write(a);
/*  START NEW MENU 2015 */
function m(){
/*beginning-local-pages-temporary use*/
l='<li><a href="';
/*beginning*/
b='<li><a href="http://';
b_disabled='<li class="disabled"><a href="http://';
g='www.manythings.org/';
/*end*/
e='</a></li>';
h=g+'vocabulary/games/';
i='</a></li>'
/*disabled*/
d='<li><a href="http://';
a='<div id="wrap">';
a+='<div class="navbar navbar-default navbar-inverse navbar-fixed-top" role="navigation">';
a+='<div class="container-fluid">';
a+='<div class="navbar-header">';
a+='<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">';
a+='<span class="sr-only">Toggle navigation</span>';
a+='<span class="icon-bar"></span>';
a+='<span class="icon-bar"></span>';
a+='<span class="icon-bar"></span>';
a+='</button>';
a+='<a class="navbar-brand" href="http://www.manythings.org">ManyThings.org</a>';
a+='</div>';
a+='<div class="collapse navbar-collapse">';
a+='<ul class="nav navbar-nav">';

a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Reading <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+=b+g+'voa/history/">American History'+i;
a+=b+g+'voa/stories/">American Stories'+i;
a+=b+g+'voa/health/">Health'+i;
a+=b+g+'voa/people/">People (Biographies)'+i;
a+=b+g+'voa/places/">Places'+i;
a+=b+g+'k/reading.html">More...'+i;
a+='</ul>';
a+='</li>';

a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Sentences <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+=b+g+'bilingual/">Bilingual Sentence Pairs'+i;
//a+=b+g+'sentences/syllables/">English Sentences with Audio, Sorted by Syllable Count'+i;
a+=b+g+'sentences/words/">English Sentences Focusing on Words and Their Word Families'+i;
a+=b+g+'sentences/audioplayer/">Audio Sentence Player'+i;
a+=b+g+'audiosentences/">Bilingual Sentence Pairs, Both with Audio'+i;
a+=b+g+'sentences/audio/">English Sentences with Audio and Translations'+i;
a+=b+g+'corpus/tatoeba.html">More...'+i;
a+='</ul>';
a+='</li>';

if (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"]){
a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Listening <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+='<li class="dropdown-header">Audio</li>';
a+=b+g+'podcast/">Selected MP3 Files for ESL Students'+i;
a+=b+g+'voa/news/">VOA News with Text'+i;
a+=b+g+'audio/news/">VOA News with Read Along Video'+i;
//a+=b+g+'elllo/">Listening to Naturally-spoken English'+i;
a+=b+g+'voa/daily/">VOA Learning English Broadcast (30-minutes)'+i;
//a+=b+g+'wikipedia/">Selected Excerpts from Spoken Wikipedia'+i;
//a+=b+g+'voa/music-mp3.html">VOA\'s MP3 Files of VOA\'s Music Programs'+i;

a+=b+g+'k/listening.html">More...'+i;
a+='<li class="divider"></li>';
a+='<li class="dropdown-header">Video</li>';
a+=b+g+'voa/v/">VOA Special English Videos (with Text)'+i;
a+=b+g+'voa/v/ipad.html">Selected VOA Special English TV Videos'+i;
a+=b+g+'voa/v/ja/">Listen and Read Along Videos in VOA Special English'+i;

//a+=b+g+'voa/youtube/">VOA\'s YouTube Video Playlists'+i;
a+=b+g+'b/e/">ESL Videos'+i;
//a+=b+g+'k/videos.html">More...'+i;
a+='</ul>';
a+='</li>';

a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Vocabulary <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+=b+g+'lulu/">Games with Pictures (lulu)'+i;
/*
a+=b+g+'vocabulary/games/v/">Every Other Letter Game'+i;
a+=b+g+'vocabulary/games/y/">First & Last Game'+i;
a+=b+g+'vocabulary/games/w/">Missing Vowels Games'+i;
*/
a+=b+g+'vocabulary/">Vocabulary Lists &amp; Games'+i;
a+=b+g+'voa/words.htm">VOA Special English Word Book'+i;
a+=b+g+'k/vocabulary.html">More...'+i;
a+='</ul>';
a+='</li>';

a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Flash <b class="caret"></b></a>';
//a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Flash <b class="caret"></b></a>';

a+='<ul class="dropdown-menu">';
a+='<li class="dropdown-header">These require Flash.</li>';
a+=b+g+'voa/">VOA Quizzes'+i;
a+=b+g+'fq/">Flash Quizzes'+i;
a+=b+g+'pp/">Pronunciation'+i;
a+=b+g+'repeat/">Listen and Repeat'+i;
a+=b+g+'lar/">Daily Listen and Repeat'+i;
/*
a+=b+g+'fq/1/spelling.php?u=1">Spelling and Vocabulary Quizzes'+i;
a+=b+g+'mq/">Matching Quizzes'+i;
a+=b+h+'g/?f=c">VP - Catch the Spelling'+i;
a+=b+g+'wbg/">Word Based Games'+i;
a+=b+g+'ww/">WordWeb Games with VOA Special English Words'+i;
a+=b+h+'h/?f=c">WordWeb Games - Comprehensive Lists'+i;
a+=b+g+'cs/">Crossword Puzzles'+i;
a+=b+g+'voa/words.htm">VOA Special English Word Book'+i;
a+=b+g+'voa/words-frequency.htm">VOA Special English Words Color-coded'+i;
a+=b+g+'listen/">Listen and Read Along'+i;
a+=b+g+'voa/classroom/">Activities from VOA\'s "The Classroom"'+i;
a+=b+g+'sm/">Sentence Machine'+e;
a+=b+g+'ac/">Audio Concentration Games'+i;
*/

a+=b+g+'k/flash.html">More...'+i;
/*
a+='<li class="divider"></li>'
a+=b+g+'e/tt.html">Tongue Twisters &amp; Poems'+e;
a+=b+g+'e/hearing.html">Hearing'+e;
*/
/*
a+='<li class="divider"></li>';
a+='<li class="dropdown-header">Java Required</li>';
a+=b+g+'wm/">WordMeister'+i;
a+=b+g+'cs/">Crossword Puzzles'+i;
*/
/*
a+=b+g+'k/java.html">More...'+i;
*/
a+='</ul>';
a+='</li>';
} // end IF FLASH
/*
a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Menus <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+=b+g+'e/vocabulary.html">Vocabulary'+e;
a+=b+g+'e/grammar.html">Grammar'+e;
a+=b+g+'e/quiz.html">Vocabulary &amp; Grammar Quizzes'+e;
a+=b+g+'e/patterns.html">Sentence Patterns'+e;
a+=b+g+'e/proverbs.html">Proverbs'+e;
a+=b+g+'e/slang.html">Slang &amp; Idioms'+e;
a+=b+g+'e/pronunciation.html">Pronunciation'+e;
a+=b+g+'e/listening.html">Listening'+e;
a+=b+g+'e/podcasts.html">Podcasts: Jokes &amp; Songs'+e;
a+=b+g+'e/reading.html">Reading'+e;
a+=b+g+'e/spelling.html">Spelling'+e;
a+=b+g+'e/crosswords.html">Crossword Puzzles'+e;
a+=b+g+'e/voa.html">Voice of America (VOA)'+e;
a+=b+g+'e/requirements.html">Mobile, iPads, iPhones &amp; Cell Phones'+e;
a+=b+g+'e/voa.html">Voice of America (VOA)'+e;
a+='<li class="divider"></li>'
a+=b+g+'c/r.cgi/quiz">Super Quiz'+i;
a+=b+g+'anagrams/">Anagrams'+i;
a+=b+g+'proverbs/">Proverbs'+i;
a+=b+g+'slang/">Slang'+i;
a+=b+g+'songs/">Learn Songs'+i;
//a+=b+g+'signs/">Reading Signs'+i;
a+='</ul>';
a+='</li>';
*/
//a+='</ul><ul class="nav navbar-nav navbar-right">';
 
 
// Drop Down ABOUT
/*
a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">More <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+=b+g+'ipad/">Things for ESL on the iPad'+i;
a+=b+g+'ipad/listen/">Listen and Read Along (iPad Version)'+i;
a+=b+g+'e/requirements.html">Non-Flash Things'+i;
a+='<li class="divider"></li>'
a+=b+g+'e/abc.html">Alphabetical List of Sections'+e;
a+=b+g+'e/about.html">About / Contact'+e;
a+='<li class="divider"></li>';
a+=b+'aitech.ac.jp/~ckelly/">aitech.ac.jp/~ckelly'+e;
a+=b+'study.aitech.ac.jp/">study.aitech.ac.jp'+e;
a+='</ul>';
a+='</li>';
*/
/*
a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">Bootstrap <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';
a+=b+'getbootstrap.com/css/">CSS'+e;
a+=b+'getbootstrap.com/components/">Components'+e;
a+=b+'getbootstrap.com/javascript/">JavaScript'+e;
a+=b+'getbootstrap.com/customize/">Customize'+e;
a+=b+'getbootstrap.com/getting-started/#examples">Examples'+e;
a+='</ul>';
a+='</li>';
*/
a+='<li class="dropdown">';
a+='<a href="#" class="dropdown-toggle" data-toggle="dropdown">More <b class="caret"></b></a>';
a+='<ul class="dropdown-menu">';

a+=b+g+'daily/">Daily Study'+e;

a+=b+g+'e/sections.html">List of All Sections'+e;
//a+=b+g+'e/abc.html">Alphabetical Listing of Sections'+e;
// Maybe I don't want this, but require 830 to show OLD menus in the more menu
if ($(window).width() > 700) {
a+='<li class="divider"></li>';
a+=b+g+'o/">Old Menus (Used Before July 2015)'+e;
}
else {
}
a+=b+g+'e/">New Menus (Used After July 2015)'+e;
//a+='<li class="divider"></li>'
//a+=b+g+'e/abc.html">Alphabetical List of Sections'+e;
//a+=b+g+'e/about.html">About / Contact'+e;
a+='<li class="divider"></li>';
a+='<li class="dropdown-header">Share This Page</li>';
//https://www.facebook.com/sharer.php?u=http://www.manythings.org/voa/history/2.html
a+=b+'www.facebook.com/sharer/sharer.php?u='+location.href+'" title="Share on Facebook" target="_blank"><img alt="Share on Facebook" height="32" width="32" src="http://www.manythings.org/sharing/facebook.png"> Share on Facebook'+e;

//a+=b+'www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fwww.manythings.org%2F&t=" title="Share on Facebook" target="_blank" onclick="window.open(\'https://www.facebook.com/sharer/sharer.php?u=\' + encodeURIComponent(document.URL) + \'&t=\' + encodeURIComponent(document.URL)); return false;"><img alt="Share on Facebook" height="32" width="32" src="http://www.manythings.org/sharing/facebook.png"> Share on Facebook'+e;

a+=b+'plus.google.com/share?url='+location.href+'" target="_blank" title="Share on Google+" onclick="window.open(\'https://plus.google.com/share?url=\' + encodeURIComponent(document.URL)); return false;"><img alt="Share on Google+" height="32" width="32" src="http://www.manythings.org/sharing/google+.png"> Share on Google+'+e;


//a+=b+'plus.google.com/share?url=http%3A%2F%2Fwww.manythings.org%2F" target="_blank" title="Share on Google+" onclick="window.open(\'https://plus.google.com/share?url=\' + encodeURIComponent(document.URL)); return false;"><img alt="Share on Google+" height="32" width="32" src="http://www.manythings.org/sharing/google+.png"> Share on Google+'+e;
a+=b+'www.linkedin.com/shareArticle?mini=true&url=http%3A%2F%2Fwww.manythings.org%2F&title=&summary=&source=http%3A%2F%2Fwww.manythings.org%2F" target="_blank" title="Share on LinkedIn" onclick="window.open(\'http://www.linkedin.com/shareArticle?mini=true&url=\' + encodeURIComponent(document.URL) + \'&title=\' +  encodeURIComponent(document.title)); return false;"><img alt="Share on LinkedIn" height="32" width="32" src="http://www.manythings.org/sharing/linkedin.png"> Share on LinkedIn'+e;
a+=b+'twitter.com/intent/tweet?source='+location.href+'&text=:%20'+location.href+'" target="_blank" title="Tweet" onclick="window.open(\'https://twitter.com/intent/tweet?text=\' + encodeURIComponent(document.title) + \':%20\'  + encodeURIComponent(document.URL)); return false;"><img alt="Tweet" height="32" width="32" src="http://www.manythings.org/sharing/twitter.png"> Tweet'+e;

//a+=b+'twitter.com/intent/tweet?source=http%3A%2F%2Fwww.manythings.org%2F&text=:%20http%3A%2F%2Fwww.manythings.org%2F" target="_blank" title="Tweet" onclick="window.open(\'https://twitter.com/intent/tweet?text=\' + encodeURIComponent(document.title) + \':%20\'  + encodeURIComponent(document.URL)); return false;"><img alt="Tweet" height="32" width="32" src="http://www.manythings.org/sharing/twitter.png"> Tweet'+e;

a+=b+'pinterest.com/pin/create/button/?url='+location.href+'&description=" target="_blank" title="Pin it" onclick="window.open(\'http://pinterest.com/pin/create/button/?url=\' + encodeURIComponent(document.URL) + \'&description=\' +  encodeURIComponent(document.title)); return false;"><img alt="Pin it" height="32" width="32" src="http://www.manythings.org/sharing/pinterest.png"> Pin it'+e;
a+=b+'www.tumblr.com/share?v=3&u='+location.href+'&t=&s=" target="_blank" title="Post to Tumblr" onclick="window.open(\'http://www.tumblr.com/share?v=3&u=\' + encodeURIComponent(document.URL) + \'&t=\' +  encodeURIComponent(document.title)); return false;"><img alt="Post to Tumblr" height="32" width="32" src="http://www.manythings.org/sharing/tumblr.png"> Post to Tumblr'+e;
a+=b+'www.reddit.com/submit?url='+location.href+'&title=" target="_blank" title="Submit to Reddit" onclick="window.open(\'http://www.reddit.com/submit?url=\' + encodeURIComponent(document.URL) + \'&title=\' +  encodeURIComponent(document.title)); return false;"><img alt="Submit to Reddit" height="32" width="32" src="http://www.manythings.org/sharing/reddit.png"> Submit to Reddit'+e;

//a+=b+'pinterest.com/pin/create/button/?url=http%3A%2F%2Fwww.manythings.org%2F&description=" target="_blank" title="Pin it" onclick="window.open(\'http://pinterest.com/pin/create/button/?url=\' + encodeURIComponent(document.URL) + \'&description=\' +  encodeURIComponent(document.title)); return false;"><img alt="Pin it" height="32" width="32" src="http://www.manythings.org/sharing/pinterest.png"> Pin it'+e;
//a+=b+'www.tumblr.com/share?v=3&u=http%3A%2F%2Fwww.manythings.org%2F&t=&s=" target="_blank" title="Post to Tumblr" onclick="window.open(\'http://www.tumblr.com/share?v=3&u=\' + encodeURIComponent(document.URL) + \'&t=\' +  encodeURIComponent(document.title)); return false;"><img alt="Post to Tumblr" height="32" width="32" src="http://www.manythings.org/sharing/tumblr.png"> Post to Tumblr'+e;
//a+=b+'www.reddit.com/submit?url=http%3A%2F%2Fwww.manythings.org%2F&title=" target="_blank" title="Submit to Reddit" onclick="window.open(\'http://www.reddit.com/submit?url=\' + encodeURIComponent(document.URL) + \'&title=\' +  encodeURIComponent(document.title)); return false;"><img alt="Submit to Reddit" height="32" width="32" src="http://www.manythings.org/sharing/reddit.png"> Submit to Reddit'+e;

//a+=b+'getpocket.com/save?url=http%3A%2F%2Fwww.manythings.org%2F&title=" target="_blank" title="Add to Pocket" onclick="window.open(\'https://getpocket.com/save?url=\' + encodeURIComponent(document.URL) + \'&title=\' +  encodeURIComponent(document.title)); return false;"><img alt="Add to Pocket" height="32" width="32" src="http://www.manythings.org/sharing/pocket.png"> Add to Pocket'+e;
//a+=b+'wordpress.com/press-this.php?u=http%3A%2F%2Fwww.manythings.org%2F&t=&s=" target="_blank" title="Publish on WordPress" onclick="window.open(\'http://wordpress.com/press-this.php?u=\' + encodeURIComponent(document.URL) + \'&t=\' +  encodeURIComponent(document.title)); return false;"><img alt="Publish on WordPress" height="32" width="32" src="http://www.manythings.org/sharing/wordpress.png"> Publish on WordPress'+e;
//a+=b+'pinboard.in/popup_login/?url=http%3A%2F%2Fwww.manythings.org%2F&title=&description=" target="_blank" title="Save to Pinboard" onclick="window.open(\'https://pinboard.in/popup_login/?url=\' + encodeURIComponent(document.URL) + \'&title=\' +  encodeURIComponent(document.title)); return false;"><img alt="Save to Pinboard" height="32" width="32" src="http://www.manythings.org/sharing/pinboard.png"> Save to Pinboard'+e;
a+='</ul>';
a+='</li>';
a+='</div><!--/.nav-collapse -->';
a+='</div>';
a+='</div>';
document.write(a);
/*  END NEW MENU */
}
/* from d.js */
/* Replace part of all URLs on page
by CK 2011-07-23 */
find= "http://trans.hiragana.jp/ruby/";
if(self.location.href.match(find)){replace="";onload=function(){for(var i=0;i<document.links.length; i++){link=document.links[i].href;temp=link.split(find);temp=temp.join(replace);if(link.match(find)){document.links[i].href=temp;}}}}
if(top.location!=self.location){top.location=self.location;}
function flashcheck(){
/* Added 2017-01-17 */
var hasFlash = false;
try {
var fo = new ActiveXObject('ShockwaveFlash.ShockwaveFlash');
if (fo) {
hasFlash = true;
}
} catch (e) {
if (navigator.mimeTypes
&& navigator.mimeTypes['application/x-shockwave-flash'] != undefined
&& navigator.mimeTypes['application/x-shockwave-flash'].enabledPlugin) {
hasFlash = true;
}
}
//OLDER  Updated from this
//if (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"]){


// commented out 2020-11-25
if (hasFlash){
//document.write('<div class="alert alert-danger" role="alert"><p>If you see <b>Loading ...... Please be patient. ......</b>, then this activity doesn\'t work anymore.<br />In 2019, Adobe Flash changed something which disabled the way I imported data into some games and quizzes. If the data doesn\'t load, that\'s the reason.<br />Adobe published an official blog saying the Flash Player will be dead at the end of 2020, so I don\'t plan to update my Flash activities.</p></div>'); 
}else{
//document.write('<div class="alert alert-danger" role="alert">Flash is either not installed or is disabled on your device.</p><p><a  href="https://helpx.adobe.com/flash-player.html">How to Enable Flash</a></div>'); 
}
}


//CK embed swf 2010 h and w are optonal
function swf(swf,w,h){
flashcheck();
document.write('<center><div class="embed-responsive embed-responsive-4by3">');
var defaultWidth = "100%";
var defaultHeight = "82%";
/* Explorer and Opera Can't take Percent Heights */
if(navigator.appName.indexOf('Microsoft')!=-1){
var defaultHeight = "480";
}
if(navigator.userAgent.indexOf("Opera")!=-1){
var defaultHeight = "480";
}
var w = w || defaultWidth;
var h = h || defaultHeight;

var w = 800;
var h = 600;

// 2017 added <div class="embed-responsive embed-responsive-4by3">

document.write('<center><div class="embed-responsive embed-responsive-4by3">');
document.write('<object width="'+w+'" height="'+h+'"><param name="movie" value="'+swf+'" /><param name="allowFullScreen" value="true" /><embed wmode="transparent" src="'+swf+'"type="application/x-shockwave-flash" allowfullscreen="true" width="'+w+'" height="'+h+'"></embed><param name="wmode" value="transparent" /></div></object></center>');
}

/*
function MP3Player2(b) {
document.write('<audio width="480" height="80" controls><source src="'+b+'" type="audio/mp3">Your browser does not support HTML5 audio.</audio>');
}
*/

function sps(id,speed){x=document.getElementById(id);x.playbackRate=speed;}

function MP3Player(b) {
document.write('<audio  width="480" height="80" id="'+b+'" controls><source src="'+b+'" type="audio/mp3">Your browser does not support HTML5 audio.</audio>');

document.write('<br>Speed: <button onclick="sps(\''+b+'\',.75)" type="button">75%</button> <button onclick="sps(\''+b+'\',1)" type="button">100%</button> <button onclick="sps(\''+b+'\',1.25)" type="button">125%</button> <button onclick="sps(\''+b+'\',1.5)" type="button">150%</button> <button onclick="sps(\''+b+'\',1.75)" type="button">175%</button>  <button onclick="sps(\''+b+'\',2)" " type="button">200%</button>');
}

/* Google analytics */
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-38296564-1']);
_gaq.push(['_trackPageview']);
(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
function foot(){
document.write('<div id="ckannouncement"><br />If something  on our web site doesn\'t load properly, try clicking your "reload" button.&nbsp; &nbsp; &nbsp;<br />If it still doesn\'t work, please send a <a href="http://www.manythings.org/z/bug2014.html">bug report</a>. &nbsp; &nbsp; &nbsp;');
var end = new Date('2014-08-31');
var now = new Date();
    if (end - now > 0) {
document.write('<center><hr /><font size="5">We will be offline.</font><br />Our web server will be offline August 17, 27 &amp; 31, 2014 during daytime working hours in Japan.<br />We\'re sorry for the inconvenience.</center><hr />');
    }
}
