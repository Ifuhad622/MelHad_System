// Example JavaScript for Admin Dashboard functionalities

// Fetch data from backend API endpoints
function fetchData(endpoint) {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            // Process data and update dashboard UI
            updateDashboard(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

// Example: Update dashboard with fetched data
function updateDashboard(data) {
    // Example: Update total orders
    document.getElementById('totalOrders').textContent = data.totalOrders;

    // Example: Update revenue
    document.getElementById('totalRevenue').textContent = '$' + data.totalRevenue.toFixed(2);

    // Example: Update recent orders list
    const recentOrdersList = document.getElementById('recentOrders');
    recentOrdersList.innerHTML = ''; // Clear existing list
    data.recentOrders.forEach(order => {
        const listItem = document.createElement('li');
        listItem.textContent = `${order.orderNumber} - ${order.customerName}`;
        recentOrdersList.appendChild(listItem);
    });
}

// Example: Initialize dashboard on page load
document.addEventListener('DOMContentLoaded', () => {
    // Fetch initial data when page loads
    fetchData('/api/dashboard_data');

    // Example: Add event listeners for refresh button
    const refreshButton = document.getElementById('refreshButton');
    refreshButton.addEventListener('click', () => {
        fetchData('/api/dashboard_data');
    });
});
