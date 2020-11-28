
// 画面のサイズ・newsの個数によって、news_allの高さを変化させる

// 初期状態の画面サイズによる条件分岐
  var elem = document.getElementById('team_all');

  if (window.innerWidth > 750) {
    if(document.getElementById('team8')!=null) {
      elem.style.height = '2000px';
    }else if(document.getElementById('team7')!=null){
      elem.style.height = '1880px';
    }else if(document.getElementById('team6')!=null){
      elem.style.height = '1500px';
    }else if(document.getElementById('team5')!=null){
      elem.style.height = '1380px';
    }else if(document.getElementById('team4')!=null){
      elem.style.height = '1000px';
    }else if(document.getElementById('team3')!=null){
      elem.style.height = '880px';
    }else if(document.getElementById('team2')!=null){
      elem.style.height = '500px';
    }else if(document.getElementById('team1')!=null){
      elem.style.height = '380px';
    }
  }else if (window.innerWidth <= 750) {

  }

// 画面サイズが変わった時の条件分岐
window.onresize = function(){

  var elem = document.getElementById('team_all');

  if (window.innerWidth > 750) {
    if(document.getElementById('team8')!=null) {
      elem.style.height = '2000px';
    }else if(document.getElementById('team7')!=null){
      elem.style.height = '1880px';
    }else if(document.getElementById('team6')!=null){
      elem.style.height = '1500px';
    }else if(document.getElementById('team5')!=null){
      elem.style.height = '1380px';
    }else if(document.getElementById('team4')!=null){
      elem.style.height = '1000px';
    }else if(document.getElementById('team3')!=null){
      elem.style.height = '880px';
    }else if(document.getElementById('team2')!=null){
      elem.style.height = '500px';
    }else if(document.getElementById('team1')!=null){
      elem.style.height = '380px';
    }
  }else if (window.innerWidth <= 750) {

  }
}
