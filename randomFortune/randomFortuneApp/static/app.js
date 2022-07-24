window.onload = function(){
    let i=1;
    setInterval(function(){
      let pic = document.getElementById('changeImg');
      pic.setAttribute("src",("../static/Image/"+"titleImage"+(i%2+1)+".png"));
      i++;
    },1000);

    let j=1;
    setInterval(function(){
      let title = document.getElementById('changeTitle');
      title.setAttribute("src",("../static/Image/"+"title"+(j%2+1)+".png"));
      j++;
    },1000);
};

const nameForm = document.querySelector("#name-form");
const nameInput = document.querySelector("#name-form input");
const introduce = document.querySelector("#introduce");
const greeting1 = document.querySelector("#greeting1");
const greeting2 = document.querySelector("#greeting2");
const greeting3 = document.querySelector("#greeting3");
const greeting4 = document.querySelector("#greeting4");
const cont1 = document.querySelector("#cont1");
const goBtn = document.querySelector("#goBtnImg");

function onNameSubmit(event) {
  event.preventDefault();
  const username = nameInput.value;
  nameForm.classList.add("hidden");
  greeting1.classList.add("hidden");
  greeting2.classList.add("hidden");
  greeting3.classList.add("hidden");
  greeting4.classList.add("hidden");
  introduce.style.fontSize = "30px";
  introduce.innerText = `${username} 님! 환영해요.`;
  introduce.classList.remove("hidden");
  cont1.classList.remove("hidden");
  goBtn.classList.remove("hidden");
}

function handleMouseEnter() {
  goBtn.setAttribute("src",("../static/Image/goBtn2.png"));
}

function handleMouseLeave() {
  goBtn.setAttribute("src",("../static/Image/goBtn.png"));
}

nameForm.addEventListener("submit", onNameSubmit);
goBtn.addEventListener("mouseenter", handleMouseEnter);
goBtn.addEventListener("mouseleave", handleMouseLeave);