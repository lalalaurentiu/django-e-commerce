let regions_data = JSON.parse(document.getElementById('regions_data').textContent);
let towns_data = JSON.parse(document.getElementById('towns_data').textContent);

let regions = document.getElementById("regions");
let default_value_region = document.createElement("option");
default_value_region.innerHTML = "Choose..."
default_value_region.setAttribute("value", "")
default_value_region.setAttribute("disabled", "")
default_value_region.setAttribute("selected", "")
regions.append(default_value_region)

for (item of regions_data ){
    let region = document.createElement("option");
    region.innerHTML = item.region;
    regions.append(region);
};

let towns = document.getElementById("towns");
let default_value_towns = document.createElement("option");
default_value_towns.innerHTML = "Choose..."
default_value_towns.setAttribute("value", "")
default_value_towns.setAttribute("disabled", "")
default_value_towns.setAttribute("selected", "")
towns.append(default_value_towns)

let check_button = document.getElementById("check")

regions.addEventListener("change", (event) => {
    towns.removeAttribute("disabled");
    for (const key of towns_data) {
        if (key[regions.value]){
            towns.innerHTML = "";
            let default_option = document.createElement("option")
            default_option.innerHTML = "Choose...";
            default_option.setAttribute("selected", "")
            default_option.setAttribute("value", "")
            default_option.setAttribute("disabled", "")
            
            
            towns.append(default_option);
            
            key[regions.value].forEach(element => {
                let option = document.createElement("option")
                option.innerHTML = element
                towns.append(option)
            });
        };
    };      
});

let payment_available = [
    document.getElementById("id_paiment_method_0"),
    document.getElementById("id_paiment_method_1"),
    document.getElementById("id_paiment_method_2"),
    document.getElementById("id_paiment_method_3"),
]

payment_available.forEach((element, index) =>{
    if (index == 0){
        element.setAttribute("checked", "");
    } else {
        element.setAttribute("disabled", "");
    };
});