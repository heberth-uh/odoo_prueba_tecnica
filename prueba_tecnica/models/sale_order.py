from odoo import fields, models
from odoo.exceptions import ValidationError

class SaleOrderPruebaTecnica(models.Model):
    _inherit = 'sale.order'

    delivery_date = fields.Date('Fecha estimada de entrega')

    def action_confirm(self):
        # Herencia método para Confirmar venta
        self.send_sale_summary()
        return super(SaleOrderPruebaTecnica, self).action_confirm()

    def send_sale_summary(self):
        # Validaciones previasa
        if not self.delivery_date:
            raise ValidationError(f'Especifique una fecha de entrega estimada.')
        if not self.env.user.email:
            raise ValidationError(f'Se requiere el correo electrónico del remitente; {self.env.user.partner_id.display_name}.')
        if not self.partner_id.email:
            raise ValidationError(f'Se requiere el correo electrónico del destinatario; {self.partner_id.display_name}.')

        # Envío de correo electrónico
        mail_summary_template = self.env.ref('prueba_tecnica.email_sale_summary', False)
        if mail_summary_template:
            mail_summary_template.send_mail(self.id, force_send=True)


