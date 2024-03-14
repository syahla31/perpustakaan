from odoo import api, fields, models, tools
import logging
_logger = logging.getLogger(__name__)

class DataPengembalian(models.Model):
    _name = 'data.returnbuku'
    _description = 'Model untuk data Pengembalian'
    
    tgl_pen = fields.Date(string='Tgl Pengembalian')
    denda = fields.Integer(string='Denda', compute='_compute_denda')
    name = fields.Many2one('data.peminjaman', string='Peminjaman')
    petugas_id = fields.Many2one(
        'data.petugas',
        string='Petugas',
        )
    
    @api.depends('tgl_pen', 'name.tgl_pen')
    def _compute_denda(self):
        for record in self:
            _logger.info('tgl_pen: %s', record.tgl_pen)
            _logger.info('tgl_pen: %s', record.name.tgl_pen)
            
            if record.tgl_pen and record.name.tgl_pen:
                if record.tgl_pen > record.name.tgl_pen:
                    # Hitung selisih hari antara tanggal pengembalian dan tanggal jatuh tempo
                    selisih_hari = (record.tgl_pen - record.name.tgl_pen).days
                    _logger.info('selisih hari: %s', selisih_hari)
                    # Hitung denda
                    record.denda = selisih_hari * 10000
                else:
                    record.denda = 0
            else:
                record.denda = 0
                
    
    
    
