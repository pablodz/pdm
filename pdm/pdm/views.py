from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
###########################################################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
###########################################################


# from .models import ProductoHijoCompra
# from .models import ProductoPadre
# from .models import Proveedor
# from .models import BoletaCompra
# ###########################################################
# from .models import ProductoPlato
# from .models import PlatoPadre
# from .models import PlatoHijoVenta
# from .models import BoletaVentaRestaurante
# from .models import ProductoHijoTransaccion


###########################################################
from django.utils.timezone import get_current_timezone
import datetime
##########################################################
from django.db.models import Count
from django.db.models import Sum
from django.db.models import F

# ------------------------ INICIO INDEX ------------------


def index_view(request):

    # Variables de reporte mensual
    cantidadPlatosMes = 900
    porcentajeRespectoMesAnterior = 112.5

    return render(request, 'index/index.html', locals())

# -------------------------- FIN INDEX -------------------

# -------------------- INICIO DASHBOARD -----------------
@login_required(login_url='/accounts/login')
def dashboard_view(request):

    nombre_vista = 'Dashboard'
    ruta_vista = ['Dashboard']

    # Variables de reporte mensual
    cantidadPlatosMes = 900
    porcentajeRespectoMesAnterior = 112.5

    porcentajeComprasMesActual = 18
    montoComprasMesActual = 10390.50
    porcentajeVentasMesActual = 17
    montoVentasMesActual = 35215.48
    porcentajeIngresosMesActual = 15
    montoIngresosMesActual = 14568.35
    porcentajeImpuestosMesActual = 14
    montoImpuestosMesActual = 5482.21

    # Para mostrar en tabla vamos a usar GROUPBY
    # tutorial sacado de https://stackoverflow.com/a/629600/10491422
    # tablaBoletasCompra = ProductoHijoCompra.objects.raw(
    #     'SELECT MIN(id) AS id,MAX(id_boleta_compra) AS id_boleta_compra, SUM(precio) AS precio_total, COUNT(*) AS nro_productos FROM producto_hijo_compra GROUP BY id_boleta_compra ORDER BY id_boleta_compra DESC;')
    # tablaBoletasVenta = PlatoHijoVenta.objects.raw(
    #     'SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')
    # sumaBoletasVentasMes=
    # sumaBoletasComprasMes=PlatoHijoVenta.objects.raw('SELECT MIN(id) AS id, MAX(id_boleta_venta_restaurante) AS id_boleta_venta_restaurante, SUM(precio_venta) AS precio_total,  COUNT(*) AS nro_productos  FROM plato_hijo_venta GROUP BY id_boleta_venta_restaurante ORDER BY id_boleta_venta_restaurante DESC;')
    maxItemTabla = 5

    return render(request, 'dashboard/dashboard.html', locals())
# ----------------------- FIN DASHBOARD -----------------
