import pandas as pd
from data.platosRestaurante import platosPopulares
from helpers.crearTabla import crearTabla
tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)