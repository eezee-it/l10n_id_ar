# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from osv import fields, osv
from tools.translate import _

class set_cash_account(osv.osv_memory):

    _name='account.set_cash_account'
    _description = 'Set Cash Account'

    _columns = {
        'name': fields.char(string='Cash Account Name', size=64, required=True),
		'currency_id' : fields.many2one(obj='res.currency', string='Currency'),
        'wizard_id': fields.many2one(obj='wizard.multi.charts.accounts', string='Wizard Multi Chart Accounts', required=False),
    }

set_cash_account()
