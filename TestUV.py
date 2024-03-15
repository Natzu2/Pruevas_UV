from pyowm import OWM
owm = OWM('25e4f8c6b58ce79d30fb2f9f51c1d1a6')
uv_mgr = owm.uvindex_manager()
uv_index = uv_mgr.uvindex_around_coords(27.967115, -110.918797)
print(f"UV Index: {uv_index.value}")
print(f"Exposure Risk: {uv_index.get_exposure_risk()}")