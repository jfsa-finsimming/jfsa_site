from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from .models import Team, NationalMember, Position, Member, Tag, NewsPost,PostManager, Event, Race, JFSACupResult, JFSACupRecord, JFSACupMedia
from django.core.paginator import Paginator
from django.views import generic
from . import calendar
import random

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
        context.update({'news_posts':data})
        return context


class TrialView(CommonTemplateView):
    # トライアルページを表示させるビュー
    template_name = 'app/trial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Event.objects.filter(tags__name="trial").order_by('event_date').published().is_public()[0:6]
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
        upload_years = NationalMember.objects.order_by('-selected_year').values('selected_year').distinct()
        context.update({'members':data,'year':year,'upload_years':upload_years})
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Race.objects.is_public()
        context.update({'races':data})
        return context

class RaceJfsaView(CommonTemplateView):
    # 学生記録会のページを表示させるビュー
    template_name = 'app/race-jfsa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record = JFSACupRecord.objects.first()
        results = JFSACupResult.objects.is_public()[0:6]

        pk_list = []
        max_id = JFSACupMedia.objects.all().aggregate(max_id=Max("id"))['max_id']
        for i in range(10):
            while True:
                pk = random.randint(1, max_id)
                pre_photos = JFSACupMedia.objects.filter(pk=pk).first()
                if pre_photos:
                    break
                else:
                    continue
            pk_list.append(pk)
        photos = JFSACupMedia.objects.filter(pk__in=pk_list)

        context.update({'record':record,'results':results,'photos':photos})
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = self.object
        prev = NewsPost.objects.published().is_public().filter(published_at__lt=news.published_at).order_by('published_at').last()
        next = NewsPost.objects.published().is_public().filter(published_at__gt=news.published_at).order_by('published_at').first()
        context.update({'prev':prev,'next':next})
        return context


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
