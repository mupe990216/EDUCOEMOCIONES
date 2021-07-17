let bandera = 0;
const slider = document.querySelector("#slider");
let sliderSection = document.querySelectorAll(".slider_section");
let sliderSectionLast = sliderSection[sliderSection.length - 1];
const btnLeft = document.querySelector("#btn_left");
const btnRight = document.querySelector("#btn_right");
slider.insertAdjacentElement('afterbegin',sliderSectionLast);
const btnsiguiente = document.querySelector("#btnsiguiente");

function next(){
	if(bandera==0){		
		let sliderSectionSecond = document.querySelectorAll(".slider_section")[1];		
		if(sliderSectionSecond===sliderSectionLast){
			bandera=1;
			btn_right.style.display = "none";
			btnsiguiente.style.display = "block";
		}else{
			let sliderSectionFirst = document.querySelectorAll(".slider_section")[0];
			slider.style.marginLeft = "-200%";
			slider.style.transition = "all 0.5s";
			setTimeout(function(){
				slider.style.transition = "none";
				slider.insertAdjacentElement('beforeend',sliderSectionFirst);
				slider.style.marginLeft = "-100%";
			}, 500);
		}
	}	
}

btnRight.addEventListener('click',function(){
	next();
});

// function preview(){
//     let sliderSection = document.querySelectorAll(".slider_section");
//     let sliderSectionLast = sliderSection[sliderSection.length - 1];
//     slider.style.marginLeft = "0";
//     slider.style.transition = "all 0.5s";
//     setTimeout(function(){
//         slider.style.transition = "none";
//         slider.insertAdjacentElement('afterbegin',sliderSectionLast);
//         slider.style.marginLeft = "-100%";
//     }, 500);
// }

// btnLeft.addEventListener('click',function(){
//     preview();
// });


// setInterval(function(){
//     next();
// },2500);