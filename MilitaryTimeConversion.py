def MilitaryTimeConverter(time):
    time_dict = { 0 : 'zero', 1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five',
                  6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11: 'eleven',
                  12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                  16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                  30: 'thirty', 40: 'fourty', 50: 'fifty'}

    military_time=[]
    time=list(time)
    colon=time.index(":")
    hours=int("".join(time[:colon]))
    minutes=time[colon+1:]
    am_pm="".join(minutes[2:])
    minutes=list(str(int("".join(minutes[:2]))))

    if am_pm=="PM":
        hours+=12
    if hours==12 and am_pm=="AM":
        hours=0
    if len(list(str(hours)))==1 and hours!=0:
        military_time.append("zero")
    military_time.append(time_dict[hours])


    if minutes[0]=='0':
        military_time.append("hundred hours")
    elif len(minutes)==1:
        military_time.append("zero")
        military_time.append(time_dict[int(minutes[0])])
    elif len(minutes)==2 and int("".join(minutes))>19:
        military_time.append(time_dict[int(minutes[0])*10])
        if minutes[1]!='0':
            military_time.append(time_dict[int(minutes[1])])
    elif len(minutes)==2 and int("".join(minutes))<20:
        military_time.append(time_dict[int("".join(minutes))])
    return " ".join(military_time)
