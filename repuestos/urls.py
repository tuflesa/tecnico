from rest_framework import routers
from .views import PedidoViewSet, InventarioViewSet, LineaPedidoViewSet, PedidoDetailViewSet, ContactoViewSet, MovimientoViewSet, PedidoListViewSet, ProveedorDetailViewSet, ProveedorViewSet, RepuestoListViewSet, RepuestoDetailViewSet, StockMinimoViewSet, AlmacenViewSet, LineaInventarioViewSet, TipoRepuestoViewSet

router = routers.DefaultRouter()
router.register('pedido', PedidoViewSet)
router.register('linea_pedido', LineaPedidoViewSet)
router.register('lista', RepuestoListViewSet)
router.register('detalle', RepuestoDetailViewSet)
router.register('tipo_repuesto', TipoRepuestoViewSet)
router.register('stocks_minimos', StockMinimoViewSet)
router.register('almacen', AlmacenViewSet)
router.register('inventario', InventarioViewSet)
router.register('lineainventario', LineaInventarioViewSet)
router.register('movimiento', MovimientoViewSet)
router.register('proveedor', ProveedorViewSet)
router.register('proveedor_detalle', ProveedorDetailViewSet)
router.register('contacto', ContactoViewSet)
router.register('lista_pedidos', PedidoListViewSet)
router.register('pedido_detalle', PedidoDetailViewSet)


urlpatterns = router.urls