import json
import codecs
from urllib.parse import urlencode

from django.test import TestCase, Client

from tournament.models import Player, Tournament


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


class TournamentTestCase(TestCase):

    def setUp(self):
        Tournament.objects.all().delete()

        self.alfred = Player.objects.create(name='Alfred')
        self.brad = Player.objects.create(name='Brad')
        self.charles = Player.objects.create(name='Charles')
        self.darcy = Player.objects.create(name='Darcy')

        self.c = Client()

    def test_can_list_tournament(self):
        t1 = Tournament.objects.create(name='Knockout')
        t2 = Tournament.objects.create(name='World Cup')
        t1.players.add(self.alfred.id,self.brad.id,self.darcy.id)
        t2.players.add(self.charles.id,self.brad.id,self.darcy.id)

        response = self.c.get('/tournaments/')
        tournament_dict = json.loads(response.content.decode('utf-8'))

        self.assertEquals(2, len(tournament_dict))
        self.assertEquals(['Knockout','World Cup'], [t['name'] for t in tournament_dict])
        self.assertEquals([{self.alfred.id,self.brad.id,self.darcy.id},{self.brad.id,self.darcy.id,self.charles.id}],
                          [set(t['players']) for t in tournament_dict])

    def test_can_create_tournament(self):
        response = self.c.post('/tournaments/', {'name': 'Smack-Down',
                                                 'players': [self.alfred.id,self.charles.id]})

        self.assertEquals(201, response.status_code)

        sd = Tournament.objects.get(name='Smack-Down')
        self.assertEquals('Smack-Down',sd.name)
        self.assertEquals({self.alfred,self.charles}, set(sd.players.all()))

    def test_can_delete_tournament(self):
        t1 = Tournament.objects.create(name='Shoot-out')
        t1.players.add(self.alfred.id,self.brad.id,self.darcy.id)

        response = self.c.delete('/tournaments/%s/' % t1.id)
        self.assertEquals(204, response.status_code)

        all_tournaments = Tournament.objects.all()
        for tournament in all_tournaments:
            self.assertNotEqual('Shoot-out',tournament.name)

    def test_can_retrieve_tournament(self):
        t = Tournament.objects.create(name='Bracket Challenge')
        t.players.add(self.charles.id,self.brad.id,self.darcy.id)

        response = self.c.get('/tournaments/%s/' % t.id)
        tournament_dict = json.loads(response.content.decode('utf-8'))
        self.assertEquals('Bracket Challenge', tournament_dict['name'])
        self.assertEquals({self.charles.id,self.brad.id,self.darcy.id},
                          set(tournament_dict['players']))

    def test_can_update_tournament(self):
        t = Tournament.objects.create(name='Elimimation')
        t.players.add(self.charles.id,self.brad.id)

        body = {'name': 'Eliminator'}
        response = self.c.put('/tournaments/%s/' % t.id,
                              urlencode(body),
                              content_type='application/x-www-form-urlencoded')

        self.assertEquals(200, response.status_code)
        retrieved_t = Tournament.objects.get(id=t.id)
        self.assertEquals('Eliminator', retrieved_t.name)

