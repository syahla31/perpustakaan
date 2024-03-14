from datetime import datetime, timedelta
from odoo import api, fields, models, tools

class DataPeminjaman(models.Model):
    _name = 'data.peminjaman'
    _description = 'Model untuk data Peminjaman'
    
    tgl_pem = fields.Date(string='Tgl Peminjaman', default=lambda self: fields.Date.today())
    tgl_pen = fields.Date(string='Tgl Pengembalian', compute='_compute_tgl_pen')
    buku_id= fields.Many2one(
        "data.buku", 
        string='Judul Buku', 
        domain=[('tersedia','=', True)],
        required=True)
    
    name = fields.Many2one("data.anggota", string='Nama Anggota', required=True)
    
    @api.depends('tgl_pem')
    def _compute_tgl_pen(self):
        for record in self:
            if record.tgl_pem:
                record.tgl_pen = record.tgl_pem + timedelta(days=14)
