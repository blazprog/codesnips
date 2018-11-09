# -*- coding: utf-8 -*-

# onchange method
# kako priredim vrednost many2many polju
#@api.onchange('member_id')
def onchange_member(self):
    loan = self.env['library.book.loan']
    loans = loan.search(
        [('state', '=', 'ongoing'),
        ('member_id', '=', self.member_id.id)]
    )
    self.book_ids = loans.mapped('book_id')


d = datetime.date(year=2018, month=2, day=20)
print d.isoformat()

I have created a my own new snippet juhhu
I am on the road to became snippet master
of disaster

I have created a my own new snippet 
I am on the road to became snippet master

I have created a my own new snippet a
I am on the road to became snippet master
l
I have just created a my own new snippet 
my snippet 
I am on the road to became snippet master
really
I have just created a my own new snippet 
item 
I am on the road to became snippet master
pass
