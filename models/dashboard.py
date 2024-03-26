from odoo import models, fields

class Library(models.Model):
    _name = 'data.library'
    _description = 'Library'

    name = fields.Char(string='Name', required=True)
    book_count = fields.Integer(string='Book Count')
    member_count = fields.Integer(string='Member Count')
    loan_count = fields.Integer(string='Loan Count')
    refund_count = fields.Integer(string='Refund Count')
    kanban_group = fields.Selection([
        ('book', 'Books'),
        ('member', 'Members'),
        ('loan', 'Loans'),
        ('refunds', 'Refunds')],
        string='Kanban Group')

    book_ids = fields.One2many('data.buku', 'library_id', string='Books')
    member_ids = fields.One2many('data.anggota', 'library_id', string='Members')
    loan_ids = fields.One2many('data.peminjaman', 'library_id', string='Loans')
    return_ids = fields.One2many('data.returnbuku', 'library_id', string='Return')
