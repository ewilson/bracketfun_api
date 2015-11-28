import json
from urllib.parse import urlencode

from django.test import TestCase, Client
from django.db import IntegrityError

from tournament.models import Player, Tournament, Match, Entry


class PlayerTestCase(TestCase):

    def setUp(self):
        Player.objects.all().delete()
        self.c = Client()

    def test_can_list_player(self):
        Player.objects.create(name='Abe')
        Player.objects.create(name='Ben')

        response = self.c.get('/players/')
        player_dict = json.loads(response.content.decode('utf-8'))

        self.assertEquals(2, len(player_dict))
        self.assertEquals(['Abe','Ben'], [p['name'] for p in player_dict])

    def test_can_create_player(self):
        response = self.c.post('/players/', {'name': 'Caleb'})

        self.assertEquals(201, response.status_code)

        caleb = Player.objects.get(name='Caleb')
        self.assertEquals('Caleb',caleb.name)

    def test_can_delete_player(self):
        david = Player.objects.create(name='David')
        pid = david.id

        response = self.c.delete('/players/%s/' % pid)
        self.assertEquals(204, response.status_code)

        all_players = Player.objects.all()
        for player in all_players:
            self.assertNotEqual('David',player.name)

    def test_can_retrieve_player(self):
        ezekiel = Player.objects.create(name='Ezekiel')
        pid = ezekiel.id

        response = self.c.get('/players/%d/' % pid)
        ezekiel_dict = json.loads(response.content.decode('utf-8'))

        self.assertEquals(pid, ezekiel_dict['id'])
        self.assertEquals('Ezekiel', ezekiel_dict['name'])

    def test_can_update_player(self):
        f = Player.objects.create(name='Festus')
        pid = f.id

        response = self.c.put('/players/%s/' % pid,
                              urlencode({'name': 'Felix'}),
                              content_type='application/x-www-form-urlencoded')
        felix = Player.objects.get(id=pid)
        self.assertEquals('Felix', felix.name)

    def test_cannot_delete_player_in_tournament(self):
        g = Player.objects.create(name='Gabe')
        t = Tournament.objects.create(title='Persistence')
        e = Entry.objects.create(player=g, tournament=t)

        response = self.c.delete('/players/%s/' % g.id)

        self.assertEquals(409, response.status_code)


class TournamentTestCase(TestCase):

    def setUp(self):
        Tournament.objects.all().delete()

        self.alfred = Player.objects.create(name='Alfred')
        self.brad = Player.objects.create(name='Brad')
        self.charles = Player.objects.create(name='Charles')
        self.darcy = Player.objects.create(name='Darcy')

        self.c = Client()

    def test_can_list_tournament(self):
        t1 = Tournament.objects.create(title='Knockout')
        t2 = Tournament.objects.create(title='World Cup')
        a1 = Entry.objects.create(player=self.alfred, tournament=t1)
        b1 = Entry.objects.create(player=self.brad, tournament=t1)
        d1 = Entry.objects.create(player=self.darcy, tournament=t1)
        a2 = Entry.objects.create(player=self.alfred, tournament=t2)
        b2 = Entry.objects.create(player=self.brad, tournament=t2)
        c2 = Entry.objects.create(player=self.charles, tournament=t2)
        t1.entries.add(a1, b1, d1)
        t2.entries.add(a2, b2, c2)

        response = self.c.get('/tournaments/')
        tournament_dict = json.loads(response.content.decode('utf-8'))

        self.assertEquals(2, len(tournament_dict))
        self.assertEquals(['Knockout','World Cup'], [t['title'] for t in tournament_dict])
        self.assertEquals([{a1.id, b1.id, d1.id}, {a2.id, b2.id, c2.id}],
                          [set(t['entries']) for t in tournament_dict])

    def test_can_create_tournament(self):
        response = self.c.post('/tournaments/', {'title': 'Smack-Down'})

        self.assertEquals(201, response.status_code)

        sd = Tournament.objects.get(title='Smack-Down')
        self.assertEquals('Smack-Down', sd.title)

    def test_can_delete_tournament(self):
        t1 = Tournament.objects.create(title='Shoot-out')
        e1 = Entry.objects.create(player=self.alfred, tournament=t1)
        e2 = Entry.objects.create(player=self.brad, tournament=t1)
        e3 = Entry.objects.create(player=self.darcy, tournament=t1)
        entry_ids = {e1.id, e2.id, e3.id}
        t1.entries.add(e1, e2, e3)
        t1.save()

        response = self.c.delete('/tournaments/%s/' % t1.id)
        self.assertEquals(204, response.status_code)

        all_tournaments = Tournament.objects.all()
        for tournament in all_tournaments:
            self.assertNotEqual('Shoot-out',tournament.title)
        all_entries = Entry.objects.all()
        for entry in all_entries:
            self.assertFalse(entry.id in entry_ids)

    def test_can_retrieve_tournament(self):
        t = Tournament.objects.create(title='Bracket Challenge')
        e1 = Entry.objects.create(player=self.alfred, tournament=t)
        e2 = Entry.objects.create(player=self.brad, tournament=t)
        e3 = Entry.objects.create(player=self.darcy, tournament=t)
        entry_ids = {e1.id, e2.id, e3.id}
        t.entries.add(e1, e2, e3)

        response = self.c.get('/tournaments/%s/' % t.id)
        tournament_dict = json.loads(response.content.decode('utf-8'))
        self.assertEquals('Bracket Challenge', tournament_dict['title'])
        self.assertEquals(entry_ids, set(tournament_dict['entries']))

    def test_can_update_tournament(self):
        t = Tournament.objects.create(title='Elimimation')
        e1 = Entry.objects.create(player=self.alfred, tournament=t)
        e2 = Entry.objects.create(player=self.brad, tournament=t)
        e3 = Entry.objects.create(player=self.darcy, tournament=t)
        t.entries.add(e1, e2, e3)

        body = {'title': 'Eliminator'}
        response = self.c.put('/tournaments/%s/' % t.id,
                              urlencode(body),
                              content_type='application/x-www-form-urlencoded')

        self.assertEquals(200, response.status_code)
        retrieved_t = Tournament.objects.get(id=t.id)
        self.assertEquals('Eliminator', retrieved_t.title)


class MatchTestCase(TestCase):

    def setUp(self):
        Tournament.objects.all().delete()
        Player.objects.all().delete()
        Match.objects.all().delete()

        self.alfred = Player.objects.create(name='Alfred')
        self.brad = Player.objects.create(name='Brad')
        self.charles = Player.objects.create(name='Charles')
        self.darcy = Player.objects.create(name='Darcy')
        self.madness = Tournament.objects.create(title='Madness')
        self.showdown = Tournament.objects.create(title='Showdown')
        self.alf_mad = Entry.objects.create(player=self.alfred, tournament=self.madness)
        self.brad_mad = Entry.objects.create(player=self.brad, tournament=self.madness)
        self.darcy_mad = Entry.objects.create(player=self.darcy, tournament=self.madness)
        # e2 = Entry.objects.create(player=self.brad, tournament=t)
        # e3 = Entry.objects.create(player=self.darcy, tournament=t)

        self.c = Client()

    def test_can_create_match(self):
        match_dict = {
            'tournament': self.madness.id, 'completed': False,
            'home_player': self.brad_mad.id, 'away_player': self.darcy_mad.id
        }
        response = self.c.post('/matches/', match_dict)

        self.assertEquals(201, response.status_code)

        created_match = Tournament.objects.get(title='Madness').matches.get()
        self.assertEquals('Brad', created_match.home_player.player.name)
        self.assertEquals('Darcy', created_match.away_player.player.name)
        self.assertEquals(False, created_match.completed)

    def test_can_delete_tournament(self):
        m1 = Match.objects.create(tournament=self.madness,
                                  home_player=self.alf_mad,
                                  away_player=self.darcy_mad)

        response = self.c.delete('/matches/%s/' % m1.id)
        self.assertEquals(204, response.status_code)

        all_matches = Match.objects.all()
        for match in all_matches:
            self.assertNotEqual(m1.id, match.id)

    def test_can_retrieve_match(self):
        m1 = Match.objects.create(tournament=self.madness,
                                  home_player=self.alf_mad,
                                  away_player=self.darcy_mad)

        response = self.c.get('/matches/%s/' % m1.id)
        self.assertEquals(200, response.status_code)

        match_dict = json.loads(response.content.decode('utf-8'))
        self.assertEquals(m1.id, match_dict['tournament'])
        self.assertEquals(self.alf_mad.id, match_dict['home_player'])
        self.assertEquals(self.darcy_mad.id, match_dict['away_player'])

    def test_can_update_match(self):
        m1 = Match.objects.create(tournament=self.madness,
                                  home_player=self.alf_mad,
                                  away_player=self.darcy_mad)
        match_dict = {
            'tournament': self.madness.id, 'completed': True,
            'home_player': self.alf_mad.id, 'away_player': self.darcy_mad.id,
            'home_score': 12, 'away_score': 21
        }
        response = self.c.put('/matches/%s/' % m1.id,
                              urlencode(match_dict),
                              content_type='application/x-www-form-urlencoded')

        self.assertEquals(200, response.status_code)
        retrieved_m = Match.objects.get(id=m1.id)
        self.assertEquals(m1, retrieved_m)
        self.assertEquals(self.alf_mad, retrieved_m.home_player)
        self.assertEquals(self.darcy_mad, retrieved_m.away_player)
        self.assertTrue(retrieved_m.completed)
        self.assertEquals(21, retrieved_m.away_score)
        self.assertEquals(12, retrieved_m.home_score)


class EntryTestCase(TestCase):

    def setUp(self):
       self.c = Client()

    def test_can_delete_entry(self):
        zed = Player.objects.create(name='Zed')
        cfp = Tournament.objects.create(title='College Football Playoffs')
        e = Entry.objects.create(player=zed, tournament=cfp)

        response = self.c.delete('/entries/%s/' % e.id)

        self.assertEquals(204, response.status_code)

    def test_can_not_enter_tournament_twice(self):
        naven = Player.objects.create(name='Naven')
        pb = Tournament.objects.create(title='Phone Book')
        e = Entry.objects.create(player=naven, tournament=pb)

        def _create_second_entry():
            e2 = Entry.objects.create(player=naven, tournament=pb)

        self.assertRaises(IntegrityError, _create_second_entry)
