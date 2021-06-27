import calendar
from collections import deque
import datetime

class BaseCalendarMixin:
    # カレンダー関連Mixinの、基底クラス
    first_weekday = 6  # 0は月曜から、1は火曜から。6なら日曜から
    week_names = ['MON','TUE','WED','THU','FRI','SAT','SUN']

    def setup_calendar(self):
        # <内部カレンダーの設定処理>
        # calendar.Calendarクラスの機能を利用するため、インスタンス化。
        # Calendarクラスのmonthdatescalendarメソッドを利用しているが、デフォルトが月曜日からで、
        # first_weekday=6 にしているので、今回は日曜日から

        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        # first_weekdayにあわせて、week_namesをシフト
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names



class MonthCalendarMixin(BaseCalendarMixin):
    # 月間カレンダーの機能を提供するMixin
    def get_previous_month(self, date):
        # 前月を返す
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)

    def get_next_month(self, date):
        # 次月を返す
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        # その月の全ての日を返す
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        # 現在の月を返す
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        # 月間カレンダー情報の入った辞書を返す
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data
