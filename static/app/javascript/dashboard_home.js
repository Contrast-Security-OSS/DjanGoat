// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

    // Create the data table.
    var pto_data = new google.visualization.DataTable();
    pto_data.addColumn('string', 'PTO');
    pto_data.addColumn('number', 'num');
    pto_data.addRows([
      ['PTO taken', 4],
      ['PTO not taken', 1],
    ]);

    var sick_days_data = new google.visualization.DataTable();
    sick_days_data.addColumn('string', 'Sick Days');
    sick_days_data.addColumn('number', 'num');
    sick_days_data.addRows([
      ['Sick Days taken', 3],
      ['Sick Days not taken', 10],
    ]);

    var income_data = new google.visualization.DataTable();
    income_data.addColumn('string', 'Income');
    income_data.addColumn('number', 'num');
    income_data.addRows([
      ['Income earned', 60000],
      ['Income not earned', 5000],
    ]);

    var performance_data = new google.visualization.DataTable();
    performance_data.addColumn('string', 'Income');
    performance_data.addColumn('number', 'num');
    performance_data.addRows([
      ['performance points earned', 5],
      ['performance points not earned', 5],
    ]);

    var retirement_data = new google.visualization.DataTable();
    retirement_data.addColumn('string', '401k');
    retirement_data.addColumn('number', 'num');
    retirement_data.addRows([
      ['Amount contributed', 7000],
      ['Amount not contributed', 1000],
    ]);

    // Set chart options
    var options = {
        'title':'Available PTO',
        'legend':'none',
        'slices': {
            0: { color: 'red' },
            1: { color: '#dddddd' }
        },
        'titlePosition': 'none',
        'backgroundColor': 'transparent',
        'pieHole': 0.85,
        'pieSliceText': 'value',
        'pieSliceTextStyle' : {
            color: 'black',
        },
        'pieSliceBorderColor': 'transparent'
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    var chart2 = new google.visualization.PieChart(document.getElementById('chart_div2'));
    var chart3 = new google.visualization.PieChart(document.getElementById('chart_div3'));
    var chart4 = new google.visualization.PieChart(document.getElementById('chart_div4'));
    var chart5 = new google.visualization.PieChart(document.getElementById('chart_div5'));

    chart.draw(pto_data, options);
    chart2.draw(sick_days_data, options);
    chart3.draw(income_data, options);
    chart4.draw(performance_data, options);
    chart5.draw(retirement_data, options);
}