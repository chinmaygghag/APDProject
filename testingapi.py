from datetime import timedelta, date
import csv
import requests
import pandas

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)



def setupAndIntial():
    start_date = date(2007, 01, 01)
    end_date = date(2009, 12, 31)
    source = "USD"
    currencies = "INR"
    f = open('data3.csv', "w")
    fields = ['date','source','tocurrency','rate']
    writer = csv.DictWriter(f,fields)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        d = start_date + timedelta(i)
        date_str = d.strftime('%Y-%m-%d')
        api = "http://apilayer.net/api/historical?access_key=3d1ce82772572a5fe161bd5e4bc6daeb&date=" + date_str + "&source=" + source + "&currencies=" + currencies
        response = requests.get(api)
        data = response.json()
        print data
        rate = data['quotes'][source+currencies]
        writer.writerow({'date': d, 'source': source, 'tocurrency': currencies , 'rate':rate})

    f.close()


def appendDayofweek():
    reader = csv.reader(open('2018/2018.csv', 'rb'))
    writer = csv.writer(open('2018/2018_final.csv', 'w'))
    headers = reader.next()
    headers.append("Day Of Week")
    writer.writerow(headers)
    for row in reader:
        dt = row[0]
        year, month, day = (int(x) for x in dt.split('-'))
        answer = date(year, month, day).weekday()
        row.append(answer)
        writer.writerow(row)




if __name__ == '__main__':
    setupAndIntial()
    # appendDayofweek()



