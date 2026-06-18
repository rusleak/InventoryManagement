const API = "https://functions-app01-b6gncbafdgfta9cs.italynorth-01.azurewebsites.net";

async function loadProducts() {
    const response = await fetch(`${API}/api/products`);
    const data = await response.json();

    const tbody = document.getElementById("products");
    tbody.innerHTML = "";

    data.forEach(p => {
        const row = document.createElement("tr");

        const total = p.price * p.quantity;

        row.innerHTML = `
            <td>${p.name}</td>
            <td>${p.price.toFixed(2)}</td>
            <td>${p.quantity}</td>
            <td>${total.toFixed(2)}</td>
        `;

        tbody.appendChild(row);
    });
}

async function loadTotal() {
    const response = await fetch(`${API}/api/total`);
    const data = await response.json();

    document.getElementById("total").innerText =
        `Total: ${data.total.toFixed(2)} PLN`;
}