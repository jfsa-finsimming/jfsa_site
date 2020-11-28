
// 画面のサイズ・newsの個数によって、news_allの高さを変化させる

// 初期状態の画面サイズによる条件分岐
  var elem = document.getElementById('news_all');

  if (window.innerWidth > 750) {
    if(document.getElementById('news7')!=null) {
      elem.style.height = '1960px';
    }else if(document.getElementById('news5')!=null){
      elem.style.height = '1480px';
    }else if(document.getElementById('news3')!=null){
      elem.style.height = '1000px';
    }else if(document.getElementById('news1')!=null){
      elem.style.height = '520px';
    }
  }else if (window.innerWidth <= 750) {

  }


// 画面サイズが変わった時の条件分岐
window.onresize = function(){

  var elem = document.getElementById('news_all');

  if (window.innerWidth > 750) {
    if(document.getElementById('news7')!=null) {
      elem.style.height = '1960px';
    }else if(document.getElementById('news5')!=null){
      elem.style.height = '1480px';
    }else if(document.getElementById('news3')!=null){
      elem.style.height = '1000px';
    }else if(document.getElementById('news1')!=null){
      elem.style.height = '520px';
    }
  }else if (window.innerWidth <= 750) {

  }
}
