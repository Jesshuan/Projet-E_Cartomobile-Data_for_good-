import geopandas as gpd

from e_cartomobile.data_transform.communes import dep_str_to_int


def get_communes_metropole_geo(filename="notebooks/datas/a-com2022-topo.json"):
    gdf_communes = gpd.read_file(filename)

    gdf_communes = gdf_communes.set_crs(crs="EPSG:4326")

    gdf_communes_metropole = gdf_communes.loc[
        gdf_communes.dep.apply(dep_str_to_int) < 100
    ]

    return gdf_communes_metropole