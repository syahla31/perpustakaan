from odoo import api, fields, models

class DataBuku(models.Model):
    _name = 'data.buku'
    _description = 'Model untuk data buku'
    
    penulis = fields.Char(string='Penulis Buku')
    name = fields.Char(string='Judul Buku')
    cover = fields.Binary(string='Cover Buku')
    id= fields.Integer(string='ID Buku')
    penerbit = fields.Char(string='Penerbit Buku')
    tahun_terbit = fields.Date(string='Tahun Terbit')
    deskripsi = fields.Text(string='Deskripsi Buku')
    tersedia = fields.Boolean(string='Tersedia')
    peminjaman_ids = fields.One2many(
        comodel_name='data.peminjaman',
        inverse_name='buku_id',
        string='Data Peminjaman'   
    )
    
    peminjaman_count = fields.Integer(string='Jumlah Peminjaman', compute='_compute_peminjaman_count',  store = True)
    @api.depends('peminjaman_ids')
    def _compute_peminjaman_count(self):
        for buku in self:
            buku.peminjaman_count = len(buku.peminjaman_ids)
    