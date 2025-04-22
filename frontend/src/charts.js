window.onload = function () {
  const emailsSentChart = new Chart(document.getElementById('emailsSentChart'), {
    type: 'bar',
    data: {
      labels: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
      datasets: [{
        label: 'Correos Enviados',
        data: [120, 150, 180, 130, 170],
        backgroundColor: '#4e73df'
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } }
    }
  });

  const emailsOpenedChart = new Chart(document.getElementById('emailsOpenedChart'), {
    type: 'bar',
    data: {
      labels: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
      datasets: [{
        label: 'Correos Abiertos',
        data: [90, 110, 150, 100, 140],
        backgroundColor: '#1cc88a'
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } }
    }
  });

  const promoClicksChart = new Chart(document.getElementById('promoClicksChart'), {
    type: 'bar',
    data: {
      labels: ['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
      datasets: [{
        label: 'Clics en Promociones',
        data: [40, 60, 70, 50, 65],
        backgroundColor: '#f6c23e'
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } }
    }
  });
}


