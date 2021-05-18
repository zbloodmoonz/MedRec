from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView, DetailView

from .forms import *


# Create your views here.
class PatientCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = PatientCreation
    template_name = 'MedRecAppointments/patient_form.html'
    form_class = CreatePatient
    success_url = '/staff'
    context_object_name = 'patient'

    def get_queryset(self):
        return PatientCreation.objects.all()


class AppointmentCreation(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Appointment
    template_name = 'MedRecAppointments/appointment.html'
    form_class = AppointmentForm
    success_url = '/staff'


class PrescriptionCreation(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Prescription
    template_name = 'MedRecAppointments/prescription.html'
    form_class = PrescriptionForm
    success_url = '/staff'


class IndexView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'MedRecAppointments/index.html'
    context_object_name = 'appointment'

    def get_queryset(self):
        return Appointment.objects.all()

    def get_context_data(self, **kwargs):
        patient = super(IndexView, self).get_context_data(**kwargs)
        patient['patient'] = PatientCreation.objects.all()
        return patient


class MedHistoryAndPrescriptionList(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'MedRecAppointments/history&prescriptions.html'

    def get_context_data(self, **kwargs):
        context = super(MedHistoryAndPrescriptionList, self).get_context_data(**kwargs)
        context['prescription'] = Prescription.objects.all()
        context['patient'] = PatientCreation.objects.all()
        return context


class PatientMeta(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(PatientView, self).get_context_data(**kwargs)
        context['object'] = Prescription.objects.all()
        context['patient'] = PatientCreation.object.all()
        return context


class PatientView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = PatientCreation
    template_name = 'MedRecAppointments/patientdetails.html'