from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Black Widow'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        users = [
            User(username='ironman', email='ironman@marvel.com', team='Marvel', leaderboard_score=100),
            User(username='captainamerica', email='cap@marvel.com', team='Marvel', leaderboard_score=90),
            User(username='thor', email='thor@marvel.com', team='Marvel', leaderboard_score=95),
            User(username='blackwidow', email='widow@marvel.com', team='Marvel', leaderboard_score=85),
            User(username='superman', email='superman@dc.com', team='DC', leaderboard_score=110),
            User(username='batman', email='batman@dc.com', team='DC', leaderboard_score=105),
            User(username='wonderwoman', email='wonder@dc.com', team='DC', leaderboard_score=100),
            User(username='flash', email='flash@dc.com', team='DC', leaderboard_score=90),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user='ironman', type='run', duration=30, calories=300)
        Activity.objects.create(user='superman', type='swim', duration=45, calories=400)

        # Leaderboard
        for user in users:
            Leaderboard.objects.create(user=user.username, score=user.leaderboard_score)

        # Workouts
        Workout.objects.create(name='Push Ups', description='Do 20 push ups', difficulty='Easy')
        Workout.objects.create(name='Sprint', description='Run 100m as fast as possible', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))