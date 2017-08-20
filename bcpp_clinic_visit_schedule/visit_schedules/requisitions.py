from edc_visit_schedule.visit import Requisition, FormsCollection, Panel

RESEARCH_BLOOD_DRAW = 'Research Blood Draw'
VIRAL_LOAD = 'Viral Load'

rdb_panel = Panel(name=RESEARCH_BLOOD_DRAW)
viral_load_panel = Panel(name=VIRAL_LOAD)

app_label = 'bcpp_clinic_subject'

requisitions = FormsCollection(
    Requisition(
        show_order=10, model=f'{app_label}.subjectrequisition',
        panel=rdb_panel, required=True, additional=False),
    Requisition(
        show_order=20, model=f'{app_label}.subjectrequisition',
        panel=viral_load_panel, additional=False),
)
