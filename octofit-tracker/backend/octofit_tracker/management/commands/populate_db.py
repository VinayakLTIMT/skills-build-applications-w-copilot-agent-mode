from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Refresh users from DB to get PKs
        users = list(User.objects.all())

        # Create activities
        Activity.objects.bulk_create([
            Activity(user=users[0], type='Running', duration=30, date=date.today()),
            Activity(user=users[1], type='Cycling', duration=45, date=date.today()),
            Activity(user=users[2], type='Swimming', duration=60, date=date.today()),
            Activity(user=users[3], type='Running', duration=25, date=date.today()),
            Activity(user=users[4], type='Cycling', duration=50, date=date.today()),
            Activity(user=users[5], type='Swimming', duration=70, date=date.today()),
        ])

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Endurance', description='Endurance workout for superheroes')
        workout2 = Workout.objects.create(name='Power Circuit', description='Strength and power circuit')
        workout1.suggested_for.set(users[:3])
        workout2.suggested_for.set(users[3:])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, score=300)
        Leaderboard.objects.create(team=dc, score=280)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
