//// Load the Visualization API and the corechart package.
//google.charts.load('current', {'packages':['corechart']});
//
//// Set a callback to run when the Google Visualization API is loaded.
//google.charts.setOnLoadCallback(drawChart);
//
//// Callback that creates and populates a data table,
//// instantiates the pie chart, passes in the data and
//// draws it.
//function drawChart() {
//
//    // Create the data table.
//    var data = new google.visualization.DataTable();
//    data.addColumn('string', 'PTO');
//    data.addColumn('number', 'num');
//    data.addRows([
//      ['PTO taken', 4],
//      ['PTO not taken', 1],
//    ]);
//
//    // Set chart options
//    var options = {
//        'title':'Available PTO',
//        'legend':'none',
//        'slices': {
//            0: { color: 'red' },
//            1: { color: '#dddddd' }
//        },
//        'titlePosition': 'none',
//        'backgroundColor': 'transparent',
//        'pieHole': 0.85,
//        'pieSliceText': 'value',
//        'pieSliceTextStyle' : {
//            color: 'black',
//        },
//        'pieSliceBorderColor': 'transparent'
//    };
//
//    // Instantiate and draw our chart, passing in some options.
//    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
//
//    chart.draw(data, options);
//}


                  google.charts.load('current', {'packages':['corechart']});
                  google.charts.setOnLoadCallback(drawChart);

                  function drawChart() {

                  var data = google.visualization.arrayToDataTable([
                        ['Year', 'Score']
                        {% for review in performance.all %}
                        , [ {{ review.date_submitted.year }}, {{ review.score }} ]
                        {% endfor %}
                        ]);

                    var options = {
                      legend: { position: 'right' }
                    };

                    var chart = new google.visualization.LineChart(document.getElementById('line_chart'));
                    chart.draw(data, options);
                  }