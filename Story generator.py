import random
when = ['A few months ago', 'Yesterday night', 'Last Sunday', 'Far in the past', 'On 1st February']
who = ['operation', 'captain', 'swordsman', 'robotAI', 'student']
name = ['Misaki', 'Luffy', 'Zoro', 'Doraemon', 'Norman']
residence = ['LA', 'London', 'Paris', 'Stuttgart', 'Tokyo']
went =['conference', 'library', 'museum', 'university', 'lab']
happened = ['Took a public speaking', 'wrote journals', 'discovered modern art', 'went for the lectures', 'attended workshops']
print(random.choice(when) + ', ' + random.choice(who) + ' that stayed in ' + random.choice(residence) + ', was headed to the ' + random.choice(went) + ' and ' + random.choice(happened))
