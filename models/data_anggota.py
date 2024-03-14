from odoo import api, fields, models
from odoo.exceptions import ValidationError

class DataAnggota(models.Model):
    _name = 'data.anggota'
    _description = 'Model untuk Data Anggota'
    
    name = fields.Char(string='Nama Anggota')
    id_ang= fields.Integer(string='ID Anggota')
    jk_ang = fields.Selection(string='Jenis Kelamin', selection=[('cowo', 'Laki-Laki'), ('cewe', 'Perempuan'),])
    no_telp = fields.Char(string='No Handphone')
    alamat = fields.Text(string='Alamat')
    foto = fields.Binary(string='Foto')
    
    @api.constrains('no_telp')
    def _check_valid_input(self):
        for record in self:
            if not record.no_telp.isdigit() or len(record.no_telp) < 10 or len(record.no_telp) > 13:
                raise ValidationError("Nomor telp harus terdiri dari 10 hingga 13 angka!")