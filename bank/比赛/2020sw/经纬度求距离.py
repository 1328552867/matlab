import math

lng_A = 111.599628
lat_A = 40.844048

lng_B = 111.604371
lat_B = 40.836106

R = 6371.004
pi = 3.141592654
#经度：113.37935836 纬度：31.71785761
#东经为正的经度，西经为负的经度，北纬为90-纬度，南纬为90+纬度
#上述数据为东经北纬
Mlng_A = lng_A
Mlat_A = 90 - lat_A

Mlng_B = lng_B
Mlat_B = 90 - lat_B
C = math.sin(Mlat_A*pi/180) * math.sin(Mlat_B*pi/180) * math.cos((Mlng_A - Mlng_B)*pi/180) +math.cos(Mlat_A*pi/180) * math.cos(Mlat_B*pi/180)
Distance = R * math.acos(C) * 1000
print(Distance)
