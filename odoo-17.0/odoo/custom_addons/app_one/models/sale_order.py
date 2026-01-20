
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    property_id = fields.Many2one('property')

    def action_confirm(self):
        # كود قبل التأكيد
        print(f"Confirming order {self.name}")

        # تنفيذ التأكيد الأصلي
        res = super(SaleOrder, self).action_confirm()

        # كود بعد التأكيد
        print(f"Order {self.name} confirmed successfully")
        # يمكن إضافة: إرسال إيميل، إنشاء سجل، إلخ.

        return res

