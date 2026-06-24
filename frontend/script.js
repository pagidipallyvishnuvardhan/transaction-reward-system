const API_URL = "http://127.0.0.1:8000";

async function addTransaction() {

    const userId = document.getElementById("userId").value;
    const amount = Number(document.getElementById("amount").value);
    const transactionId = document.getElementById("transactionId").value;

    const response = await fetch(`${API_URL}/transaction`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            userId,
            amount,
            transactionId
        })
    });

    const data = await response.json();

    const result = document.getElementById("transactionResult");

    if (response.ok) {
        result.style.color = "green";
        result.innerText = data.message;
    } else {
        result.style.color = "red";
        result.innerText = data.detail;
    }
}


async function getSummary() {

    const userId =
        document.getElementById("summaryUserId").value;

    const response =
        await fetch(`${API_URL}/summary/${userId}`);

    const data =
        await response.json();

    if (!response.ok) {
        document.getElementById("summaryResult").innerHTML =
            `<p style="color:red">${data.detail}</p>`;
        return;
    }

    document.getElementById("summaryResult").innerHTML = `
        <div class="summary-cards">

            <div class="summary-box">
                <h3>Total Amount</h3>
                <p>₹${data.totalAmount}</p>
            </div>

            <div class="summary-box">
                <h3>Transactions</h3>
                <p>${data.totalTransactions}</p>
            </div>

            <div class="summary-box">
                <h3>Reward Score</h3>
                <p>${data.score}</p>
            </div>

        </div>
    `;
}


async function getRanking() {

    const response =
        await fetch(`${API_URL}/ranking`);

    const data =
        await response.json();

    let table = `
        <table>
            <tr>
                <th>Rank</th>
                <th>User ID</th>
                <th>Score</th>
                <th>Total Amount</th>
                <th>Transactions</th>
            </tr>
    `;

    data.forEach(user => {

        table += `
            <tr>
                <td>${user.rank}</td>
                <td>${user.userId}</td>
                <td>${user.score}</td>
                <td>₹${user.totalAmount}</td>
                <td>${user.totalTransactions}</td>
            </tr>
        `;
    });

    table += `</table>`;

    document.getElementById("rankingResult").innerHTML = table;
}