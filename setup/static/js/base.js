let sidebarbutton = document.getElementById("sidebarbutton");

function closeElemen (parrent, element){
    console.log("")
};

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