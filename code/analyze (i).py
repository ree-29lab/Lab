# 步骤 1： 打开文件并读取核心头信息 (Header Information)
from astropy.io import fits

# 打开FITS文件
file_path = 'jw02722-o004_t001_miri_p750l-slitlessprism_x1dints.fits'
hdul = fits.open(file_path)

# 打印主头信息中的关键内容
header = hdul[0].header
print("=== 观测目标信息 (Observation Target Info) ===")
print(f"目标名称 (Target Name - TARGNAME): {header.get('TARGNAME', 'Not Found')}")
print(f"提案标题 (Proposal Title - TITLE): {header.get('TITLE', 'Not Found')}")
print(f"观测对象 (Object - OBJECT): {header.get('OBJECT', 'Not Found')}")
print(f"仪器 (Instrument): {header.get('INSTRUME', 'Not Found')}")
print(f")")
print("=== 数据文件结构 (File Structure) ===")
hdul.info() # 这行会显示文件有多少个部分(HDU)
