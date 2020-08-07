import datetime
from dateutil.relativedelta import relativedelta

paid_holidays_list = [10, 11, 12, 14, 16, 18, 20]
cnt = 0


date = input('入社日を入力してください。 ex.20200831 ⇒　')
date = datetime.datetime.strptime(date, '%Y%m%d')  # 入力した日付からdatetimeを生成
date = date.date()  # datetimeをdateに変換

# 半年後の日付（最初の有給付与日）
date = date + relativedelta(months=6)
print('付与日：{0}　付与日数：{1}'.format(date, paid_holidays_list[cnt]))
cnt += 1

year = date.year

flg = False  # 基本的には半年後の付与日と同じ年にもう一度付与日が来るかどうかのフラグ

while year <= datetime.datetime.today().year:

    # 2020年以降の有給付与日は4/11、以前は5/1
    if year >= 2020:
        if date < datetime.date(year=year, month=4, day=11):
            date = datetime.date(year=year, month=4, day=11)
            flg = True
    else:
        if date < datetime.date(year=year, month=5, day=1):
            date = datetime.date(year=year, month=5, day=1)
            flg = True

    if flg:
        print('付与日：{0}　付与日数：{1}'.format(date, paid_holidays_list[cnt]))
        cnt += 1
        if cnt >= len(paid_holidays_list):
            cnt = len(paid_holidays_list) - 1

    year += 1
    date = datetime.date(year=year, month=1, day=1)
