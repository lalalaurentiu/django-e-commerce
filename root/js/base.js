window.onload = function (){
    let alert = document.getElementById("message");
    console.log(alert)
    if (alert !== null){
        setTimeout(() =>{
            alert.classList.add("show-messages")
        }, 250);
    };
};

let sidebarbutton = document.getElementById("sidebarbutton");

sidebarbutton.addEventListener("click", () =>{
    let sidebar = document.getElementById("sidebar");
    if (sidebar.classList.contains("sidebarclose")){
        sidebar.classList.remove("sidebarclose");
    };

    let inside = document.getElementById("insideSidebar");
    sidebar.addEventListener("click", event =>{
        
        const isClickInside = inside.contains(event.target);
        if(!isClickInside){
            sidebar.classList.add("sidebarclose"); 
        }
    });
});

let headernav = document.getElementById("headernav");

document.addEventListener("scroll", e =>{
    if (this.scrollY > 144){
        headernav.style.maxHeight = "48px";
        
    }else {
        headernav.style.maxHeight = "70px";
    };
});

const cart_buttons = [...document.querySelectorAll(".cart-button")];
const cart_remove_buttons = [...document.querySelectorAll(".cart-remove-product")]

function listener_buttons (list){
    list.forEach(element => {
        element.addEventListener("click", () =>{
            setTimeout( () =>{
                location.reload(true)
            }, 500);
            
        });
    });
};

listener_buttons(cart_buttons);
listener_buttons(cart_remove_buttons);

let input = document.getElementById("search");

input.addEventListener("click", () =>{
    let browse_container = document.getElementById("browse");
    if (browse_container.classList.contains("d-none")){
        browse_container.classList.remove("d-none");
    }else{
        browse_container.classList.add("d-none");
    }
    })

    function search_products (){
    let input = document.getElementById("search");
    let search_items = document.getElementsByClassName("search-item");
    input = input.value.toLowerCase();;
    search_items.forEach(element => {
        if(!element.innerHTML.toLowerCase().includes(input)){
        element.style.display = "none";
        }else{
        element.style.display = "initial";
        }
    });
};

