from statistics import mean, median, stdev, quantiles
from ios_sensor_pack.models import Location
locations = Location.objects.all().order_by('id')
old_timestamp = None
time_difference_list = []
for location in locations:
    if old_timestamp:
        time_difference = location.sat_timestamp - old_timestamp
        time_difference_seconds = time_difference.total_seconds()
        time_difference_list.append(time_difference_seconds)
        
    old_timestamp = location.sat_timestamp

print("min: %s\nmax: %s\nmean: %s\nmedian: %s\nstdev: %s\nquantiles: %s" % (
            str(min((time_difference_list))),
            str(max(time_difference_list)),
            str(mean(time_difference_list)),
            str(median(time_difference_list)),
            str(stdev(time_difference_list)),
            str(quantiles(time_difference_list)),
        )
    )
