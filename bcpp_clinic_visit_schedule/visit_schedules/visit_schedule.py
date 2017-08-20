from django.core.management.color import color_style

from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule1


style = color_style()


visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='BCPP Clinic Survey',
    app_label='bcpp_clinic_subject',
    visit_model='bcpp_clinic_subject.subjectvisit',
    offstudy_model='bcpp_clinic_subject.subjectoffstudy',
    previous_visit_schedule=None,
)

visit_schedule1.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule1)
