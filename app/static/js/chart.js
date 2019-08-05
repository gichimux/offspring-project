document.addEventListener('DOMContentLoaded', function () {
    var myChart = Highcharts.chart('container', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'Product Prediction'
        },
        xAxis: {
            categories: ['months']
        },
        yAxis: {
            title: {
                text: 'pampers bought'
            }
        },
        series: [{
            name: 'past sales',
            data: [1, 0, 1, 1, 0, 0, -1 ,1, 0, 4, 5, 0, 0, -1]
        }, {
            name: 'prediction',
            data: [5, 7, 3, 6, 9, 3, 5, 1 , 0, 2, 3, 0, 0, -1]
        }]
    });
});