// app/static/js/main.js

document.addEventListener("DOMContentLoaded", function() {
    // Fetch login analytics
    fetch('/admin/login-analytics')
        .then(response => response.json())
        .then(data => {
            let tableBody = document.querySelector("#login-analytics tbody");
            data.forEach(item => {
                let row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.username}</td>
                    <td>${item.email}</td>
                    <td>${item.login_time}</td>
                    <td>${item.ip_address}</td>
                    <td>${item.country}</td>
                `;
                tableBody.appendChild(row);
            });
        });

    // Fetch activity logs
    fetch('/admin/activity-logs')
        .then(response => response.json())
        .then(data => {
            let tableBody = document.querySelector("#activity-logs tbody");
            data.forEach(item => {
                let row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.username}</td>
                    <td>${item.event_type}</td>
                    <td>${item.event_description}</td>
                    <td>${item.event_time}</td>
                    <td>${item.risk_score}</td>
                `;
                tableBody.appendChild(row);
            });
        });
});
