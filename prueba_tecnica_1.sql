SELECT 
    pt.name AS product_name,
    pt.hs_code AS barcode,
    MAX(po.date_order) AS last_purchase_date,
    MAX(so.date_order) AS last_sale_date
FROM product_template pt
LEFT JOIN purchase_order_line po_line ON po_line.product_id = pt.id
LEFT JOIN purchase_order po ON po.id = po_line.order_id
LEFT JOIN sale_order_line so_line ON so_line.product_id = pt.id
LEFT JOIN sale_order so ON so.id = so_line.order_id
GROUP BY pt.id;