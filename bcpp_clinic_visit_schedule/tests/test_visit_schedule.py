from django.test import TestCase
from edc_visit_schedule.site_visit_schedules import site_visit_schedules


class TestVisitSchedule(TestCase):

    def test(self):
        site_visit_schedules.validate()
