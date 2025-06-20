#Code 1 Source : https://gist.github.com/copernicusmarinegist/b57417225d0d4ea47c5d6200f9d8cac3

import xarray as xr
#import os
netcdf_file_in = r'D:\My_Stuff\IIT-J Academics\Subjects\BTP\Dataset\Vertical_Velo_Wind.nc'
ds = xr.open_dataset(netcdf_file_in)
df = ds.to_dataframe()
df.to_csv(r'D:\My_Stuff\IIT-J Academics\Subjects\BTP\Dataset\Vertical_Velo_Wind.csv')
print('Done')

#Code 2 Source : https://pypi.org/project/netcdf2csv/

#Code 3 Source : To checkout each field https://www.youtube.com/watch?v=hrm5RmsVXo0&list=PLLxyyob7YmEE8S3QDs1PZQkiBxA4zn_Gx&index=3
