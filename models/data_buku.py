from odoo import api, fields, models

class DataBuku(models.Model):
    _name = 'data.buku'
    _description = 'Model untuk data buku'
    
    penulis = fields.Char(string='Penulis Buku')
    name = fields.Char(string='Judul Buku')
    cover = fields.Image(string='Cover Buku')
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

    kanban_group = fields.Selection([
        ('peminjaman', 'Jumlah Peminjaman')],
        string='Kanban Group')
    
    peminjaman_count = fields.Integer(string='Jumlah Peminjaman', compute='_compute_peminjaman_count',  store = True)
    library_id = fields.Many2one('data.library', string='Library')
    @api.depends('peminjaman_ids')
    def _compute_peminjaman_count(self):
        for buku in self:
            buku.peminjaman_count = len(buku.peminjaman_ids)

    def get_loan_count(self):
        return sum(self.mapped('peminjaman_count'))

    def get_available_book_count(self):
        return self.search_count([('tersedia', '=', True)])

    def get_return_count(self):
        return sum(self.mapped('peminjaman_ids.returnbuku_ids'))
    