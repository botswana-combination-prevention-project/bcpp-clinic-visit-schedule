from edc_visit_schedule.visit import Crf, FormsCollection

app_label = 'bcpp_clinic_subject'

crfs = FormsCollection(
    Crf(show_order=1, model=f'{app_label}.questionnaire'),
    Crf(show_order=2, model=f'{app_label}.viralloadtracking'),
    Crf(show_order=3, model=f'{app_label}.vlresult'))
