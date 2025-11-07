function navToggleSubMenuContent(button){
    button.nextElementSibling.classList.toggle("show")
    button.classList.toggle("isShow")

    // Для поворота стрелки
    childrens = button.children
    childrens[childrens.length-1].classList.toggle("rotate")
}