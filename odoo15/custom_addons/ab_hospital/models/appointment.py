# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    ref = fields.Integer(string='Referance', help="Regerance from the patient record")
    patient_id = fields.Many2one(comodel_name='hospital.patient', string="Patient")
    age = fields.Integer(string='Age')
    gender = fields.Selection(related="patient_id.gender")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")
    Pharmacy = fields.Html(string="Pharmacy")

    priority = fields.Selection([('0', 'Normal'),
                                 ('1', 'Low'),
                                 ('2', 'High'),
                                 ('3', 'Very High'), ], string='Priority')

    state = fields.Selection([('draft', 'Draft'),
                              ('in_consultation', 'In_Consultation'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel'), ], default='draft', string='Status', required=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string="Hide Sales Price")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button Clicked !!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfully',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_in_done(self):
        for rec in self:
            rec.state = 'done'

    # def action_in_cancel(self):
    #     for rec in self:
    #         rec.state = 'cancel'

    def action_in_cancel(self):
        action = self.env.ref("ab_hospital.action_cancel_appointment").read()[0]
        return action

    def action_in_draft(self):
        for rec in self:
            rec.state = 'draft'


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(related='product_id.list_price', required=True)
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
