let regions_data = JSON.parse(document.getElementById('regions_data').textContent);
let towns_data = JSON.parse(document.getElementById('towns_data').textContent);

let regions = document.getElementById("regions");

for (item of regions_data ){
    let region = document.createElement("option");
    region.innerHTML = item.region;
    regions.append(region);
};

let towns = document.getElementById("towns");

let check_button = document.getElementById("check")

regions.addEventListener("change", (event) => {
    towns.removeAttribute("disabled");
    for (const key of towns_data) {
        if (key[regions.value]){
            towns.innerHTML = "";
            let default_option = document.createElement("option")
            default_option.innerHTML = "Choose...";
            towns.append(default_option);
            
            key[regions.value].forEach(element => {
                let option = document.createElement("option")
                option.innerHTML = element
                towns.append(option)
            });
        };
    };      
});