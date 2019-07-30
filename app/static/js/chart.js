document.addEventListener('DOMContentLoaded', function () {
    var myChart = Highcharts.chart('container', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'Offspring prediction'
        },
        xAxis: {
            categories: ['pampers', 'baby socks', 'towels']
        },
        yAxis: {
            title: {
                text: 'pampers bought'
            }
        },
        series: [{
            name: 'January',
            data: [1, 0, 4, 5, 0, 6, 7]
        }, {
            name: 'February',
            data: [5, 7, 3, 6, 9, 3, 5]
        }]
    });
});