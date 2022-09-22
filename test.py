import datetime
end_date = '12-02-2022'
end_date = datetime.datetime.strptime(end_date, '%m-%d-%Y')
end_date += datetime.timedelta(days=1)
print(end_date)


