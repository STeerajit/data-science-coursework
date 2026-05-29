import pandas as pd

# ชื่อคอลัมน์ทั้งหมดของชุดข้อมูลรถยนต์
columns = [
    "symboling", "normalized-losses", "make", "fuel-type", "aspiration",
    "num-of-doors", "body-style", "drive-wheels", "engine-location",
    "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
    "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg",
    "price"
]

# อ่านไฟล์ autos.csv ที่ไม่มี header แล้วตั้งชื่อคอลัมน์เอง
df = pd.read_csv("data/autos.csv", header=None, names=columns)
df.to_csv("autos_with_headers.csv", index=False)