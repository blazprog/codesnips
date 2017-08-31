# onchange method
# kako priredim vrednost many2many polju
@api.onchange('member_id')
def onchange_member(self):
    loan = self.env['library.book.loan']
    loans = loan.search(
        [('state', '=', 'ongoing'),
        ('member_id', '=', self.member_id.id)]
    )
    self.book_ids = loans.mapped('book_id')
