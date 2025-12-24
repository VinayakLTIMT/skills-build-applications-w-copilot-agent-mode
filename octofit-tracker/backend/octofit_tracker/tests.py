from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=30, date='2025-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, score=100)
        self.workout.suggested_for.set([self.user])

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team, self.team)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Test Activity')

    def test_workout(self):
        self.assertIn(self.user, self.workout.suggested_for.all())

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)
