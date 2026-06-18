const API="https://functions-app01-b6gncbafdgfta9cs.italynorth-01.azurewebsites.net";


async function loadProducts(){

    const response=await fetch(
        `${API}/api/products`
    );

    const data=await response.json();

    document.getElementById(
        "output"
    ).innerText=
    JSON.stringify(data,null,2);

}


async function loadTotal(){

    const response=await fetch(
        `${API}/api/total`
    );

    const data=await response.json();

    document.getElementById(
        "output"
    ).innerText=
    "Total: "+data.total;

}