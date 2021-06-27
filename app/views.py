from django.shortcuts import render, get_object_or_404
from .models import Team, NationalMember, Position, Member, Tag, NewsPost,PostManager, Event
from django.core.paginator import Paginator
from django.views import generic
from . import calendar


class CommonTemplateView(calendar.MonthCalendarMixin, generic.TemplateView):
    # 月間カレンダーを表示するTemplatView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class CommonListView(calendar.MonthCalendarMixin, generic.ListView):
    # 月間カレンダーを表示するListView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class CommonDetailView(calendar.MonthCalendarMixin, generic.DetailView):
    # 月間カレンダーを表示するDetailView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context



class TopView(CommonTemplateView):
    # トップページを表示させるビュー
    template_name = 'app/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = NewsPost.objects.order_by('-published_at').published().is_public()[0:6]
        context.update({'news_lists':data})
        return context


class TrialView(CommonTemplateView):
    # トライアルページを表示させるビュー
    template_name = 'app/trial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Event.objects.filter(tags__name="trial").order_by('-event_date').published().is_public()[0:6]
        context.update({'events':data})
        return context


class TeamView(CommonTemplateView):
    # チームのトップページを表示させるビュー
    template_name = 'app/team-top.html'


class TeamCollegeView(CommonListView):
    # 大学チームを表示させるビュー
    template_name = 'app/team-college.html'
    model = Team
    paginate_by = 8
    queryset = Team.objects.filter(college_or_club = 'college')
    context_object_name = "teams"


class TeamClubView(CommonListView):
    # クラブチームを表示させるビュー
    template_name = 'app/team-club.html'
    model = Team
    paginate_by = 8
    queryset = Team.objects.filter(college_or_club = 'club')
    context_object_name = "teams"


class TeamNationalView(CommonTemplateView):
    template_name = 'app/team-national.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('year'):
            year = self.kwargs.get('year')
        else:
            year = str(NationalMember.objects.first().selected_year.year)

        data = NationalMember.objects.filter(selected_year__year=year)
        context.update({'members':data,'year':year,})
        return context


class TrainingView(CommonTemplateView):
    # trainingのトップページを表示させるビュー
    template_name = 'app/training-top.html'


class TrainingJfsaView(CommonTemplateView):
    # 練習会のページを表示させるビュー
    template_name = 'app/training-jfsa.html'


class TrainingStoryView(CommonTemplateView):
    # 学生の練習風景を表示させるビュー
    template_name = 'app/training-story.html'


class RaceView(CommonTemplateView):
    # raceのトップページを表示させるビュー
    template_name = 'app/race-top.html'


class RaceJfsaView(CommonTemplateView):
    # 学生記録会のページを表示させるビュー
    template_name = 'app/race-jfsa.html'


class RaceOnlineView(CommonTemplateView):
    # 学生記録会のページを表示させるビュー
    template_name = 'app/race-online.html'


class NewsView(CommonListView):
    # Newsの一覧を表示させるビュー
    template_name = 'app/news-top.html'
    model = NewsPost
    paginate_by = 8
    queryset = NewsPost.objects.order_by('-published_at').published().is_public()
    context_object_name = "news_posts"


class NewsDetailView(CommonDetailView):
    template_name = 'app/news-detail.html'
    model = NewsPost
    context_object_name = "news_detail"


class AboutView(CommonTemplateView):
    # aboutのページを表示させるビュー
    template_name = 'app/about-top.html'


class AboutFinView(CommonTemplateView):
    # aboutのページを表示させるビュー
    template_name = 'app/about-fin.html'


class AboutJfsaView(CommonTemplateView):
    # aboutのページを表示させるビュー
    template_name = 'app/about-jfsa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Member.objects.all()
        context.update({'members':data})
        return context
