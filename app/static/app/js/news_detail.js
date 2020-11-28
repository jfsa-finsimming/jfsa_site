
// 画面のサイズ・contentsの長さによって、detai・cover・右下の三角の高さを変化させる

// 初期状態の画面サイズによる条件分岐
window.onload = function(){
  var news_contents_h = document.getElementById('news_contents').clientHeight;
  console.log(news_contents_h)
  if (window.innerWidth > 750) {
    document.getElementById('news_cover').style.height = 140 + news_contents_h + 'px';
    document.getElementById('news_detail').style.height = 540 + news_contents_h + 'px';
  }else if (window.innerWidth <= 750) {

  }
}

// 画面サイズが変わった時の条件分岐
window.onresize = function(){
  var news_contents_h = document.getElementById('news_contents').clientHeight;
  console.log(news_contents_h)
  if (window.innerWidth > 750) {
    document.getElementById('news_cover').style.height = 140 + news_contents_h + 'px';
    document.getElementById('news_detail').style.height = 540 + news_contents_h + 'px';
  }else if (window.innerWidth <= 750) {

  }
}
