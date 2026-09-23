import duckdb

from darkwater import paths


def test_paths_resolve_to_repo():
    assert (paths.ROOT / "pyproject.toml").exists()
    assert paths.RAW.parent == paths.DATA


def test_duckdb_spatial_loads():
    con = duckdb.connect()
    con.install_extension("spatial")
    con.load_extension("spatial")
    wkt = con.sql("select ST_AsText(ST_Point(-118.25, 33.73))").fetchone()[0]
    assert wkt.startswith("POINT")
