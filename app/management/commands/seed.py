import binascii
import datetime

import pytz
from Crypto import Random
from django.core.management.base import BaseCommand

from app.models import User, PaidTimeOff, Retirement, Schedule, KeyManagement, WorkInfo, Performance, Message

users = [
    {
        "id": 1,
        "user_id": 1,
        "email": "admin@metacorp.com",
        "is_admin": True,
        "password": "admin1234",
        "first_name": "Admin",
        "last_name": "",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 2,
        "user_id": 2,
        "email": "jack@metacorp.com",
        "is_admin": False,
        "password": "yankeessuck",
        "first_name": "Jack",
        "last_name": "Mannino",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 3,
        "user_id": 3,
        "email": "jim@metacorp.com",
        "is_admin": False,
        "password": "alohaowasp",
        "first_name": "Jim",
        "last_name": "Manico",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 4, 
        "user_id": 4, 
        "email": "mike@metacorp.com",
        "is_admin": False,
        "password": "motocross1445",
        "first_name": "Mike",
        "last_name": "McCabe",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "id": 5,
        "user_id": 5,
        "email": "ken@metacorp.com",
        "is_admin": False,
        "password": "citrusblend",
        "first_name": "Ken",
        "last_name": "Johnson",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]

retirements = [
    {
        "user_id": 2,
        "employee_contrib": "1000",
        "employer_contrib": "2000",
        "total": "4500",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 3,
        "employee_contrib": "8000",
        "employer_contrib": "16000",
        "total": "30000",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 4,
        "employee_contrib": "10000",
        "employer_contrib": "20000",
        "total": "40000",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 5,
        "employee_contrib": "3000",
        "employer_contrib": "6000",
        "total": "12500",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]

paid_time_off = [
    {
        "user_id": 2,
        "sick_days_taken": 2,
        "sick_days_earned": 5,
        "pto_taken": 5,
        "pto_earned": 30,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 3,
        "sick_days_taken": 3,
        "sick_days_earned": 6,
        "pto_taken": 3,
        "pto_earned": 20,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 4,
        "sick_days_taken": 2,
        "sick_days_earned": 5,
        "pto_taken": 5,
        "pto_earned": 30,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 5,
        "sick_days_taken": 1,
        "sick_days_earned": 5,
        "pto_taken": 10,
        "pto_earned": 30,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]

schedule = [
    {
        "user_id": 2,
        "date_begin": pytz.utc.localize(datetime.datetime.now()),
        "date_end": pytz.utc.localize(datetime.datetime.now()),
        "event_type": "pto",
        "event_desc": "vacation to france",
        "event_name": "My 2014 Vacation",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())

    },
    {
        "user_id": 3,
        "date_begin": pytz.utc.localize(datetime.datetime.now()),
        "date_end": pytz.utc.localize(datetime.datetime.now()),
        "event_type": "pto",
        "event_desc": "Going Home to see folks",
        "event_name": "Visit Parents",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())

    },
    {
        "user_id": 4,
        "date_begin": pytz.utc.localize(datetime.datetime.now()),
        "date_end": pytz.utc.localize(datetime.datetime.now()),
        "event_type": "pto",
        "event_desc": "Taking kids to Grand Canyon",
        "event_name": "AZ Trip",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())

    },
    {
        "user_id": 5,
        "date_begin": pytz.utc.localize(datetime.datetime.now()),
        "date_end": pytz.utc.localize(datetime.datetime.now()),
        "event_type": "pto",
        "event_desc": "Xmas Staycation",
        "event_name": "Christmas Leave",
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }

]

work_info = [
    {
        "user_id": 2,
        "income": "$50,000",
        "bonuses": "$10,000",
        "years_worked": 2,
        "SSN": "555-55-5555",
        "DoB": datetime.date(1996, 7, 31),
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 3,
        "income": "$40,000",
        "bonuses": "$10,000",
        "years_worked": 1,
        "SSN": "333-33-3333",
        "DoB": datetime.date(1996, 7, 31),
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 4,
        "income": "$60,000",
        "bonuses": "$12,000",
        "years_worked": 3,
        "SSN": "444-44-4444",
        "DoB": datetime.date(1996, 7, 31),
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 5,
        "income": "$30,000",
        "bonuses": "7,000",
        "years_worked": 1,
        "SSN": "222-22-2222",
        "DoB": datetime.date(1996, 7, 31),
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]

performance = [
    {
        "user_id": 2,
        "comments": "Great job! You are my hero",
        "date_submitted": pytz.utc.localize(datetime.datetime.now()),
        "score": 5,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 2,
        "comments": "Once again, you've done a great job this year. We greatly appreciate your hard work.",
        "date_submitted": pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0)),
        "score": 5,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 3,
        "comments": "Great worker, great attitude for this newcomer!",
        "date_submitted": pytz.utc.localize(datetime.datetime.now()),
        "score": 5,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 4,
        "comments": "Wow, right out of the gate we've been very impressed but unfortunately, our system doesn't allow us to give you a full 5.0 because other ppl have gotten 5.0 ratings.",
        "date_submitted": pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0)),
        "score": 4,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 4,
        "comments": "We highly recommend promotion for this employee! Consistent performer with proven leadership qualities.",
        "date_submitted":  pytz.utc.localize(datetime.datetime(2017, 6, 2, 0, 0)),
        "score": 5,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 4,
        "comments": "Right out of the gate, Mike has made incredible moves as a newly appointed leader. His only improvement would be more cowbell. Not enough of it.",
        "date_submitted": pytz.utc.localize(datetime.datetime.now()),
        "score": 4,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "user_id": 5,
        "comments": "Ehh, you are okay, we will let you stay..... barely",
        "date_submitted": pytz.utc.localize(datetime.datetime.now()),
        "score": 2,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]

messages = [
    {
        "receiver_id": 2,
        "creator_id": 5,
        "message": 'Your benefits have been updated.',
        "read": False,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "receiver_id": 3,
        "creator_id": 4,
        "message": 'Please update your profile.',
        "read": False,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "receiver_id": 4,
        "creator_id": 3,
        "message": 'Welcome to Railsgoat.',
        "read": False,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    },
    {
        "receiver_id": 5,
        "creator_id": 2,
        "message": 'Hello friend.',
        "read": False,
        "created_at": pytz.utc.localize(datetime.datetime.now()),
        "updated_at": pytz.utc.localize(datetime.datetime.now())
    }
]


class Command(BaseCommand):
    def create_users(self):
        for obj in users:
            u = User.objects.create(**obj)
            u.generate_token()
            User.objects.filter(pk=u.pk).update(**{'auth_token': u.auth_token})

    def create_paid_time_off(self):
        for obj in paid_time_off:
            PaidTimeOff.objects.create(**obj)

    def create_retirements(self):
        for obj in retirements:
            Retirement.objects.create(**obj)

    def create_schedule(self):
        for obj in schedule:
            Schedule.objects.create(**obj)

    def create_key_management(self):
        for counter in range(1, len(users) + 1):
            user = User.objects.get(user_id=counter)
            KeyManagement.objects.create(iv=binascii.hexlify(Random.new().read(8)), user=user,
                                         created_at=pytz.utc.localize(datetime.datetime.now()),
                                         updated_at=pytz.utc.localize(datetime.datetime.now()))

    def create_work_info(self):
        for obj in work_info:
            wi = WorkInfo.objects.create(**obj)
            wi.encrypted_ssn = wi.encrypt_ssn()

    def create_performance(self):
        for obj in performance:
            obj['reviewer'] = User.objects.get(user_id=1)
            Performance.objects.create(**obj)

    def create_messages(self):
        for obj in messages:
            Message.objects.create(**obj)

    def handle(self, *args, **options):
        self.create_users()
        self.create_paid_time_off()
        self.create_retirements()
        self.create_schedule()
        self.create_key_management()
        self.create_work_info()
        self.create_performance()
        self.create_messages()
