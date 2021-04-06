const burger = document.querySelector('#toggle');
const info = document.querySelector('.menu');

burger.addEventListener('change',function(e){
    if(burger.notchecked){
        info.style.display = 'none';
    }else{
        info.style.display = 'initial';
    }
});