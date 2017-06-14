import datetime
import pytz
from app.models import User

# Array of tuples for retirement data where the tuple is of the form
# ("employee_contrib", "employer_contrib", "total")
retirement_data = [("1000", "2000", "4500"), ("8000", "16000", "30000"),
                   ("10000", "200-0", "40000"), ("3000", "6000", "12500")]

# Array of tuples for pto data where the tuple is of the form
# ("sick_days_taken", "sick_days_earned", "pto_taken", "pto_earned")
pto_data = [("2", "5", "5", "30"), ("3", "6", "3", "20"),
            ("1", "5", "10", "30"), ("4", "2", "2", "16")]

date_one = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
date_two = pytz.utc.localize(datetime.datetime(2017, 6, 2, 0, 0))
date_three = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
date_four = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))

# Array of tuples for schedule data where the tuple is of the form
# ("date_begin", "date_end", "event_type", "event_desc", "event_name")
schedule_data = [("pto", "france vacation", "vacation"),
                 ("pto", "going home", "Visit Parents"),
                 ("pto", "Grand Canyon Trip", "AZ Trip"),
                 ("pto", "Xmas break", "Christmas Leave")]

# Array of tuples for work_info data where the tuple is of the form
# ("income", "bonuses", years_worked, "SSN", "DoB")
work_info_data = [("$50,000", "$10,000", 2, "666-66-6666", "01-01-1980"),
                  ("$40,000", "$10,000", 1, "777-77-7777", "01-01-1979"),
                  ("$60,000", "$12,000", 3, "888-888-8888", "01-04-1982"),
                  ("$30,000", "$7,000", 1, "999-99-9999", "02-03-1981")]

# Array of tuples for performance data where the tuple is of the form
# ("comments", date_submitted, score)
performance_data = [("Great job! You are my hero", date_one, 5),
                    ("Once again, you've done a great job this year.", date_two, 5),
                    ("Ehh, you are okay, we will let you stay..... barely", date_one, 2),
                    ("Good enough", date_one, 3)]

reviewer = User.objects.create(
    user_id=112,
    email="reviewer@contrastsecurity.com", password="12321",
    is_admin=True, first_name="Reviewer",
    last_name="Guy", created_at=date_one,
    updated_at=date_one, auth_token="auth_token"
)
