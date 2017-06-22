// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {
    // console.log(document.all)

    // Create the data table.
    var sick_days_taken = parseInt(document.getElementById('sick_days_taken').value);
    var sick_days_earned = parseInt(document.getElementById('sick_days_earned').value);
    var pto_taken = parseInt(document.getElementById('pto_taken').value);
    var pto_earned = parseInt(document.getElementById('pto_earned').value);
    var time = new Date();
    var year = time.getFullYear()
    var month = time.getMonth() + 1
    var date = time.getDate()
    var today = 'As of today: ' + year + '-' + month + '-' + date


    var sick_days_data = google.visualization.arrayToDataTable([
        ['timeofday', 'Days Earned', 'Days Taken', 'Days Remaining'],
        [today, sick_days_earned, sick_days_taken, sick_days_earned - sick_days_taken]
        ])

    var pto_data = google.visualization.arrayToDataTable([
        ['As of Today', 'Days Earned', 'Days Taken', 'Days Remaining'],
        [today, pto_earned, pto_taken, pto_earned - pto_taken]
        ])

    // Set chart options
    var options = {
        'title':'Available PTO',
        'legend':{ position: 'right' },
        'titlePosition': 'none',
        'backgroundColor': 'transparent',
        'colors': ['#579da9', '#e26666', '#1e825e']
    };

    // Instantiate and draw our chart, passing in some options.
    var sick_days_chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    var pto_chart = new google.visualization.ColumnChart(document.getElementById('chart_div2'));

    sick_days_chart.draw(sick_days_data, options);
    pto_chart.draw(pto_data, options);

}

$(document).ready(function(){
    var schedules = JSON.parse(document.getElementById('schedules').value)
    $('#calendar').fullCalendar({
        events: schedules,
    });
});
