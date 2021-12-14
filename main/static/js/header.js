let slider_im = document.querySelectorAll('.slider_image')
let left_slider = document.querySelector('.left_slider')
let right_slider = document.querySelector('.right_slider')


left_slider.addEventListener('click',setActiveImage)

right_slider.addEventListener('click',setActiveImage)

function setActiveImage(){
    
    if (slider_im[0].classList.contains('im_active')){
        slider_im[0].classList.remove('im_active')
        slider_im[1].classList.add('im_active')
    }else if (slider_im[1].classList.contains('im_active')){
        slider_im[1].classList.remove('im_active')
        slider_im[2].classList.add('im_active')
    }else if (slider_im[2].classList.contains('im_active')){
        slider_im[2].classList.remove('im_active')
        slider_im[0].classList.add('im_active')
    }
}

slider_im.forEach((elem)=>{
    elem.addEventListener('click',()=>{
        clearActive();
        elem.classList.add('im_active')

    })
})

function clearActive(){
    slider_im.forEach((elem)=>{
        elem.classList.remove('im_active') 
    })
}