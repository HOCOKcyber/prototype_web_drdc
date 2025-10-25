const menuButton = document.getElementById("collapse_menu_btn")
const sidebar = document.getElementById("site_navigation")

menuButton.addEventListener("click", () => {
    sidebar.classList.toggle("close")

    Array.from(sidebar.getElementsByClassName("show")).forEach(it => {
        it.classList.remove("show")
    });

    Array.from(sidebar.getElementsByClassName("sub_menu_btn")).forEach(it => {
        it.classList.remove("isShow")
    });
})

function navToggleSubMenu(button){
    button.nextElementSibling.classList.toggle("show")
    button.classList.toggle("isShow")

    if (sidebar.classList.contains("close")){
        sidebar.classList.toggle("close")
    }
}