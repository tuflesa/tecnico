from rest_framework import routers
from .views import RepuestoConPrecioViewSet, PrecioRepuestoViewSet, MovimientoTrazabilidadViewSet, ArticulosFueraStockViewSet, LineaPedidoPendViewSet, EntregaViewSet, LineaAdicionalPedidoViewSet, LineasSalidaVieSet, MovimientoDetailViewSet, PedidoViewSet, InventarioViewSet, LineaPedidoViewSet, PedidoDetailViewSet, ContactoViewSet, MovimientoViewSet, PedidoListViewSet, ProveedorDetailViewSet, ProveedorViewSet, RepuestoListViewSet, RepuestoDetailViewSet, SalidaVieSet, StockMinimoDetailViewSet, StockMinimoViewSet, AlmacenViewSet, LineaInventarioViewSet, TipoRepuestoViewSet, TipoUnidadViewSet

router = routers.DefaultRouter()
router.register('pedido', PedidoViewSet)
router.register('linea_pedido_pend', LineaPedidoPendViewSet)
router.register('repuesto_precio', RepuestoConPrecioViewSet)
router.register('precio', PrecioRepuestoViewSet)
router.register('tipo_unidad', TipoUnidadViewSet)
router.register('linea_adicional_pedido', LineaAdicionalPedidoViewSet)
router.register('movimiento', MovimientoViewSet)
router.register('entrega', EntregaViewSet)
router.register('linea_pedido', LineaPedidoViewSet)
router.register('lista', RepuestoListViewSet)
router.register('detalle', RepuestoDetailViewSet)
router.register('tipo_repuesto', TipoRepuestoViewSet)
router.register('stocks_minimos', StockMinimoViewSet)
router.register('almacen', AlmacenViewSet)
router.register('inventario', InventarioViewSet)
router.register('lineainventario', LineaInventarioViewSet)
router.register('movimiento_trazabilidad', MovimientoTrazabilidadViewSet)
router.register('movimiento_detalle', MovimientoDetailViewSet)
router.register('proveedor', ProveedorViewSet)
router.register('proveedor_detalle', ProveedorDetailViewSet)
router.register('contacto', ContactoViewSet)
router.register('lista_pedidos', PedidoListViewSet)
router.register('pedido_detalle', PedidoDetailViewSet)
router.register('articulos_fuera_stock',ArticulosFueraStockViewSet)
router.register('stocks_minimo_detalle', StockMinimoDetailViewSet)
router.register('salida', SalidaVieSet)
router.register('lineasalida', LineasSalidaVieSet)


urlpatterns = router.urls