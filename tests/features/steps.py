# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_p1_and_p2_start_a_match_to_pacted_sets(step, p1, p2, sets):
    world.match = m.Match(p1, p2, sets)


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score(step, score):
    assert world.match.score() == score, "Got %s" % world.match.score()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_player_won_the_set_num(step, p1, set_num, num1, num2):
    world.match.add(p1, int(set_num[0]), num1, num2)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_player_won_the_set_num(step, p1, set_num, num1, num2):
    world.match.add(p1, int(set_num[0]), num1, num2)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_p1(step, score):
    assert world.match.score() == score, "Got %s" % world.match.score()
