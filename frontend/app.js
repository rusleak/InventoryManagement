const API="REPLACE_LATER";


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