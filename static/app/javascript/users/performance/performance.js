// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

    // Create the data table.

                    var data = google.visualization.arrayToDataTable([
                      ['Year', 'Sales', 'Expenses'],
        [2016, 1777, 1929]
                    ]);

    // Set chart options
                    var options = {
                      legend: { position: 'right' }
                    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

    chart.draw(data, options);
});