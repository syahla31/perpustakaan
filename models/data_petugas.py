from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError

class DataPetugas(models.Model):

    _name = 'data.petugas'
    _description = 'Model untuk data Petugas'
    
    id_p= fields.Integer(string='ID Petugas')
    name = fields.Char(string='Nama Petugas')
    jabatan = fields.Selection(string='Jabatan', selection=[('pk', 'Pustakawan'), ('a_pk', 'Asisten Pustakawan'),('sf', 'Staff')])
    no_HP = fields.Char(string='No Handphone')
    alamat_p = fields.Text(string='Alamat')
    
    @api.constrains('no_HP')
    def _check_valid_input(self):
        for record in self:
            if not record.no_HP.isdigit() or len(record.no_HP) < 10 or len(record.no_HP) > 13:
                raise ValidationError("Nomor telp harus terdiri dari 10 hingga 13 angka!")
