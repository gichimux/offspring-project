var chartData=JSON.parse(window.appConfig.chartData)


Highcharts.chart('chart-container', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Sales Analytics'
    },
    subtitle: {
        text: 'product sales'
    },
    xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            },
        
        }
    },
    series: [
        {
            name: 'month ',
            data: Object.values(chartData)
        }
    ]
});
